from enum import Enum

from pelicanfix.protocol import FIXField


BEGIN_STRING = 'FIX.4.1'


class Field(Enum):
    ACCOUNT = FIXField('Account', 1)
    ACCRUED_INTEREST_AMT = FIXField('AccruedInterestAmt', 159)
    ACCRUED_INTEREST_RATE = FIXField('AccruedInterestRate', 158)
    ADV_ID = FIXField('AdvId', 2)
    ADV_REF_ID = FIXField('AdvRefID', 3)
    ADV_SIDE = FIXField('AdvSide', 4)
    ADV_TRANS_TYPE = FIXField('AdvTransType', 5)
    ALLOC_ACCOUNT = FIXField('AllocAccount', 79)
    ALLOC_AVG_PX = FIXField('AllocAvgPx', 153)
    ALLOC_HANDL_INST = FIXField('AllocHandlInst', 209)
    ALLOC_ID = FIXField('AllocID', 70)
    ALLOC_LINK_ID = FIXField('AllocLinkID', 196)
    ALLOC_LINK_TYPE = FIXField('AllocLinkType', 197)
    ALLOC_NET_MONEY = FIXField('AllocNetMoney', 154)
    ALLOC_REJ_CODE = FIXField('AllocRejCode', 88)
    ALLOC_SHARES = FIXField('AllocShares', 80)
    ALLOC_STATUS = FIXField('AllocStatus', 87)
    ALLOC_TEXT = FIXField('AllocText', 161)
    ALLOC_TRANS_TYPE = FIXField('AllocTransType', 71)
    AVG_PRX_PRECISION = FIXField('AvgPrxPrecision', 74)
    AVG_PX = FIXField('AvgPx', 6)
    BEGIN_SEQ_NO = FIXField('BeginSeqNo', 7)
    BEGIN_STRING = FIXField('BeginString', 8)
    BID_FORWARD_POINTS = FIXField('BidForwardPoints', 189)
    BID_PX = FIXField('BidPx', 132)
    BID_SIZE = FIXField('BidSize', 134)
    BID_SPOT_RATE = FIXField('BidSpotRate', 188)
    BODY_LENGTH = FIXField('BodyLength', 9)
    BROKER_OF_CREDIT = FIXField('BrokerOfCredit', 92)
    CASH_ORDER_QTY = FIXField('CashOrderQty', 152)
    CASH_SETTL_AGENT_ACCT_NAME = FIXField('CashSettlAgentAcctName', 185)
    CASH_SETTL_AGENT_ACCT_NUM = FIXField('CashSettlAgentAcctNum', 184)
    CASH_SETTL_AGENT_CODE = FIXField('CashSettlAgentCode', 183)
    CASH_SETTL_AGENT_CONTACT_NAME = FIXField('CashSettlAgentContactName', 186)
    CASH_SETTL_AGENT_CONTACT_PHONE = FIXField('CashSettlAgentContactPhone', 187)
    CASH_SETTL_AGENT_NAME = FIXField('CashSettlAgentName', 182)
    CHECK_SUM = FIXField('CheckSum', 10)
    CL_ORD_ID = FIXField('ClOrdID', 11)
    CLIENT_ID = FIXField('ClientID', 109)
    COMM_TYPE = FIXField('CommType', 13)
    COMMISSION = FIXField('Commission', 12)
    COVERED_OR_UNCOVERED = FIXField('CoveredOrUncovered', 203)
    CUM_QTY = FIXField('CumQty', 14)
    CURRENCY = FIXField('Currency', 15)
    CUSTOMER_OR_FIRM = FIXField('CustomerOrFirm', 204)
    CXL_QTY = FIXField('CxlQty', 84)
    CXL_REJ_REASON = FIXField('CxlRejReason', 102)
    DK_REASON = FIXField('DKReason', 127)
    DELIVER_TO_COMP_ID = FIXField('DeliverToCompID', 128)
    DELIVER_TO_LOCATION_ID = FIXField('DeliverToLocationID', 145)
    DELIVER_TO_SUB_ID = FIXField('DeliverToSubID', 129)
    EFFECTIVE_TIME = FIXField('EffectiveTime', 168)
    EMAIL_THREAD_ID = FIXField('EmailThreadID', 164)
    EMAIL_TYPE = FIXField('EmailType', 94)
    ENCRYPT_METHOD = FIXField('EncryptMethod', 98)
    END_SEQ_NO = FIXField('EndSeqNo', 16)
    EX_DESTINATION = FIXField('ExDestination', 100)
    EXEC_BROKER = FIXField('ExecBroker', 76)
    EXEC_ID = FIXField('ExecID', 17)
    EXEC_INST = FIXField('ExecInst', 18)
    EXEC_REF_ID = FIXField('ExecRefID', 19)
    EXEC_TRANS_TYPE = FIXField('ExecTransType', 20)
    EXEC_TYPE = FIXField('ExecType', 150)
    EXPIRE_TIME = FIXField('ExpireTime', 126)
    FOREX_REQ = FIXField('ForexReq', 121)
    FUT_SETT_DATE = FIXField('FutSettDate', 64)
    FUT_SETT_DATE2 = FIXField('FutSettDate2', 193)
    GAP_FILL_FLAG = FIXField('GapFillFlag', 123)
    HANDL_INST = FIXField('HandlInst', 21)
    HEADLINE = FIXField('Headline', 148)
    HEART_BT_INT = FIXField('HeartBtInt', 108)
    ID_SOURCE = FIXField('IDSource', 22)
    IOI_NATURAL_FLAG = FIXField('IOINaturalFlag', 130)
    IOI_OTH_SVC = FIXField('IOIOthSvc', 24)
    IOI_QLTY_IND = FIXField('IOIQltyInd', 25)
    IOI_QUALIFIER = FIXField('IOIQualifier', 104)
    IOI_REF_ID = FIXField('IOIRefID', 26)
    IOI_SHARES = FIXField('IOIShares', 27)
    IOI_TRANS_TYPE = FIXField('IOITransType', 28)
    IO_IID = FIXField('IOIid', 23)
    ISSUER = FIXField('Issuer', 106)
    LAST_CAPACITY = FIXField('LastCapacity', 29)
    LAST_FORWARD_POINTS = FIXField('LastForwardPoints', 195)
    LAST_MKT = FIXField('LastMkt', 30)
    LAST_PX = FIXField('LastPx', 31)
    LAST_SHARES = FIXField('LastShares', 32)
    LAST_SPOT_RATE = FIXField('LastSpotRate', 194)
    LEAVES_QTY = FIXField('LeavesQty', 151)
    LINES_OF_TEXT = FIXField('LinesOfText', 33)
    LIST_EXEC_INST = FIXField('ListExecInst', 69)
    LIST_ID = FIXField('ListID', 66)
    LIST_NO_ORDS = FIXField('ListNoOrds', 68)
    LIST_SEQ_NO = FIXField('ListSeqNo', 67)
    LOCATE_REQD = FIXField('LocateReqd', 114)
    MATURITY_DAY = FIXField('MaturityDay', 205)
    MATURITY_MONTH_YEAR = FIXField('MaturityMonthYear', 200)
    MAX_FLOOR = FIXField('MaxFloor', 111)
    MAX_SHOW = FIXField('MaxShow', 210)
    MIN_QTY = FIXField('MinQty', 110)
    MISC_FEE_AMT = FIXField('MiscFeeAmt', 137)
    MISC_FEE_CURR = FIXField('MiscFeeCurr', 138)
    MISC_FEE_TYPE = FIXField('MiscFeeType', 139)
    MSG_SEQ_NUM = FIXField('MsgSeqNum', 34)
    MSG_TYPE = FIXField('MsgType', 35)
    NET_MONEY = FIXField('NetMoney', 118)
    NEW_SEQ_NO = FIXField('NewSeqNo', 36)
    NO_ALLOCS = FIXField('NoAllocs', 78)
    NO_EXECS = FIXField('NoExecs', 124)
    NO_IOI_QUALIFIERS = FIXField('NoIOIQualifiers', 199)
    NO_MISC_FEES = FIXField('NoMiscFees', 136)
    NO_ORDERS = FIXField('NoOrders', 73)
    NO_RELATED_SYM = FIXField('NoRelatedSym', 146)
    NO_RPTS = FIXField('NoRpts', 82)
    NOTIFY_BROKER_OF_CREDIT = FIXField('NotifyBrokerOfCredit', 208)
    NUM_DAYS_INTEREST = FIXField('NumDaysInterest', 157)
    OFFER_FORWARD_POINTS = FIXField('OfferForwardPoints', 191)
    OFFER_PX = FIXField('OfferPx', 133)
    OFFER_SIZE = FIXField('OfferSize', 135)
    OFFER_SPOT_RATE = FIXField('OfferSpotRate', 190)
    ON_BEHALF_OF_COMP_ID = FIXField('OnBehalfOfCompID', 115)
    ON_BEHALF_OF_LOCATION_ID = FIXField('OnBehalfOfLocationID', 144)
    ON_BEHALF_OF_SUB_ID = FIXField('OnBehalfOfSubID', 116)
    OPEN_CLOSE = FIXField('OpenClose', 77)
    OPT_ATTRIBUTE = FIXField('OptAttribute', 206)
    ORD_REJ_REASON = FIXField('OrdRejReason', 103)
    ORD_STATUS = FIXField('OrdStatus', 39)
    ORD_TYPE = FIXField('OrdType', 40)
    ORDER_ID = FIXField('OrderID', 37)
    ORDER_QTY = FIXField('OrderQty', 38)
    ORDER_QTY2 = FIXField('OrderQty2', 192)
    ORIG_CL_ORD_ID = FIXField('OrigClOrdID', 41)
    ORIG_SENDING_TIME = FIXField('OrigSendingTime', 122)
    ORIG_TIME = FIXField('OrigTime', 42)
    PEG_DIFFERENCE = FIXField('PegDifference', 211)
    POSS_DUP_FLAG = FIXField('PossDupFlag', 43)
    POSS_RESEND = FIXField('PossResend', 97)
    PREV_CLOSE_PX = FIXField('PrevClosePx', 140)
    PRICE = FIXField('Price', 44)
    PROCESS_CODE = FIXField('ProcessCode', 81)
    PUT_OR_CALL = FIXField('PutOrCall', 201)
    QUOTE_ID = FIXField('QuoteID', 117)
    QUOTE_REQ_ID = FIXField('QuoteReqID', 131)
    RAW_DATA = FIXField('RawData', 96)
    RAW_DATA_LENGTH = FIXField('RawDataLength', 95)
    REF_ALLOC_ID = FIXField('RefAllocID', 72)
    REF_SEQ_NUM = FIXField('RefSeqNum', 45)
    RELATD_SYM = FIXField('RelatdSym', 46)
    REPORT_TO_EXCH = FIXField('ReportToExch', 113)
    RESET_SEQ_NUM_FLAG = FIXField('ResetSeqNumFlag', 141)
    RPT_SEQ = FIXField('RptSeq', 83)
    RULE80_A = FIXField('Rule80A', 47)
    SECONDARY_ORDER_ID = FIXField('SecondaryOrderID', 198)
    SECURE_DATA = FIXField('SecureData', 91)
    SECURE_DATA_LEN = FIXField('SecureDataLen', 90)
    SECURITY_DESC = FIXField('SecurityDesc', 107)
    SECURITY_EXCHANGE = FIXField('SecurityExchange', 207)
    SECURITY_ID = FIXField('SecurityID', 48)
    SECURITY_SETTL_AGENT_ACCT_NAME = FIXField('SecuritySettlAgentAcctName', 179)
    SECURITY_SETTL_AGENT_ACCT_NUM = FIXField('SecuritySettlAgentAcctNum', 178)
    SECURITY_SETTL_AGENT_CODE = FIXField('SecuritySettlAgentCode', 177)
    SECURITY_SETTL_AGENT_CONTACT_NAME = FIXField('SecuritySettlAgentContactName', 180)
    SECURITY_SETTL_AGENT_CONTACT_PHONE = FIXField('SecuritySettlAgentContactPhone', 181)
    SECURITY_SETTL_AGENT_NAME = FIXField('SecuritySettlAgentName', 176)
    SECURITY_TYPE = FIXField('SecurityType', 167)
    SENDER_COMP_ID = FIXField('SenderCompID', 49)
    SENDER_LOCATION_ID = FIXField('SenderLocationID', 142)
    SENDER_SUB_ID = FIXField('SenderSubID', 50)
    SENDING_TIME = FIXField('SendingTime', 52)
    SETTL_BRKR_CODE = FIXField('SettlBrkrCode', 174)
    SETTL_CURR_AMT = FIXField('SettlCurrAmt', 119)
    SETTL_CURR_FX_RATE = FIXField('SettlCurrFxRate', 155)
    SETTL_CURR_FX_RATE_CALC = FIXField('SettlCurrFxRateCalc', 156)
    SETTL_CURRENCY = FIXField('SettlCurrency', 120)
    SETTL_DELIVERY_TYPE = FIXField('SettlDeliveryType', 172)
    SETTL_DEPOSITORY_CODE = FIXField('SettlDepositoryCode', 173)
    SETTL_INST_CODE = FIXField('SettlInstCode', 175)
    SETTL_INST_ID = FIXField('SettlInstID', 162)
    SETTL_INST_MODE = FIXField('SettlInstMode', 160)
    SETTL_INST_SOURCE = FIXField('SettlInstSource', 165)
    SETTL_INST_TRANS_TYPE = FIXField('SettlInstTransType', 163)
    SETTL_LOCATION = FIXField('SettlLocation', 166)
    SETTLMNT_TYP = FIXField('SettlmntTyp', 63)
    SHARES = FIXField('Shares', 53)
    SIDE = FIXField('Side', 54)
    SIGNATURE = FIXField('Signature', 89)
    SIGNATURE_LENGTH = FIXField('SignatureLength', 93)
    STAND_INST_DB_ID = FIXField('StandInstDbID', 171)
    STAND_INST_DB_NAME = FIXField('StandInstDbName', 170)
    STAND_INST_DB_TYPE = FIXField('StandInstDbType', 169)
    STOP_PX = FIXField('StopPx', 99)
    STRIKE_PRICE = FIXField('StrikePrice', 202)
    SUBJECT = FIXField('Subject', 147)
    SYMBOL = FIXField('Symbol', 55)
    SYMBOL_SFX = FIXField('SymbolSfx', 65)
    TARGET_COMP_ID = FIXField('TargetCompID', 56)
    TARGET_LOCATION_ID = FIXField('TargetLocationID', 143)
    TARGET_SUB_ID = FIXField('TargetSubID', 57)
    TEST_REQ_ID = FIXField('TestReqID', 112)
    TEXT = FIXField('Text', 58)
    TIME_IN_FORCE = FIXField('TimeInForce', 59)
    TRADE_DATE = FIXField('TradeDate', 75)
    TRANSACT_TIME = FIXField('TransactTime', 60)
    URL_LINK = FIXField('URLLink', 149)
    URGENCY = FIXField('Urgency', 61)
    VALID_UNTIL_TIME = FIXField('ValidUntilTime', 62)
    WAVE_NO = FIXField('WaveNo', 105)


