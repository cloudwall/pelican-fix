import logging
from abc import ABC, abstractmethod
from enum import Enum, auto

from simplefix import FixMessage


class DuplicateSeqNoError(Exception):
    pass


class MessageDirection(Enum):
    INBOUND = auto()
    OUTBOUND = auto()


class FIXMessageContainer(ABC):
    @abstractmethod
    def has_field(self, number: int):
        pass

    @abstractmethod
    def get_field(self, field_id) -> str:
        pass

    @abstractmethod
    def set_field(self, number: int, value: str):
        pass

    @abstractmethod
    def remove_field(self, number: int):
        pass

    @abstractmethod
    def encode(self):
        pass


class FIXSession:
    logger = logging.getLogger(__name__)

    def __init__(self, key, target_comp_id: str, sender_comp_id: str):
        self.key = key
        self.sender_comp_id = sender_comp_id
        self.target_comp_id = target_comp_id

        self.send_seq_num = None
        self.messages = None
        self.next_expected_msg_seq_num = None

        self.reset_msgs()

    def get_sender_comp_id(self):
        return self.sender_comp_id

    def get_target_comp_id(self):
        return self.target_comp_id

    def reset_msgs(self):
        self.send_seq_num = 0
        self.next_expected_msg_seq_num = 1
        self.messages = {
            MessageDirection.OUTBOUND: {},
            MessageDirection.INBOUND: {}
        }

    def validate_comp_ids(self, target_comp_id: str, sender_comp_id: str):
        return self.sender_comp_id == sender_comp_id and self.target_comp_id == target_comp_id

    def allocate_send_seq_no(self):
        self.send_seq_num += 1
        return str(self.send_seq_num)

    def validate_recv_seq_no(self, seq_no: int):
        if self.next_expected_msg_seq_num < seq_no:
            self.logger.warning(f'SeqNum from client unexpected (Rcvd: {seq_no} '
                                f'Expected: {self.next_expected_msg_seq_num})')
            return False, self.next_expected_msg_seq_num
        else:
            return True, seq_no

    def reset_seq_no(self):
        self.send_seq_num = 0
        self.next_expected_msg_seq_num = 1

    def set_recv_seq_no(self, seq_no: int):
        if self.next_expected_msg_seq_num != seq_no:
            self.logger.warning(f'SeqNum from client unexpected (Rcvd: {seq_no} '
                                f'Expected: {self.next_expected_msg_seq_num})')
        self.next_expected_msg_seq_num = int(seq_no) + 1


class JournalProvider(ABC):
    @abstractmethod
    def get_sessions(self):
        pass

    @abstractmethod
    def create_session(self, target_comp_id: str, sender_comp_id: str):
        pass

    @abstractmethod
    def persist_msg(self, msg: FIXMessageContainer, session: FIXSession, direction: MessageDirection):
        pass

    @abstractmethod
    def recover_msgs(self, session: FIXSession, direction: MessageDirection, begin_seq_no: int, end_seq_no: int):
        pass


class SessionManager:
    def __init__(self, journal_provider: JournalProvider):
        self.journal_provider = journal_provider
        self.sessions = {}

        # load all sessions from the journal provider on startup
        for session in self.journal_provider.get_sessions():
            self.sessions[session.key] = session

    def create_session(self, target_comp_id: str, sender_comp_id: str):
        if self.__find_session_by_comp_ids(target_comp_id, sender_comp_id) is None:
            session = self.journal_provider.create_session(target_comp_id, sender_comp_id)
            self.sessions[session.key] = session
        else:
            raise RuntimeError("Failed to add session with duplicate key")
        return session

    def get_session(self, identifier: str):
        return self.sessions.get(identifier, None)

    def get_or_create_session_from_comp_ids(self, target_comp_id: str, sender_comp_id: str):
        session = self.__find_session_by_comp_ids(target_comp_id, sender_comp_id)
        if session is None:
            if self.validate_session(target_comp_id, sender_comp_id):
                session = self.create_session(target_comp_id, sender_comp_id)

        return session

    # noinspection PyMethodMayBeStatic,PyUnusedLocal
    def validate_session(self, target_comp_id: str, sender_comp_id: str) -> bool:
        # this make any session we receive valid
        return True

    def __find_session_by_comp_ids(self, target_comp_id: str, sender_comp_id: str):
        sessions = [x for x in self.sessions.values() if
                    x.target_comp_id == target_comp_id and x.sender_comp_id == sender_comp_id]
        if sessions is not None and len(sessions) != 0:
            return sessions[0]
        return None


class FIXEngine:
    def __init__(self, journal_provider: JournalProvider):
        self.session_manager = SessionManager(journal_provider)
        self.journal_provider = journal_provider

    # noinspection PyMethodMayBeStatic,PyUnusedLocal
    def should_resend_message(self, session: FIXSession, msg: FixMessage) -> bool:
        # we should resend all application messages
        return True
