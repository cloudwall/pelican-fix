import sqlite3
import pickle

from pelicanfix.engine import JournalProvider, FIXSession, MessageDirection, DuplicateSeqNoError


# noinspection SqlDialectInspection,SqlNoDataSourceInspection
class SqliteJournalProvider(JournalProvider):
    def __init__(self, filename=None):
        if filename is None:
            self.conn = sqlite3.connect(":memory:")
        else:
            self.conn = sqlite3.connect(filename)

        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS message("
                            "seqNo INTEGER NOT NULL,"
                            "session TEXT NOT NULL,"
                            "direction INTEGER NOT NULL,"
                            "msg TEXT,"
                            "PRIMARY KEY (seqNo, session, direction))")

        self.cursor.execute("CREATE TABLE IF NOT EXISTS session("
                            "sessionId INTEGER PRIMARY KEY AUTOINCREMENT,"
                            "targetCompId TEXT NOT NULL,"
                            "senderCompId TEXT NOT NULL,"
                            "outboundSeqNo INTEGER DEFAULT 0,"
                            "inboundSeqNo INTEGER DEFAULT 0,"
                            "UNIQUE (targetCompId, senderCompId))")

    def get_sessions(self):
        sessions = []
        self.cursor.execute("SELECT sessionId, targetCompId, senderCompId, outboundSeqNo, inboundSeqNo FROM session")
        for sessionInfo in self.cursor:
            session = FIXSession(sessionInfo[0], sessionInfo[1], sessionInfo[2])
            session.send_seq_num = sessionInfo[3]
            session.next_expected_msg_seq_num = sessionInfo[4] + 1
            sessions.append(session)

        return sessions

    def create_session(self, target_comp_id, send_comp_id):
        try:
            self.cursor.execute("INSERT INTO session(targetCompId, senderCompId) VALUES(?, ?)",
                                (target_comp_id, send_comp_id))
            session_id = self.cursor.lastrowid
            self.conn.commit()
            return FIXSession(session_id, target_comp_id, send_comp_id)
        except sqlite3.IntegrityError:
            raise RuntimeError(
                "Session already exists for TargetCompId: %s SenderCompId: %s" % (target_comp_id, send_comp_id))

    def persist_msg(self, msg, session, direction):
        msg_str = pickle.dumps(msg)
        seq_no = msg.get_field(34)
        try:
            self.cursor.execute("INSERT INTO message VALUES(?, ?, ?, ?)",
                                (seq_no, session.key, direction.value, msg_str))
            if direction == MessageDirection.OUTBOUND:
                self.cursor.execute("UPDATE session SET outboundSeqNo=?", (seq_no,))
            elif direction == MessageDirection.INBOUND:
                self.cursor.execute("UPDATE session SET inboundSeqNo=?", (seq_no,))

            self.conn.commit()
        except sqlite3.IntegrityError:
            raise DuplicateSeqNoError("%s is a duplicate" % (seq_no,))

    def recover_msg(self, session, direction, seq_no):
        try:
            msgs = self.recover_msgs(session, direction, seq_no, seq_no)
            return msgs[0]
        except IndexError:
            return None

    def recover_msgs(self, session, direction, start_seq_no, end_seq_no):
        self.cursor.execute(
            "SELECT msg FROM message WHERE session = ? AND direction = ? AND seqNo >= ? AND seqNo <= ? ORDER BY seqNo",
            (session.key, direction.value, start_seq_no, end_seq_no))
        msgs = []
        for msg in self.cursor:
            msgs.append(pickle.loads(msg[0]))
        return msgs

    def get_all_msgs(self, sessions=None, direction=None):
        if sessions is None:
            sessions = []
        sql = "SELECT seqNo, msg, direction, session FROM message"
        clauses = []
        args = []
        if sessions is not None and len(sessions) != 0:
            clauses.append("session in (" + ','.join('?' * len(sessions)) + ")")
            args.extend(sessions)
        if direction is not None:
            clauses.append("direction = ?")
            args.append(direction.value)

        if clauses:
            sql = sql + " WHERE " + " AND ".join(clauses)

        sql = sql + " ORDER BY rowid"

        self.cursor.execute(sql, tuple(args))
        msgs = []
        for msg in self.cursor:
            msgs.append((msg[0], pickle.loads(msg[1]), msg[2], msg[3]))

        return msgs