class AdvSide(Enum):
    BUY = 'B'
    SELL = 'S'
    TRADE = 'T'
    CROSS = 'X'


class AdvTransType(Enum):
    CANCEL = 'C'
    NEW = 'N'
    REPLACE = 'R'


class AllocHandlInst(Enum):
    MATCH = '1'
    FORWARD = '2'
    FORWARD_AND_MATCH = '3'


class AllocLinkType(Enum):
    F_X_NETTING = '0'
    F_X_SWAP = '1'


class AllocRejCode(Enum):
    UNKNOWN_ACCOUNT = '0'
    INCORRECT_QUANTITY = '1'
    INCORRECT_AVERAGE_PRICE = '2'
    UNKNOWN_EXECUTING_BROKER_MNEMONIC = '3'
    COMMISSION_DIFFERENCE = '4'
    UNKNOWN_ORDERID = '5'
    UNKNOWN_LISTID = '6'
    OTHER = '7'


class AllocStatus(Enum):
    ACCEPTED = '0'
    REJECTED = '1'
    PARTIAL_ACCEPT = '2'
    RECEIVED = '3'


class AllocTransType(Enum):
    NEW = '0'
    REPLACE = '1'
    CANCEL = '2'
    PRELIMINARY = '3'
    CALCULATED = '4'


