import asyncio
from enum import Enum
import logging

from pelicanfix.engine import FIXEngine, MessageDirection
from pelicanfix.engine.codec import SimpleFixCodec
from pelicanfix.engine.connection import ConnectionState, FIXConnectionHandler
from pelicanfix.engine.journal import SqliteJournalProvider
from pelicanfix.engine.server import FIXServer


class Side(Enum):
    buy = 1
    sell = 2


class Server(FIXEngine):
    def __init__(self):
        FIXEngine.__init__(self, SqliteJournalProvider('server.store'))
        # create a FIX Server using the FIX 4.2 standard
        self.server = FIXServer(self, SimpleFixCodec('pelicanfix.protocol.fix44'))

        # we register some listeners since we want to know when the connection goes up or down
        self.server.add_connection_listener(self.on_connect, ConnectionState.CONNECTED)
        self.server.add_connection_listener(self.on_disconnect, ConnectionState.DISCONNECTED)

    async def start(self, host, port, loop):
        await self.server.start(host, port, loop)

    async def on_connect(self, session: FIXConnectionHandler):
        logging.info("Accepted new connection from %s" % (session.address(),))

        # register to receive message notifications on the session which has just been created
        session.add_message_handler(self.on_login, MessageDirection.OUTBOUND, self.server.protocol.MsgType.LOGON.value)
        session.add_message_handler(self.on_new_order, MessageDirection.INBOUND,
                                    self.server.protocol.MsgType.ORDER_SINGLE.value)

    async def on_disconnect(self, session: FIXConnectionHandler):
        logging.info("%s has disconnected" % (session.address(),))

        # we need to clean up our handlers, since this session is disconnected now
        session.remove_message_handler(self.on_login, MessageDirection.OUTBOUND,
                                       self.server.protocol.MsgType.LOGON.value)
        session.remove_message_handler(self.on_new_order, MessageDirection.INBOUND,
                                       self.server.protocol.MsgType.ORDER_SINGLE.value)

    # noinspection PyMethodMayBeStatic
    async def on_login(self, connection_handler, msg):
        codec = connection_handler.codec
        logging.info("[" + msg.get_field(codec.protocol.Field.SENDER_COMP_ID) + "] <---- "
                     + msg.get_field(codec.protocol.Field.MSG_TYPE))

    # noinspection PyMethodMayBeStatic
    async def on_new_order(self, connection_handler, request):
        codec = connection_handler.codec
        protocol = codec.protocol
        try:
            side = Side(int(request.get_field(codec.protocol.Field.SIDE)))
            logging.debug("<--- [%s] %s: %s %s %s@%s" % (
                request.get_field(codec.protocol.Field.MSG_TYPE),
                request.get_field(codec.protocol.Field.CL_ORD_ID),
                request.get_field(codec.protocol.Field.SYMBOL),
                side.name, request.get_field(codec.protocol.Field.ORDER_QTY),
                request.get_field(codec.protocol.Field.PRICE)))

            # respond with an ExecutionReport Ack
            msg = codec.create_message()
            msg.set_field(protocol.Field.MSG_TYPE, protocol.MsgType.EXECUTION_REPORT.value)
            msg.set_field(protocol.Field.PRICE,
                          request.get_field(protocol.Field.PRICE))
            msg.set_field(protocol.Field.ORDER_QTY,
                          request.get_field(protocol.Field.ORDER_QTY))
            msg.set_field(protocol.Field.SYMBOL,
                          request.get_field(protocol.Field.SYMBOL))
            msg.set_field(protocol.Field.SECURITY_ID, "GB00BH4HKS39")
            msg.set_field(protocol.Field.SECURITY_ID_SOURCE, "4")
            msg.set_field(protocol.Field.ACCOUNT,
                          request.get_field(protocol.Field.ACCOUNT))
            msg.set_field(protocol.Field.HANDL_INST, "1")
            msg.set_field(protocol.Field.ORD_STATUS, "0")
            msg.set_field(protocol.Field.EXEC_TYPE, "0")
            msg.set_field(protocol.Field.LEAVES_QTY, "0")
            msg.set_field(protocol.Field.SIDE,
                          request.get_field(protocol.Field.SIDE))
            msg.set_field(protocol.Field.CL_ORD_ID,
                          request.get_field(protocol.Field.CL_ORD_ID))
            msg.set_field(protocol.Field.CURRENCY,
                          request.get_field(protocol.Field.CURRENCY))

            await connection_handler.send_msg(msg)
            logging.debug("---> [%s] %s: %s %s %s@%s" % (
                msg.get_field(protocol.Field.MSG_TYPE),
                msg.get_field(protocol.Field.CL_ORD_ID),
                request.get_field(protocol.Field.SYMBOL),
                side.name,
                request.get_field(protocol.Field.ORDER_QTY),
                request.get_field(protocol.Field.PRICE)))
        except Exception as e:
            msg = codec.create_message()
            msg.set_field(protocol.Field.MSG_TYPE, protocol.MsgType.EXECUTION_REPORT.value)
            msg.set_field(protocol.Field.ORD_STATUS, "4")
            msg.set_field(protocol.Field.EXEC_TYPE, "4")
            msg.set_field(protocol.Field.LEAVES_QTY, "0")
            msg.set_field(protocol.Field.TEXT, str(e))
            msg.set_field(protocol.Field.CL_ORD_ID,
                          request.get_field(protocol.Field.CL_ORD_ID))

            await connection_handler.send_msg(msg)


def main():
    logging.basicConfig(level=logging.DEBUG)
    loop = asyncio.get_event_loop()
    server = Server()
    loop.run_until_complete(server.start('', 9898, loop))
    loop.run_forever()


if __name__ == '__main__':
    main()
