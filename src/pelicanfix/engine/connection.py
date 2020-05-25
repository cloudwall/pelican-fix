import asyncio
import logging
import sys

from enum import Enum

from pelicanfix.engine import FIXEngine, DuplicateSeqNoError, MessageDirection, FIXMessageContainer
from pelicanfix.engine.codec import Codec


class ConnectionState(Enum):
    UNKNOWN = 0
    DISCONNECTED = 1
    CONNECTED = 2
    LOGGED_IN = 3
    LOGGED_OUT = 4


class FIXException(Exception):
    class FIXExceptionReason(Enum):
        NOT_CONNECTED = 0
        DECODE_ERROR = 1
        ENCODE_ERROR = 2

    def __init__(self, reason: FIXExceptionReason, description: str = None):
        super(Exception, self).__init__(description)
        self.reason = reason


class SessionWarning(Exception):
    pass


class SessionError(Exception):
    pass


class FIXConnectionHandler(object):
    logger = logging.getLogger(__name__)

    def __init__(self, engine: FIXEngine, codec: Codec, reader, writer, addr=None, observer=None):
        self.codec = codec
        self.engine = engine
        self.connection_state = ConnectionState.CONNECTED
        self.session = None
        self.addr = addr
        self.observer = observer
        self.msg_buffer = b''
        self.heartbeat_period = 30.0
        self.msg_handlers = []
        self.reader = reader
        self.writer = writer
        self.heartbeat_timer_registration = None
        self.expected_heartbeat_registration = None
        asyncio.ensure_future(self.handle_read())

    def address(self) -> str:
        return self.addr

    async def disconnect(self):
        await self.handle_close()

    def add_message_handler(self, handler, direction: MessageDirection = None, msg_type=None):
        self.msg_handlers.append((handler, direction, msg_type))

    def remove_message_handler(self, handler, direction=None, msg_type=None):
        remove = filter(lambda x: (x[0] == handler) and
                                  (x[1] == direction or direction is None) and
                                  (x[2] == msg_type or msg_type is None), self.msg_handlers)
        for h in remove:
            self.msg_handlers.remove(h)

    async def handle_read(self):
        while True:
            try:
                msg = await self.reader.read(8192)
                if not msg:
                    raise ConnectionError
                self.msg_buffer = self.msg_buffer + msg
                while True:
                    if self.connection_state == ConnectionState.DISCONNECTED:
                        break

                    (decoded_msg, parsed_length) = self.codec.decode(self.msg_buffer)
                    if decoded_msg is None:
                        break
                    await self.process_message(decoded_msg)
                    self.msg_buffer = self.msg_buffer[parsed_length:]
            except ConnectionError as why:
                self.logger.debug("Connection has been closed %s" % (why,))
                await self.disconnect()
                return

    async def handle_session_message(self, msg):
        return -1

    async def process_message(self, decoded_msg: FIXMessageContainer):
        protocol = self.codec.protocol

        begin_string = decoded_msg.get_field(protocol.Field.BEGIN_STRING.value.get_number())
        if begin_string != protocol.BEGIN_STRING:
            self.logger.error("FIX BeginString is incorrect (expected: %s received: %s)",
                              (protocol.BEGIN_STRING, begin_string))
            await self.disconnect()
            return

        msg_type = decoded_msg.get_field(protocol.Field.MSG_TYPE.value.get_number())
        recv_seq_no = 0
        try:
            responses = []
            if msg_type in self.codec.get_session_msg_types():
                (recv_seq_no, responses) = await self.handle_session_message(decoded_msg)
            else:
                recv_seq_no = int(decoded_msg.get_field(protocol.Field.MSG_SEQ_NUM.value.get_number()))

            # validate the seq number
            (seq_no_state, last_known_seq_no) = self.session.validate_recv_seq_no(recv_seq_no)

            if seq_no_state is False:
                # We should send a resend request
                self.logger.info("Requesting resend of messages: %s to %s" % (last_known_seq_no, 0))
                responses.append(self.codec.create_resend_request(last_known_seq_no, 0))
                # we still need to notify if we are processing Logon message
                if msg_type == protocol.MsgType.LOGON.value:
                    await self.__notify_message_observers(decoded_msg, MessageDirection.INBOUND, False)
            else:
                self.session.set_recv_seq_no(recv_seq_no)
                await self.__notify_message_observers(decoded_msg, MessageDirection.INBOUND)

            for m in responses:
                await self.send_msg(m)

        except SessionWarning as sw:
            self.logger.warning(sw)
        except SessionError as se:
            self.logger.error(se)
            await self.disconnect()
        except DuplicateSeqNoError:
            try:
                if decoded_msg.has_field(protocol.Field.POSS_DUP_FLAG) and \
                        decoded_msg.get_field(protocol.Field.POSS_DUP_FLAG.value.get_number()) == "Y":
                    self.logger.debug("Received duplicate message with PossDupFlag set")
            finally:
                self.logger.error(
                    "Failed to process message with duplicate seq no (MsgSeqNum: %s) (and no PossDupFlag='Y') "
                    "- disconnecting" % (recv_seq_no,))
                await self.disconnect()

    async def handle_close(self):
        if self.connection_state != ConnectionState.DISCONNECTED:
            self.logger.info("Client disconnected")
            self.writer.close()
            self.connection_state = ConnectionState.DISCONNECTED
            self.msg_handlers.clear()
            if self.observer is not None:
                await self.observer.notify_disconnect(self)

    async def send_msg(self, msg: FIXMessageContainer):
        if self.connection_state != ConnectionState.CONNECTED and self.connection_state != ConnectionState.LOGGED_IN:
            return

        encoded_msg = self.codec.encode(msg, self.session)
        self.writer.write(encoded_msg)
        await self.writer.drain()
        decoded_msg, junk = self.codec.decode(encoded_msg)

        try:
            await self.__notify_message_observers(decoded_msg, MessageDirection.OUTBOUND)
        except DuplicateSeqNoError:
            self.logger.error("We have sent a message with a duplicate seq no, failed to persist it (MsgSeqNum: %s)" % (
                decoded_msg.get_field(self.codec.protocol.Field.MSG_SEQ_NUM.value.get_number())))

    def _handle_resend_request(self, msg: FIXMessageContainer):
        protocol = self.codec.protocol
        responses = []

        begin_seq_no = int(msg.get_field(protocol.Field.BEGIN_SEQ_NO.value.get_number()))
        end_seq_no = int(msg.get_field(protocol.Field.END_SEQ_NO.value.get_number()))
        if end_seq_no == 0:
            end_seq_no = sys.maxsize
        self.logger.info("Received resent request from %s to %s", begin_seq_no, end_seq_no)
        replay_msgs = self.engine.journal_provider.recover_msgs(self.session, MessageDirection.OUTBOUND, begin_seq_no,
                                                                end_seq_no)
        gap_fill_begin = int(begin_seq_no)
        gap_fill_end = int(begin_seq_no)
        for replay_msg in replay_msgs:
            msg_seq_num = int(replay_msg.get_field(protocol.Field.MSG_SEQ_NUM.value.get_number()))
            if replay_msg.get_field(protocol.Field.MSG_TYPE.value.get_number()) in self.codec.get_session_msg_types():
                gap_fill_end = msg_seq_num + 1
            else:
                if self.engine.should_resend_message(self.session, replay_msg):
                    if gap_fill_begin < gap_fill_end:
                        # we need to send a gap fill message
                        gap_fill_msg = self.codec.create_message()
                        gap_fill_msg.set_field(protocol.Field.MSG_TYPE.value.get_number(),
                                               protocol.MsgType.SEQUENCE_RESET)
                        gap_fill_msg.set_field(protocol.Field.GAP_FILL_FLAG.value.get_number(), 'Y')
                        gap_fill_msg.set_field(protocol.Field.MSG_SEQ_NUM.value.get_number(), str(gap_fill_begin))
                        gap_fill_msg.set_field(protocol.Field.NEW_SEQ_NO.value.get_number(), str(gap_fill_end))
                        responses.append(gap_fill_msg)

                    # and then send the replay_msg
                    replay_msg.remove_field(protocol.Field.BEGIN_STRING.value.get_number())
                    replay_msg.remove_field(protocol.Field.BODY_LENGTH.value.get_number())
                    replay_msg.remove_field(protocol.Field.SENDING_TIME.value.get_number())
                    replay_msg.remove_field(protocol.Field.SENDER_COMP_ID.value.get_number())
                    replay_msg.remove_field(protocol.Field.TARGET_COMP_ID.value.get_number())
                    replay_msg.remove_field(protocol.Field.CHECK_SUM.value.get_number())
                    replay_msg.set_field(protocol.Field.POSS_DUP_FLAG.value.get_number(), "Y")
                    responses.append(replay_msg)

                    gap_fill_begin = msg_seq_num + 1
                else:
                    gap_fill_end = msg_seq_num + 1
                    responses.append(replay_msg)

        if gap_fill_begin < gap_fill_end:
            # we need to send a gap fill message
            gap_fill_msg = self.codec.create_message()
            gap_fill_msg.set_field(protocol.Field.MSG_TYPE.value.get_number(), protocol.MsgType.SEQUENCE_RESET.value)
            gap_fill_msg.set_field(protocol.Field.GAP_FILL_FLAG.value.get_number(), 'Y')
            gap_fill_msg.set_field(protocol.Field.MSG_SEQ_NUM.value.get_number(), str(gap_fill_begin))
            gap_fill_msg.set_field(protocol.Field.NEW_SEQ_NO.value.get_number(), str(gap_fill_end))
            responses.append(gap_fill_msg)

        return responses

    async def __notify_message_observers(self, msg: FIXMessageContainer, direction: MessageDirection,
                                         persist_msg: bool = True):
        if persist_msg is True:
            self.engine.journal_provider.persist_msg(msg, self.session, direction)

        msg_type = msg.get_field(self.codec.protocol.Field.MSG_TYPE.value.get_number())
        for handler in filter(lambda x: (x[1] is None or x[1] == direction) and
                                        (x[2] is None or x[2] == msg_type),
                              self.msg_handlers):
            await handler[0](self, msg)


class FIXEndPoint(object):
    def __init__(self, engine, protocol):
        self.engine = engine
        self.protocol = protocol

        self.connections = []
        self.connection_handlers = []

    # noinspection PyMethodMayBeStatic
    def writable(self):
        return True

    def start(self, host, port, loop):
        pass

    def stop(self):
        pass

    def add_connection_listener(self, handler, filter_expr):
        self.connection_handlers.append((handler, filter_expr))

    def remove_connection_listener(self, handler, filter_expr):
        for s in self.connection_handlers:
            if s == (handler, filter_expr):
                self.connection_handlers.remove(s)

    async def notify_disconnect(self, connection):
        self.connections.remove(connection)
        for handler in filter(lambda x: x[1] == ConnectionState.DISCONNECTED, self.connection_handlers):
            await handler[0](connection)