class CommType(Enum):
    PER_SHARE = '1'
    PERCENTAGE = '2'
    ABSOLUTE = '3'


class CoveredOrUncovered(Enum):
    COVERED = '0'
    UNCOVERED = '1'


class CustomerOrFirm(Enum):
    CUSTOMER = '0'
    FIRM = '1'


class CxlRejReason(Enum):
    TOO_LATE_TO_CANCEL = '0'
    UNKNOWN_ORDER = '1'


class DKReason(Enum):
    UNKNOWN_SYMBOL = 'A'
    WRONG_SIDE = 'B'
    QUANTITY_EXCEEDS_ORDER = 'C'
    NO_MATCHING_ORDER = 'D'
    PRICE_EXCEEDS_LIMIT = 'E'
    OTHER = 'Z'


class EmailType(Enum):
    NEW = '0'
    REPLY = '1'
    ADMIN_REPLY = '2'


class EncryptMethod(Enum):
    NONE = '0'
    PKCS = '1'
    DES = '2'
    PKCS_DES = '3'
    PGP_DES = '4'
    PGP_DES_MD5 = '5'
    PEM_DES_MD5 = '6'


class ExecInst(Enum):
    STAY_ON_OFFERSIDE = '0'
    NOT_HELD = '1'
    WORK = '2'
    GO_ALONG = '3'
    OVER_THE_DAY = '4'
    HELD = '5'
    PARTICIPATE_DONT_INITIATE = '6'
    STRICT_SCALE = '7'
    TRY_TO_SCALE = '8'
    STAY_ON_BIDSIDE = '9'
    NO_CROSS = 'A'
    OK_TO_CROSS = 'B'
    CALL_FIRST = 'C'
    PERCENT_OF_VOLUME = 'D'
    DO_NOT_INCREASE = 'E'
    DO_NOT_REDUCE = 'F'
    ALL_OR_NONE = 'G'
    INSTITUTIONS_ONLY = 'I'
    LAST_PEG = 'L'
    MID_PRICE_PEG = 'M'
    NON_NEGOTIABLE = 'N'
    OPENING_PEG = 'O'
    MARKET_PEG = 'P'
    PRIMARY_PEG = 'R'
    SUSPEND = 'S'
    CUSTOMER_DISPLAY_INSTRUCTION = 'U'
    NETTING = 'V'


