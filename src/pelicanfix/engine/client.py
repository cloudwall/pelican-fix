import asyncio
import logging

from pelicanfix.engine import DuplicateSeqNoError, FIXMessageContainer
from pelicanfix.engine.codec import Codec
from pelicanfix.engine.connection import FIXConnectionHandler, ConnectionState, FIXEndPoint


class FIXClientConnectionHandler(FIXConnectionHandler):
    def __init__(self, engine, codec, target_comp_id: str, sender_comp_id: str, reader, writer, addr=None,
                 observer=None, target_sub_id: str = None, sender_sub_id: str = None, heartbeat_timeout: float = 30,
                 heartbeat: int = 1):
        FIXConnectionHandler.__init__(self, engine, codec, reader, writer, addr, observer)

        self.target_comp_id = target_comp_id
        self.sender_comp_id = sender_comp_id
        self.target_sub_id = target_sub_id
        self.sender_sub_id = sender_sub_id
        self.heartbeat_timeout = heartbeat_timeout
        self.heartbeat = heartbeat

        # we need to send a login request.
        self.session = self.engine.session_manager.get_or_create_session_from_comp_ids(self.target_comp_id,
                                                                                       self.sender_comp_id)
        if self.session is None:
            raise RuntimeError("Failed to create client session")

        self.protocol = codec.protocol

        asyncio.ensure_future(self.logon())

    async def logon(self):
        logon_msg = self.codec.create_logon_msg()
        logon_msg.set_field(self.protocol.Field.HEART_BT_INT, str(self.heartbeat))
        await self.send_msg(logon_msg)

    async def handle_session_message(self, msg: FIXMessageContainer):
        protocol = self.codec.protocol
        responses = []

        recv_seq_no = int(msg.get_field(protocol.Field.MSG_SEQ_NUM))

        msg_type = msg.get_field(protocol.Field.MSG_TYPE)
        target_comp_id = msg.get_field(protocol.Field.TARGET_COMP_ID)
        sender_comp_id = msg.get_field(protocol.Field.SENDER_COMP_ID)

        if msg_type == protocol.MsgType.LOGON.value:
            if self.connection_state == ConnectionState.LOGGED_IN:
                logging.warning("Client session already logged in - ignoring login request")
            else:
                try:
                    self.connection_state = ConnectionState.LOGGED_IN
                    self.heartbeat_period = float(msg.get_field(protocol.Field.HEART_BT_INT))
                except DuplicateSeqNoError:
                    logging.error("Failed to process login request with duplicate seq no")
                    await self.disconnect()
                    return
        elif self.connection_state == ConnectionState.LOGGED_IN:
            # compids are reversed here
            if not self.session.validateCompIds(sender_comp_id, target_comp_id):
                logging.error("Received message with unexpected comp ids")
                await self.disconnect()
                return

            if msg_type == protocol.MsgType.LOGOUT.value:
                self.connection_state = ConnectionState.LOGGED_OUT
                await self.handle_close()
            elif msg_type == protocol.MsgType.TEST_REQUEST.value:
                responses.append(self.codec.create_heartbeat_msg())
            elif msg_type == protocol.MsgType.RESEND_REQUEST.value:
                responses.extend(self._handle_resend_request(msg))
            elif msg_type == protocol.MsgType.SEQUENCE_RESET.value:
                # we can treat GapFill and SequenceReset in the same way
                # in both cases we will just reset the seq number to the
                # NewSeqNo received in the message
                new_seq_no = msg.get_field(protocol.Field.NEW_SEQ_NO)
                if msg.get_field(protocol.Field.GAP_FILL_FLAG) == "Y":
                    logging.info("Received SequenceReset(GapFill) filling gap from %s to %s"
                                 % (recv_seq_no, new_seq_no))
                self.session.set_recv_seq_no(int(new_seq_no) - 1)
                recv_seq_no = new_seq_no
        else:
            logging.warning("Can't process message, counterparty is not logged in")

        return recv_seq_no, responses


class FIXClient(FIXEndPoint):
    def __init__(self, engine, codec: Codec, target_comp_id: str, sender_comp_id: str, target_sub_id: str = None,
                 sender_sub_id: str = None, heartbeat_timeout: float = 30, with_seq_no_reset: bool = True):
        self.codec = codec
        self.target_comp_id = target_comp_id
        self.sender_comp_id = sender_comp_id
        self.target_sub_id = target_sub_id
        self.sender_sub_id = sender_sub_id
        self.heartbeat_timeout = heartbeat_timeout
        self.with_seq_no_reset = with_seq_no_reset
        self.reader = self.writer = None
        self.addr = None

        FIXEndPoint.__init__(self, engine, codec.protocol)

    async def start(self, host, port, loop):
        self.reader, self.writer = await asyncio.open_connection(host, port, loop=loop)
        self.addr = (host, port)
        logging.info("Connected to %s" % repr(self.addr))
        connection = FIXClientConnectionHandler(self.engine, self.codec, self.target_comp_id, self.sender_comp_id,
                                                self.reader, self.writer, self.addr, self, self.target_sub_id,
                                                self.sender_sub_id, self.heartbeat_timeout)
        self.connections.append(connection)
        for handler in filter(lambda x: x[1] == ConnectionState.CONNECTED, self.connection_handlers):
            await handler[0](connection)

    def stop(self):
        logging.info("Stopping client connections")
        for connection in self.connections:
            connection.disconnect()
        self.writer.close()
