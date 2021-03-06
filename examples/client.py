import asyncio
import uuid
from enum import Enum
import logging
import random

from pelicanfix.engine import FIXEngine, MessageDirection, FIXMessageContainer
from pelicanfix.engine.client import FIXClient
from pelicanfix.engine.codec import SimpleFixCodec
from pelicanfix.engine.connection import ConnectionState, FIXConnectionHandler
from pelicanfix.engine.journal import SqliteJournalProvider


class Side(Enum):
    buy = 1
    sell = 2


class Client(FIXEngine):
    def __init__(self):
        FIXEngine.__init__(self, SqliteJournalProvider('client.store'))
        self.clOrdID = 0
        self.msgGenerator = None

        # create a FIX Client using the FIX 4.4 standard
        codec = SimpleFixCodec('pelicanfix.protocol.fix44')
        self.client = FIXClient(self, codec, "TARGET", "SENDER")

        # we register some listeners since we want to know when the connection goes up or down
        self.client.add_connection_listener(self.on_connect, ConnectionState.CONNECTED)
        self.client.add_connection_listener(self.on_disconnect, ConnectionState.DISCONNECTED)

    async def start(self, host, port, loop):
        await self.client.start(host, port, loop)

    async def on_connect(self, session: FIXConnectionHandler):
        logging.info("Established connection to %s" % (session.address(),))
        # register to receive message notifications on the session which has just been created
        session.add_message_handler(self.on_login, MessageDirection.INBOUND,
                                    self.client.protocol.MsgType.LOGON.value)
        session.add_message_handler(self.on_execution_report, MessageDirection.INBOUND,
                                    self.client.protocol.MsgType.EXECUTION_REPORT.value)

    async def on_disconnect(self, session: FIXConnectionHandler):
        logging.info("%s has disconnected" % (session.address(),))
        # we need to clean up our handlers, since this session is disconnected now
        session.remove_message_handler(self.on_login, MessageDirection.INBOUND,
                                       self.client.protocol.MsgType.LOGON.value)
        session.remove_message_handler(self.on_execution_report, MessageDirection.INBOUND,
                                       self.client.protocol.MsgType.EXECUTION_REPORT.value)

    async def send_order(self, connection_handler: FIXConnectionHandler):
        self.clOrdID = self.clOrdID + 1
        codec = connection_handler.codec
        protocol = codec.protocol

        msg = codec.create_message()
        msg.set_field(protocol.Field.MSG_TYPE, protocol.MsgType.ORDER_SINGLE.value)
        msg.set_field(protocol.Field.BEGIN_STRING, 'FIX.4.4')
        msg.set_field(protocol.Field.MSG_TYPE, protocol.MsgType.ORDER_SINGLE.value)
        msg.set_field(protocol.Field.PRICE, "%0.2f" % (random.random() * 2 + 10))
        msg.set_field(protocol.Field.ORDER_QTY, str(int(random.random() * 100)))
        msg.set_field(protocol.Field.SYMBOL, "VOD.L")
        msg.set_field(protocol.Field.SECURITY_ID, "GB00BH4HKS39")
        msg.set_field(protocol.Field.SECURITY_ID_SOURCE,
                      protocol.SecurityIDSource.ISIN_NUMBER.value)
        msg.set_field(protocol.Field.ACCOUNT, "TEST")
        msg.set_field(protocol.Field.HANDL_INST,
                      protocol.HandlInst.AUTOMATED_EXECUTION_ORDER_PRIVATE_NO_BROKER_INTERVENTION.value)
        msg.set_field(protocol.Field.EX_DESTINATION, "XLON")
        msg.set_field(protocol.Field.SIDE, str(Side.buy.value))
        msg.set_field(protocol.Field.CL_ORD_ID, str(uuid.uuid1()))
        msg.set_field(protocol.Field.CURRENCY, "GBP")

        await connection_handler.send_msg(msg)
        side = Side(int(msg.get_field(protocol.Field.SIDE)))
        logging.debug("---> [%s] %s: %s %s %s@%s" % (
            msg.get_field(protocol.Field.MSG_TYPE),
            msg.get_field(protocol.Field.CL_ORD_ID),
            msg.get_field(protocol.Field.SYMBOL),
            side.name,
            msg.get_field(protocol.Field.ORDER_QTY),
            msg.get_field(protocol.Field.PRICE)))

    # noinspection PyUnusedLocal
    async def on_login(self, connection_handler: FIXConnectionHandler, msg):
        logging.info("Logged in")
        await self.send_order(connection_handler)

    # noinspection PyMethodMayBeStatic
    async def on_execution_report(self, connection_handler: FIXConnectionHandler, msg: FIXMessageContainer):
        codec = connection_handler.codec
        protocol = codec.protocol
        if msg.has_field(protocol.Field.EXEC_TYPE):
            if msg.get_field(protocol.Field.EXEC_TYPE) == "0":
                side = Side(int(msg.get_field(protocol.Field.SIDE)))
                logging.debug("<--- [%s] %s: %s %s %s@%s" % (
                    msg.get_field(protocol.Field.MSG_TYPE),
                    msg.get_field(protocol.Field.CL_ORD_ID),
                    msg.get_field(protocol.Field.SYMBOL),
                    side.name,
                    msg.get_field(protocol.Field.ORDER_QTY),
                    msg.get_field(protocol.Field.PRICE)))
            elif msg.get_field(protocol.Field.EXEC_TYPE) == "4":
                reason = "Unknown" if msg.has_field(protocol.Field.TEXT) else \
                    msg.get_field(protocol.Field.TEXT)
                logging.info("Order Rejected '%s'" % (reason,))
        else:
            logging.error("Received execution report without ExecType")


def main():
    logging.basicConfig(level=logging.DEBUG)
    loop = asyncio.get_event_loop()
    client = Client()
    loop.run_until_complete(client.start('', 9898, loop))
    loop.run_forever()


if __name__ == '__main__':
    main()