class ExecTransType(Enum):
    NEW = '0'
    CANCEL = '1'
    CORRECT = '2'
    STATUS = '3'


class ExecType(Enum):
    NEW = '0'
    PARTIAL_FILL = '1'
    FILL = '2'
    DONE_FOR_DAY = '3'
    CANCELLED = '4'
    REPLACE = '5'
    PENDING_CANCEL_REPLACE = '6'
    STOPPED = '7'
    REJECTED = '8'
    SUSPENDED = '9'
    PENDING_NEW = 'A'
    CALCULATED = 'B'
    EXPIRED = 'C'


class ForexReq(Enum):
    NO = 'N'
    YES = 'Y'


class GapFillFlag(Enum):
    NO = 'N'
    YES = 'Y'


class HandlInst(Enum):
    AUTOMATED_EXECUTION_ORDER_PRIVATE_NO_BROKER_INTERVENTION = '1'
    AUTOMATED_EXECUTION_ORDER_PUBLIC_BROKER_INTERVENTION_OK = '2'
    MANUAL_ORDER_BEST_EXECUTION = '3'


class IDSource(Enum):
    CUSIP = '1'
    SEDOL = '2'
    QUIK = '3'
    ISIN_NUMBER = '4'
    RIC_CODE = '5'
    ISO_CURRENCY_CODE = '6'
    ISO_COUNTRY_CODE = '7'


