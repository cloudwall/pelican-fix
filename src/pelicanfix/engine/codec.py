import importlib
from abc import ABC, abstractmethod
from datetime import datetime
from typing import List

import simplefix

from pelicanfix.engine import FIXSession, FIXMessageContainer


class EncodingError(Exception):
    pass


class DecodingError(Exception):
    pass


class Codec(ABC):
    def __init__(self, protocol):
        self.protocol = importlib.import_module(protocol)

    @staticmethod
    def current_datetime():
        return datetime.utcnow().strftime("%Y%m%d-%H:%M:%S.%f")[:-3]

    @abstractmethod
    def create_message(self) -> FIXMessageContainer:
        pass

    @abstractmethod
    def create_logon_msg(self) -> FIXMessageContainer:
        pass

    @abstractmethod
    def create_heartbeat_msg(self) -> FIXMessageContainer:
        pass

    def create_resend_request(self, begin_seq_no: int, end_seq_no: int) -> FIXMessageContainer:
        pass

    @abstractmethod
    def get_session_msg_types(self) -> List[str]:
        pass

    def encode(self, msg: FIXMessageContainer, session: FIXSession):
        msg_type = msg.get_field(self.protocol.Field.MSG_TYPE.value.get_number())
        msg.set_field(self.protocol.Field.SENDER_COMP_ID.value.get_number(), session.get_sender_comp_id())
        msg.set_field(self.protocol.Field.TARGET_COMP_ID.value.get_number(), session.get_target_comp_id())

        if msg_type == self.protocol.MsgType.SEQUENCE_RESET:
            if msg.has_field(self.protocol.Field.GAP_FILL_FLAG.value.get_number()) \
                    and msg.get_field(self.protocol.Field.GAP_FILL_FLAG.value.get_number()) == "Y":
                # in this case the sequence number should already be on the message
                try:
                    seq_no = msg.get_field(self.protocol.Field.MSG_SEQ_NUM.value.get_number())
                except KeyError:
                    raise EncodingError("SequenceReset with GapFill='Y' must have the MsgSeqNum already populated")
            else:
                msg.set_field(self.protocol.Field.NEW_SEQ_NO.value.get_number(), str(session.allocate_send_seq_no()))
                seq_no = msg.get_field(self.protocol.Field.MSG_SEQ_NUM.value.get_number())
        else:
            # if we have the PossDupFlag set, we need to send the message with the same seq_no
            if msg.has_field(self.protocol.Field.POSS_DUP_FLAG.value.get_number()) \
                    and msg.get_field(self.protocol.Field.POSS_DUP_FLAG.value.get_number()) == "Y":
                try:
                    seq_no = msg.get_field(self.protocol.Field.MSG_SEQ_NUM.value.get_number())
                except KeyError:
                    raise EncodingError("Failed to encode message with PossDupFlay=Y but no previous MsgSeqNum")
            else:
                seq_no = session.allocate_send_seq_no()

        msg.set_field(self.protocol.Field.MSG_SEQ_NUM.value.get_number(), seq_no)
        msg.set_field(self.protocol.Field.SENDING_TIME.value.get_number(), self.current_datetime())

        return msg.encode()

    @abstractmethod
    def decode(self, raw_msg):
        pass


class SimpleFixMessageContainer(FIXMessageContainer):
    def __init__(self, message: simplefix.FixMessage = None):
        if message is None:
            message = simplefix.FixMessage()
        self.message = message

    def has_field(self, number: int):
        return number in self.message

    def get_field(self, number: int) -> str:
        return self.message.get(number).decode('utf-8')

    def set_field(self, number: int, value: str):
        return self.message.append_pair(number, value)

    def remove_field(self, number: int):
        return self.message.remove(number)

    def encode(self):
        return self.message.encode()


class SimpleFixCodec(Codec):
    def __init__(self, protocol):
        super().__init__(protocol)

    def create_message(self) -> FIXMessageContainer:
        msg = SimpleFixMessageContainer()
        msg.set_field(self.protocol.Field.BEGIN_STRING.value.get_number(), self.protocol.BEGIN_STRING)
        return msg

    def create_logon_msg(self) -> FIXMessageContainer:
        msg = self.create_message()
        msg.set_field(self.protocol.Field.MSG_TYPE.value.get_number(), self.protocol.MsgType.LOGON.value)
        msg.set_field(self.protocol.Field.ENCRYPT_METHOD.value.get_number(), '0')
        msg.set_field(self.protocol.Field.HEART_BT_INT.value.get_number(), '30')
        return msg

    def create_heartbeat_msg(self) -> FIXMessageContainer:
        msg = self.create_message()
        msg.set_field(self.protocol.Field.MSG_TYPE.value.get_number(), self.protocol.MsgType.HEARTBEAT.value)
        return msg

    def get_session_msg_types(self) -> List[str]:
        return [
            self.protocol.MsgType.LOGON.value,
            self.protocol.MsgType.HEARTBEAT.value,
            self.protocol.MsgType.TEST_REQUEST.value,
        ]

    def decode(self, raw_msg):
        parser = simplefix.FixParser()
        parser.append_buffer(raw_msg)
        msg = parser.get_message()
        if msg is not None:
            return SimpleFixMessageContainer(msg), len(raw_msg)
        else:
            return None, len(raw_msg)
