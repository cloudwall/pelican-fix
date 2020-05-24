import random
import uuid

import simplefix

from pelicanfix.protocol.fix44 import Field, MsgType, Side, HandlInst, SecurityIDSource


def main():
    msg = simplefix.FixMessage()
    msg.append_pair(Field.BEGIN_STRING.value.get_number(), 'FIX.4.2')
    msg.append_pair(Field.MSG_TYPE.value.get_number(), MsgType.ORDER_SINGLE.value)
    msg.append_pair(Field.PRICE.value.get_number(), "%0.2f" % (random.random() * 2 + 10))
    msg.append_pair(Field.ORDER_QTY.value.get_number(), int(random.random() * 100))
    msg.append_pair(Field.SYMBOL.value.get_number(), "VOD.L")
    msg.append_pair(Field.SECURITY_ID.value.get_number(), "GB00BH4HKS39")
    msg.append_pair(Field.SECURITY_ID_SOURCE.value.get_number(), SecurityIDSource.ISIN_NUMBER.value)
    msg.append_pair(Field.ACCOUNT.value.get_number(), "TEST")
    msg.append_pair(Field.HANDL_INST.value.get_number(),
                    HandlInst.AUTOMATED_EXECUTION_ORDER_PRIVATE_NO_BROKER_INTERVENTION.value)
    msg.append_pair(Field.EX_DESTINATION.value.get_number(), "XLON")
    msg.append_pair(Field.SIDE.value.get_number(), Side.BUY.value)
    msg.append_pair(Field.CL_ORD_ID.value.get_number(), str(uuid.uuid1()))
    msg.append_pair(Field.CURRENCY.value.get_number(), "GBP")

    print(str(msg.encode()).replace('\\x01', '|'))


if __name__ == '__main__':
    main()