class IOINaturalFlag(Enum):
    NO = 'N'
    YES = 'Y'


class IOIOthSvc(Enum):
    AUTEX = 'A'
    BRIDGE = 'B'


class IOIQltyInd(Enum):
    HIGH = 'H'
    LOW = 'L'
    MEDIUM = 'M'


class IOIQualifier(Enum):
    ALL_OR_NONE = 'A'
    AT_THE_CLOSE = 'C'
    IN_TOUCH_WITH = 'I'
    LIMIT = 'L'
    MORE_BEHIND = 'M'
    AT_THE_OPEN = 'O'
    TAKING_A_POSITION = 'P'
    AT_THE_MARKET = 'Q'
    PORTFOLIO_SHOW_N = 'S'
    THROUGH_THE_DAY = 'T'
    VERSUS = 'V'
    INDICATION = 'W'
    CROSSING_OPPORTUNITY = 'X'
    AT_THE_MIDPOINT = 'Y'
    PRE_OPEN = 'Z'


class IOIShares(Enum):
    LARGE = 'L'
    MEDIUM = 'M'
    SMALL = 'S'


class IOITransType(Enum):
    CANCEL = 'C'
    NEW = 'N'
    REPLACE = 'R'


class LastCapacity(Enum):
    AGENT = '1'
    CROSS_AS_AGENT = '2'
    CROSS_AS_PRINCIPAL = '3'
    PRINCIPAL = '4'


