import asyncio
import logging

from pelicanfix.engine import DuplicateSeqNoError, FIXEngine, FIXMessageContainer
from pelicanfix.engine.codec import Codec
from pelicanfix.engine.connection import FIXConnectionHandler, ConnectionState, FIXEndPoint


class FIXServerConnectionHandler(FIXConnectionHandler):
    logger = logging.getLogger(__name__)

    def __init__(self, engine: FIXEngine, codec: Codec, reader, writer, addr=None, observer=None):
        FIXConnectionHandler.__init__(self, engine, codec, reader, writer, addr, observer)

    async def handle_session_message(self, msg: FIXMessageContainer):
        protocol = self.codec.protocol

        recv_seq_no = int(msg.get_field(protocol.Field.MSG_SEQ_NUM))

        msg_type = msg.get_field(protocol.Field.MSG_TYPE)
        target_comp_id = msg.get_field(protocol.Field.TARGET_COMP_ID)
        sender_comp_id = msg.get_field(protocol.Field.SENDER_COMP_ID)
        responses = []

        if msg_type == protocol.MsgType.LOGON.value:
            if self.connection_state == ConnectionState.LOGGED_IN:
                self.logger.warning("Client session already logged in - ignoring login request")
            else:
                # compids are reversed here...
                session_mgr = self.engine.session_manager
                self.session = session_mgr.get_or_create_session_from_comp_ids(sender_comp_id, target_comp_id)
                if self.session is not None:
                    try:
                        self.connection_state = ConnectionState.LOGGED_IN
                        self.heartbeat_period = float(msg.get_field(protocol.Field.HEART_BT_INT))
                        responses.append(self.codec.create_logon_msg())
                    except DuplicateSeqNoError:
                        logging.error("Failed to process login request with duplicate seq no")
                        await self.disconnect()
                        return
                else:
                    self.logger.warning(
                        "Rejected login attempt for invalid session (SenderCompId: %s, TargetCompId: %s)" % (
                            sender_comp_id, target_comp_id))
                    await self.disconnect()
                    return  # we have to return here since self.session won't be valid
        elif self.connection_state == ConnectionState.LOGGED_IN:
            # compids are reversed here
            if not self.session.validateCompIds(sender_comp_id, target_comp_id):
                self.logger.error("Received message with unexpected comp ids")
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
                new_seq_no = msg.get_field(protocol.Field.NEW_SEQ_NO)
                self.session.set_recv_seq_no(int(new_seq_no) - 1)
                recv_seq_no = new_seq_no
        else:
            logging.warning("Can't process message, counterparty is not logged in")

        return recv_seq_no, responses


class FIXServer(FIXEndPoint):
    logger = logging.getLogger(__name__)

    def __init__(self, engine, codec: Codec):
        FIXEndPoint.__init__(self, engine, codec.protocol)
        self.codec = codec
        self.server = None

    async def start(self, host, port, loop):
        self.connections = []
        self.server = await asyncio.start_server(self.handle_accept, host, port, loop=loop)
        self.logger.info("Awaiting connections on " + host + ":" + str(port))

    async def handle_accept(self, reader, writer):
        addr = writer.get_extra_info('peername')
        self.logger.info("Connection from %s" % repr(addr))
        connection = FIXServerConnectionHandler(self.engine, self.codec, reader, writer, addr, self)
        self.connections.append(connection)
        for handler in filter(lambda x: x[1] == ConnectionState.CONNECTED, self.connection_handlers):
            await handler[0](connection)