class LocateReqd(Enum):
    NO = 'N'
    YES = 'Y'


class MiscFeeType(Enum):
    REGULATORY = '1'
    TAX = '2'
    LOCAL_COMMISSION = '3'
    EXCHANGE_FEES = '4'
    STAMP = '5'
    LEVY = '6'
    OTHER = '7'
    MARKUP = '8'


class MsgType(Enum):
    HEARTBEAT = '0'
    TEST_REQUEST = '1'
    RESEND_REQUEST = '2'
    REJECT = '3'
    SEQUENCE_RESET = '4'
    LOGOUT = '5'
    INDICATION_OF_INTEREST = '6'
    ADVERTISEMENT = '7'
    EXECUTION_REPORT = '8'
    ORDER_CANCEL_REJECT = '9'
    LOGON = 'A'
    NEWS = 'B'
    EMAIL = 'C'
    ORDER_D = 'D'
    ORDER_E = 'E'
    ORDER_CANCEL_REQUEST = 'F'
    ORDER_CANCEL_REPLACE_REQUEST = 'G'
    ORDER_STATUS_REQUEST = 'H'
    ALLOCATION = 'J'
    LIST_CANCEL_REQUEST = 'K'
    LIST_EXECUTE = 'L'
    LIST_STATUS_REQUEST = 'M'
    LIST_STATUS = 'N'
    ALLOCATION_ACK = 'P'
    DONT_KNOW_TRADE = 'Q'
    QUOTE_REQUEST = 'R'
    QUOTE = 'S'
    SETTLEMENT_INSTRUCTIONS = 'T'


class NotifyBrokerOfCredit(Enum):
    NO = 'N'
    YES = 'Y'


class OpenClose(Enum):
    CLOSE = 'C'
    OPEN = 'O'


class OrdRejReason(Enum):
    BROKER_OPTION = '0'
    UNKNOWN_SYMBOL = '1'
    EXCHANGE_CLOSED = '2'
    ORDER_EXCEEDS_LIMIT = '3'
    TOO_LATE_TO_ENTER = '4'
    UNKNOWN_ORDER = '5'
    DUPLICATE_ORDER = '6'


class OrdStatus(Enum):
    NEW = '0'
    PARTIALLY_FILLED = '1'
    FILLED = '2'
    DONE_FOR_DAY = '3'
    CANCELED = '4'
    REPLACED = '5'
    PENDING_CANCEL_REPLACE = '6'
    STOPPED = '7'
    REJECTED = '8'
    SUSPENDED = '9'
    PENDING_NEW = 'A'
    CALCULATED = 'B'
    EXPIRED = 'C'


class OrdType(Enum):
    MARKET = '1'
    LIMIT = '2'
    STOP = '3'
    STOP_LIMIT = '4'
    MARKET_ON_CLOSE = '5'
    WITH_OR_WITHOUT = '6'
    LIMIT_OR_BETTER = '7'
    LIMIT_WITH_OR_WITHOUT = '8'
    ON_BASIS = '9'
    ON_CLOSE = 'A'
    LIMIT_ON_CLOSE = 'B'
    FOREX_C = 'C'
    PREVIOUSLY_QUOTED = 'D'
    PREVIOUSLY_INDICATED = 'E'
    FOREX_F = 'F'
    FOREX_G = 'G'
    FOREX_H = 'H'
    PEGGED = 'P'


class PossDupFlag(Enum):
    NO = 'N'
    YES = 'Y'


class PossResend(Enum):
    NO = 'N'
    YES = 'Y'


class ProcessCode(Enum):
    REGULAR = '0'
    SOFT_DOLLAR = '1'
    STEP_IN = '2'
    STEP_OUT = '3'
    SOFT_DOLLAR_STEP_IN = '4'
    SOFT_DOLLAR_STEP_OUT = '5'
    PLAN_SPONSOR = '6'


class PutOrCall(Enum):
    PUT = '0'
    CALL = '1'


class ReportToExch(Enum):
    NO = 'N'
    YES = 'Y'


class ResetSeqNumFlag(Enum):
    NO = 'N'
    YES = 'Y'


class Rule80A(Enum):
    AGENCY_SINGLE_ORDER = 'A'
    SHORT_EXEMPT_TRANSACTION_B = 'B'
    PROGRAM_ORDER_NON_INDEX_ARB_FOR_MEMBER_FIRM_ORG = 'C'
    PROGRAM_ORDER_INDEX_ARB_FOR_MEMBER_FIRM_ORG = 'D'
    REGISTERED_EQUITY_MARKET_MAKER_TRADES = 'E'
    SHORT_EXEMPT_TRANSACTION_F = 'F'
    SHORT_EXEMPT_TRANSACTION_H = 'H'
    INDIVIDUAL_INVESTOR_SINGLE_ORDER = 'I'
    PROGRAM_ORDER_INDEX_ARB_FOR_INDIVIDUAL_CUSTOMER = 'J'
    PROGRAM_ORDER_NON_INDEX_ARB_FOR_INDIVIDUAL_CUSTOMER = 'K'
    SHORT_EXEMPT_TRANSACTION_FOR_MEMBER_COMPETING_MARKET_MAKER_AFFILIATED_WITH_THE_FIRM_CLEARING_THE_TRADE = 'L'
    PROGRAM_ORDER_INDEX_ARB_FOR_OTHER_MEMBER = 'M'
    PROGRAM_ORDER_NON_INDEX_ARB_FOR_OTHER_MEMBER = 'N'
    COMPETING_DEALER_TRADES_O = 'O'
    PRINCIPAL = 'P'
    COMPETING_DEALER_TRADES_R = 'R'
    SPECIALIST_TRADES = 'S'
    COMPETING_DEALER_TRADES_T = 'T'
    PROGRAM_ORDER_INDEX_ARB_FOR_OTHER_AGENCY = 'U'
    ALL_OTHER_ORDERS_AS_AGENT_FOR_OTHER_MEMBER = 'W'
    SHORT_EXEMPT_TRANSACTION_FOR_MEMBER_COMPETING_MARKET_MAKER_NOT_AFFILIATED_WITH_THE_FIRM_CLEARING_THE_TRADE = 'X'
    PROGRAM_ORDER_NON_INDEX_ARB_FOR_OTHER_AGENCY = 'Y'
    SHORT_EXEMPT_TRANSACTION_FOR_NON_MEMBER_COMPETING_MARKET_MAKER = 'Z'


class SecurityType(Enum):
    BANKERS_ACCEPTANCE = 'BA'
    CERTIFICATE_OF_DEPOSIT = 'CD'
    COLLATERALIZE_MORTGAGE_OBLIGATION = 'CMO'
    CORPORATE_BOND = 'CORP'
    COMMERCIAL_PAPER = 'CP'
    CORPORATE_PRIVATE_PLACEMENT = 'CPP'
    COMMON_STOCK = 'CS'
    FEDERAL_HOUSING_AUTHORITY = 'FHA'
    FEDERAL_HOME_LOAN = 'FHL'
    FEDERAL_NATIONAL_MORTGAGE_ASSOCIATION = 'FN'
    FOREIGN_EXCHANGE_CONTRACT = 'FOR'
    FUTURE = 'FUT'
    GOVERNMENT_NATIONAL_MORTGAGE_ASSOCIATION = 'GN'
    TREASURIES_PLUS_AGENCY_DEBENTURE = 'GOVT'
    MUTUAL_FUND = 'MF'
    MORTGAGE_INTEREST_ONLY = 'MIO'
    MORTGAGE_PRINCIPLE_ONLY = 'MPO'
    MORTGAGE_PRIVATE_PLACEMENT = 'MPP'
    MISCELLANEOUS_PASS_THRU = 'MPT'
    MUNICIPAL_BOND = 'MUNI'
    NO_ISITC_SECURITY_TYPE = 'NONE'
    OPTION = 'OPT'
    PREFERRED_STOCK = 'PS'
    REPURCHASE_AGREEMENT = 'RP'
    REVERSE_REPURCHASE_AGREEMENT = 'RVRP'
    STUDENT_LOAN_MARKETING_ASSOCIATION = 'SL'
    TIME_DEPOSIT = 'TD'
    US_TREASURY_BILL = 'USTB'
    WARRANT = 'WAR'
    CATS_TIGERS_LIONS = 'ZOO'


class SettlCurrFxRateCalc(Enum):
    MULTIPLY = 'M'
    DIVIDE = 'D'


class SettlInstMode(Enum):
    DEFAULT = '0'
    STANDING_INSTRUCTIONS_PROVIDED = '1'
    SPECIFIC_ALLOCATION_ACCOUNT_OVERRIDING = '2'
    SPECIFIC_ALLOCATION_ACCOUNT_STANDING = '3'


class SettlInstSource(Enum):
    BROKERS_INSTRUCTIONS = '1'
    INSTITUTIONS_INSTRUCTIONS = '2'


class SettlInstTransType(Enum):
    CANCEL = 'C'
    NEW = 'N'
    REPLACE = 'R'


class SettlLocation(Enum):
    CEDEL = 'CED'
    DEPOSITORY_TRUST_COMPANY = 'DTC'
    EUROCLEAR = 'EUR'
    FEDERAL_BOOK_ENTRY = 'FED'
    LOCAL_MARKET_SETTLE_LOCATION = 'ISO Country Code'
    PHYSICAL = 'PNY'
    PARTICIPANT_TRUST_COMPANY = 'PTC'


class SettlmntTyp(Enum):
    REGULAR = '0'
    CASH = '1'
    NEXT_DAY = '2'
    T_PLUS_2 = '3'
    T_PLUS_3 = '4'
    T_PLUS_4 = '5'
    FUTURE = '6'
    WHEN_ISSUED = '7'
    SELLERS_OPTION = '8'
    T_PLUS_5 = '9'


class Side(Enum):
    BUY = '1'
    SELL = '2'
    BUY_MINUS = '3'
    SELL_PLUS = '4'
    SELL_SHORT = '5'
    SELL_SHORT_EXEMPT = '6'
    UNDISCLOSED = '7'
    CROSS = '8'


class StandInstDbType(Enum):
    OTHER = '0'
    DTC_SID = '1'
    THOMSON_ALERT = '2'
    A_GLOBAL_CUSTODIAN = '3'


class TimeInForce(Enum):
    DAY = '0'
    GOOD_TILL_CANCEL = '1'
    AT_THE_OPENING = '2'
    IMMEDIATE_OR_CANCEL = '3'
    FILL_OR_KILL = '4'
    GOOD_TILL_CROSSING = '5'
    GOOD_TILL_DATE = '6'


class Urgency(Enum):
    NORMAL = '0'
    FLASH = '1'
    BACKGROUND = '2'
