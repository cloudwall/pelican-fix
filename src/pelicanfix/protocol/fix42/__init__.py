from enum import Enum

from pelicanfix.protocol import FIXField


class Field(Enum):
    ACCOUNT = FIXField('Account', 1)
    ACCRUED_INTEREST_AMT = FIXField('AccruedInterestAmt', 159)
    ACCRUED_INTEREST_RATE = FIXField('AccruedInterestRate', 158)
    ADJUSTMENT = FIXField('Adjustment', 334)
    ADV_ID = FIXField('AdvId', 2)
    ADV_REF_ID = FIXField('AdvRefID', 3)
    ADV_SIDE = FIXField('AdvSide', 4)
    ADV_TRANS_TYPE = FIXField('AdvTransType', 5)
    AGGREGATED_BOOK = FIXField('AggregatedBook', 266)
    ALLOC_ACCOUNT = FIXField('AllocAccount', 79)
    ALLOC_AVG_PX = FIXField('AllocAvgPx', 153)
    ALLOC_HANDL_INST = FIXField('AllocHandlInst', 209)
    ALLOC_ID = FIXField('AllocID', 70)
    ALLOC_LINK_ID = FIXField('AllocLinkID', 196)
    ALLOC_LINK_TYPE = FIXField('AllocLinkType', 197)
    ALLOC_NET_MONEY = FIXField('AllocNetMoney', 154)
    ALLOC_PRICE = FIXField('AllocPrice', 366)
    ALLOC_REJ_CODE = FIXField('AllocRejCode', 88)
    ALLOC_SHARES = FIXField('AllocShares', 80)
    ALLOC_STATUS = FIXField('AllocStatus', 87)
    ALLOC_TEXT = FIXField('AllocText', 161)
    ALLOC_TRANS_TYPE = FIXField('AllocTransType', 71)
    AVG_PRX_PRECISION = FIXField('AvgPrxPrecision', 74)
    AVG_PX = FIXField('AvgPx', 6)
    BASIS_PX_TYPE = FIXField('BasisPxType', 419)
    BEGIN_SEQ_NO = FIXField('BeginSeqNo', 7)
    BEGIN_STRING = FIXField('BeginString', 8)
    BENCHMARK = FIXField('Benchmark', 219)
    BID_DESCRIPTOR = FIXField('BidDescriptor', 400)
    BID_DESCRIPTOR_TYPE = FIXField('BidDescriptorType', 399)
    BID_FORWARD_POINTS = FIXField('BidForwardPoints', 189)
    BID_ID = FIXField('BidID', 390)
    BID_PX = FIXField('BidPx', 132)
    BID_REQUEST_TRANS_TYPE = FIXField('BidRequestTransType', 374)
    BID_SIZE = FIXField('BidSize', 134)
    BID_SPOT_RATE = FIXField('BidSpotRate', 188)
    BID_TYPE = FIXField('BidType', 394)
    BODY_LENGTH = FIXField('BodyLength', 9)
    BROKER_OF_CREDIT = FIXField('BrokerOfCredit', 92)
    BUSINESS_REJECT_REASON = FIXField('BusinessRejectReason', 380)
    BUSINESS_REJECT_REF_ID = FIXField('BusinessRejectRefID', 379)
    BUY_VOLUME = FIXField('BuyVolume', 330)
    CASH_ORDER_QTY = FIXField('CashOrderQty', 152)
    CASH_SETTL_AGENT_ACCT_NAME = FIXField('CashSettlAgentAcctName', 185)
    CASH_SETTL_AGENT_ACCT_NUM = FIXField('CashSettlAgentAcctNum', 184)
    CASH_SETTL_AGENT_CODE = FIXField('CashSettlAgentCode', 183)
    CASH_SETTL_AGENT_CONTACT_NAME = FIXField('CashSettlAgentContactName', 186)
    CASH_SETTL_AGENT_CONTACT_PHONE = FIXField('CashSettlAgentContactPhone', 187)
    CASH_SETTL_AGENT_NAME = FIXField('CashSettlAgentName', 182)
    CHECK_SUM = FIXField('CheckSum', 10)
    CL_ORD_ID = FIXField('ClOrdID', 11)
    CLEARING_ACCOUNT = FIXField('ClearingAccount', 440)
    CLEARING_FIRM = FIXField('ClearingFirm', 439)
    CLIENT_BID_ID = FIXField('ClientBidID', 391)
    CLIENT_ID = FIXField('ClientID', 109)
    COMM_TYPE = FIXField('CommType', 13)
    COMMISSION = FIXField('Commission', 12)
    COMPLIANCE_ID = FIXField('ComplianceID', 376)
    CONTRA_BROKER = FIXField('ContraBroker', 375)
    CONTRA_TRADE_QTY = FIXField('ContraTradeQty', 437)
    CONTRA_TRADE_TIME = FIXField('ContraTradeTime', 438)
    CONTRA_TRADER = FIXField('ContraTrader', 337)
    CONTRACT_MULTIPLIER = FIXField('ContractMultiplier', 231)
    CORPORATE_ACTION = FIXField('CorporateAction', 292)
    COUNTRY = FIXField('Country', 421)
    COUPON_RATE = FIXField('CouponRate', 223)
    COVERED_OR_UNCOVERED = FIXField('CoveredOrUncovered', 203)
    CROSS_PERCENT = FIXField('CrossPercent', 413)
    CUM_QTY = FIXField('CumQty', 14)
    CURRENCY = FIXField('Currency', 15)
    CUSTOMER_OR_FIRM = FIXField('CustomerOrFirm', 204)
    CXL_QTY = FIXField('CxlQty', 84)
    CXL_REJ_REASON = FIXField('CxlRejReason', 102)
    CXL_REJ_RESPONSE_TO = FIXField('CxlRejResponseTo', 434)
    CXL_TYPE = FIXField('CxlType', 125)
    DK_REASON = FIXField('DKReason', 127)
    DAY_AVG_PX = FIXField('DayAvgPx', 426)
    DAY_CUM_QTY = FIXField('DayCumQty', 425)
    DAY_ORDER_QTY = FIXField('DayOrderQty', 424)
    DEF_BID_SIZE = FIXField('DefBidSize', 293)
    DEF_OFFER_SIZE = FIXField('DefOfferSize', 294)
    DELETE_REASON = FIXField('DeleteReason', 285)
    DELIVER_TO_COMP_ID = FIXField('DeliverToCompID', 128)
    DELIVER_TO_LOCATION_ID = FIXField('DeliverToLocationID', 145)
    DELIVER_TO_SUB_ID = FIXField('DeliverToSubID', 129)
    DESK_ID = FIXField('DeskID', 284)
    DISCRETION_INST = FIXField('DiscretionInst', 388)
    DISCRETION_OFFSET = FIXField('DiscretionOffset', 389)
    DLVY_INST = FIXField('DlvyInst', 86)
    DUE_TO_RELATED = FIXField('DueToRelated', 329)
    EFP_TRACKING_ERROR = FIXField('EFPTrackingError', 405)
    EFFECTIVE_TIME = FIXField('EffectiveTime', 168)
    EMAIL_THREAD_ID = FIXField('EmailThreadID', 164)
    EMAIL_TYPE = FIXField('EmailType', 94)
    ENCODED_ALLOC_TEXT = FIXField('EncodedAllocText', 361)
    ENCODED_ALLOC_TEXT_LEN = FIXField('EncodedAllocTextLen', 360)
    ENCODED_HEADLINE = FIXField('EncodedHeadline', 359)
    ENCODED_HEADLINE_LEN = FIXField('EncodedHeadlineLen', 358)
    ENCODED_ISSUER = FIXField('EncodedIssuer', 349)
    ENCODED_ISSUER_LEN = FIXField('EncodedIssuerLen', 348)
    ENCODED_LIST_EXEC_INST = FIXField('EncodedListExecInst', 353)
    ENCODED_LIST_EXEC_INST_LEN = FIXField('EncodedListExecInstLen', 352)
    ENCODED_LIST_STATUS_TEXT = FIXField('EncodedListStatusText', 446)
    ENCODED_LIST_STATUS_TEXT_LEN = FIXField('EncodedListStatusTextLen', 445)
    ENCODED_SECURITY_DESC = FIXField('EncodedSecurityDesc', 351)
    ENCODED_SECURITY_DESC_LEN = FIXField('EncodedSecurityDescLen', 350)
    ENCODED_SUBJECT = FIXField('EncodedSubject', 357)
    ENCODED_SUBJECT_LEN = FIXField('EncodedSubjectLen', 356)
    ENCODED_TEXT = FIXField('EncodedText', 355)
    ENCODED_TEXT_LEN = FIXField('EncodedTextLen', 354)
    ENCODED_UNDERLYING_ISSUER = FIXField('EncodedUnderlyingIssuer', 363)
    ENCODED_UNDERLYING_ISSUER_LEN = FIXField('EncodedUnderlyingIssuerLen', 362)
    ENCODED_UNDERLYING_SECURITY_DESC = FIXField('EncodedUnderlyingSecurityDesc', 365)
    ENCODED_UNDERLYING_SECURITY_DESC_LEN = FIXField('EncodedUnderlyingSecurityDescLen', 364)
    ENCRYPT_METHOD = FIXField('EncryptMethod', 98)
    END_SEQ_NO = FIXField('EndSeqNo', 16)
    EX_DESTINATION = FIXField('ExDestination', 100)
    EXCHANGE_FOR_PHYSICAL = FIXField('ExchangeForPhysical', 411)
    EXEC_BROKER = FIXField('ExecBroker', 76)
    EXEC_ID = FIXField('ExecID', 17)
    EXEC_INST = FIXField('ExecInst', 18)
    EXEC_REF_ID = FIXField('ExecRefID', 19)
    EXEC_RESTATEMENT_REASON = FIXField('ExecRestatementReason', 378)
    EXEC_TRANS_TYPE = FIXField('ExecTransType', 20)
    EXEC_TYPE = FIXField('ExecType', 150)
    EXPIRE_DATE = FIXField('ExpireDate', 432)
    EXPIRE_TIME = FIXField('ExpireTime', 126)
    FAIR_VALUE = FIXField('FairValue', 406)
    FINANCIAL_STATUS = FIXField('FinancialStatus', 291)
    FOREX_REQ = FIXField('ForexReq', 121)
    FUT_SETT_DATE = FIXField('FutSettDate', 64)
    FUT_SETT_DATE2 = FIXField('FutSettDate2', 193)
    GT_BOOKING_INST = FIXField('GTBookingInst', 427)
    GAP_FILL_FLAG = FIXField('GapFillFlag', 123)
    GROSS_TRADE_AMT = FIXField('GrossTradeAmt', 381)
    HALT_REASON_CHAR = FIXField('HaltReasonChar', 327)
    HANDL_INST = FIXField('HandlInst', 21)
    HEADLINE = FIXField('Headline', 148)
    HEART_BT_INT = FIXField('HeartBtInt', 108)
    HIGH_PX = FIXField('HighPx', 332)
    ID_SOURCE = FIXField('IDSource', 22)
    IOI_NATURAL_FLAG = FIXField('IOINaturalFlag', 130)
    IOI_OTH_SVC = FIXField('IOIOthSvc', 24)
    IOI_QLTY_IND = FIXField('IOIQltyInd', 25)
    IOI_QUALIFIER = FIXField('IOIQualifier', 104)
    IOI_REF_ID = FIXField('IOIRefID', 26)
    IOI_SHARES = FIXField('IOIShares', 27)
    IOI_TRANS_TYPE = FIXField('IOITransType', 28)
    IO_IID = FIXField('IOIid', 23)
    IN_VIEW_OF_COMMON = FIXField('InViewOfCommon', 328)
    INC_TAX_IND = FIXField('IncTaxInd', 416)
    ISSUER = FIXField('Issuer', 106)
    LAST_CAPACITY = FIXField('LastCapacity', 29)
    LAST_FORWARD_POINTS = FIXField('LastForwardPoints', 195)
    LAST_MKT = FIXField('LastMkt', 30)
    LAST_MSG_SEQ_NUM_PROCESSED = FIXField('LastMsgSeqNumProcessed', 369)
    LAST_PX = FIXField('LastPx', 31)
    LAST_SHARES = FIXField('LastShares', 32)
    LAST_SPOT_RATE = FIXField('LastSpotRate', 194)
    LEAVES_QTY = FIXField('LeavesQty', 151)
    LINES_OF_TEXT = FIXField('LinesOfText', 33)
    LIQUIDITY_IND_TYPE = FIXField('LiquidityIndType', 409)
    LIQUIDITY_NUM_SECURITIES = FIXField('LiquidityNumSecurities', 441)
    LIQUIDITY_PCT_HIGH = FIXField('LiquidityPctHigh', 403)
    LIQUIDITY_PCT_LOW = FIXField('LiquidityPctLow', 402)
    LIQUIDITY_VALUE = FIXField('LiquidityValue', 404)
    LIST_EXEC_INST = FIXField('ListExecInst', 69)
    LIST_EXEC_INST_TYPE = FIXField('ListExecInstType', 433)
    LIST_ID = FIXField('ListID', 66)
    LIST_NAME = FIXField('ListName', 392)
    LIST_ORDER_STATUS = FIXField('ListOrderStatus', 431)
    LIST_SEQ_NO = FIXField('ListSeqNo', 67)
    LIST_STATUS_TEXT = FIXField('ListStatusText', 444)
    LIST_STATUS_TYPE = FIXField('ListStatusType', 429)
    LOCATE_REQD = FIXField('LocateReqd', 114)
    LOCATION_ID = FIXField('LocationID', 283)
    LOW_PX = FIXField('LowPx', 333)
    MD_ENTRY_BUYER = FIXField('MDEntryBuyer', 288)
    MD_ENTRY_DATE = FIXField('MDEntryDate', 272)
    MD_ENTRY_ID = FIXField('MDEntryID', 278)
    MD_ENTRY_ORIGINATOR = FIXField('MDEntryOriginator', 282)
    MD_ENTRY_POSITION_NO = FIXField('MDEntryPositionNo', 290)
    MD_ENTRY_PX = FIXField('MDEntryPx', 270)
    MD_ENTRY_REF_ID = FIXField('MDEntryRefID', 280)
    MD_ENTRY_SELLER = FIXField('MDEntrySeller', 289)
    MD_ENTRY_SIZE = FIXField('MDEntrySize', 271)
    MD_ENTRY_TIME = FIXField('MDEntryTime', 273)
    MD_ENTRY_TYPE = FIXField('MDEntryType', 269)
    MD_MKT = FIXField('MDMkt', 275)
    MD_REQ_ID = FIXField('MDReqID', 262)
    MD_REQ_REJ_REASON = FIXField('MDReqRejReason', 281)
    MD_UPDATE_ACTION = FIXField('MDUpdateAction', 279)
    MD_UPDATE_TYPE = FIXField('MDUpdateType', 265)
    MARKET_DEPTH = FIXField('MarketDepth', 264)
    MATURITY_DAY = FIXField('MaturityDay', 205)
    MATURITY_MONTH_YEAR = FIXField('MaturityMonthYear', 200)
    MAX_FLOOR = FIXField('MaxFloor', 111)
    MAX_MESSAGE_SIZE = FIXField('MaxMessageSize', 383)
    MAX_SHOW = FIXField('MaxShow', 210)
    MESSAGE_ENCODING = FIXField('MessageEncoding', 347)
    MIN_QTY = FIXField('MinQty', 110)
    MISC_FEE_AMT = FIXField('MiscFeeAmt', 137)
    MISC_FEE_CURR = FIXField('MiscFeeCurr', 138)
    MISC_FEE_TYPE = FIXField('MiscFeeType', 139)
    MSG_DIRECTION = FIXField('MsgDirection', 385)
    MSG_SEQ_NUM = FIXField('MsgSeqNum', 34)
    MSG_TYPE = FIXField('MsgType', 35)
    MULTI_LEG_REPORTING_TYPE = FIXField('MultiLegReportingType', 442)
    NET_GROSS_IND = FIXField('NetGrossInd', 430)
    NET_MONEY = FIXField('NetMoney', 118)
    NEW_SEQ_NO = FIXField('NewSeqNo', 36)
    NO_ALLOCS = FIXField('NoAllocs', 78)
    NO_BID_COMPONENTS = FIXField('NoBidComponents', 420)
    NO_BID_DESCRIPTORS = FIXField('NoBidDescriptors', 398)
    NO_CONTRA_BROKERS = FIXField('NoContraBrokers', 382)
    NO_DLVY_INST = FIXField('NoDlvyInst', 85)
    NO_EXECS = FIXField('NoExecs', 124)
    NO_IOI_QUALIFIERS = FIXField('NoIOIQualifiers', 199)
    NO_MD_ENTRIES = FIXField('NoMDEntries', 268)
    NO_MD_ENTRY_TYPES = FIXField('NoMDEntryTypes', 267)
    NO_MISC_FEES = FIXField('NoMiscFees', 136)
    NO_MSG_TYPES = FIXField('NoMsgTypes', 384)
    NO_ORDERS = FIXField('NoOrders', 73)
    NO_QUOTE_ENTRIES = FIXField('NoQuoteEntries', 295)
    NO_QUOTE_SETS = FIXField('NoQuoteSets', 296)
    NO_RELATED_SYM = FIXField('NoRelatedSym', 146)
    NO_ROUTING_I_DS = FIXField('NoRoutingIDs', 215)
    NO_RPTS = FIXField('NoRpts', 82)
    NO_STRIKES = FIXField('NoStrikes', 428)
    NO_TRADING_SESSIONS = FIXField('NoTradingSessions', 386)
    NOTIFY_BROKER_OF_CREDIT = FIXField('NotifyBrokerOfCredit', 208)
    NUM_BIDDERS = FIXField('NumBidders', 417)
    NUM_DAYS_INTEREST = FIXField('NumDaysInterest', 157)
    NUM_TICKETS = FIXField('NumTickets', 395)
    NUMBER_OF_ORDERS = FIXField('NumberOfOrders', 346)
    OFFER_FORWARD_POINTS = FIXField('OfferForwardPoints', 191)
    OFFER_PX = FIXField('OfferPx', 133)
    OFFER_SIZE = FIXField('OfferSize', 135)
    OFFER_SPOT_RATE = FIXField('OfferSpotRate', 190)
    ON_BEHALF_OF_COMP_ID = FIXField('OnBehalfOfCompID', 115)
    ON_BEHALF_OF_LOCATION_ID = FIXField('OnBehalfOfLocationID', 144)
    ON_BEHALF_OF_SENDING_TIME = FIXField('OnBehalfOfSendingTime', 370)
    ON_BEHALF_OF_SUB_ID = FIXField('OnBehalfOfSubID', 116)
    OPEN_CLOSE = FIXField('OpenClose', 77)
    OPEN_CLOSE_SETTLE_FLAG = FIXField('OpenCloseSettleFlag', 286)
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
    OUT_MAIN_CNTRY_U_INDEX = FIXField('OutMainCntryUIndex', 412)
    OUTSIDE_INDEX_PCT = FIXField('OutsideIndexPct', 407)
    PEG_DIFFERENCE = FIXField('PegDifference', 211)
    POSS_DUP_FLAG = FIXField('PossDupFlag', 43)
    POSS_RESEND = FIXField('PossResend', 97)
    PREV_CLOSE_PX = FIXField('PrevClosePx', 140)
    PRICE = FIXField('Price', 44)
    PRICE_TYPE = FIXField('PriceType', 423)
    PROCESS_CODE = FIXField('ProcessCode', 81)
    PROG_PERIOD_INTERVAL = FIXField('ProgPeriodInterval', 415)
    PROG_RPT_REQS = FIXField('ProgRptReqs', 414)
    PUT_OR_CALL = FIXField('PutOrCall', 201)
    QUOTE_ACK_STATUS = FIXField('QuoteAckStatus', 297)
    QUOTE_CANCEL_TYPE = FIXField('QuoteCancelType', 298)
    QUOTE_CONDITION = FIXField('QuoteCondition', 276)
    QUOTE_ENTRY_ID = FIXField('QuoteEntryID', 299)
    QUOTE_ENTRY_REJECT_REASON = FIXField('QuoteEntryRejectReason', 368)
    QUOTE_ID = FIXField('QuoteID', 117)
    QUOTE_REJECT_REASON = FIXField('QuoteRejectReason', 300)
    QUOTE_REQ_ID = FIXField('QuoteReqID', 131)
    QUOTE_REQUEST_TYPE = FIXField('QuoteRequestType', 303)
    QUOTE_RESPONSE_LEVEL = FIXField('QuoteResponseLevel', 301)
    QUOTE_SET_ID = FIXField('QuoteSetID', 302)
    QUOTE_SET_VALID_UNTIL_TIME = FIXField('QuoteSetValidUntilTime', 367)
    RATIO_QTY = FIXField('RatioQty', 319)
    RAW_DATA = FIXField('RawData', 96)
    RAW_DATA_LENGTH = FIXField('RawDataLength', 95)
    REF_ALLOC_ID = FIXField('RefAllocID', 72)
    REF_MSG_TYPE = FIXField('RefMsgType', 372)
    REF_SEQ_NUM = FIXField('RefSeqNum', 45)
    REF_TAG_ID = FIXField('RefTagID', 371)
    RELATD_SYM = FIXField('RelatdSym', 46)
    REPORT_TO_EXCH = FIXField('ReportToExch', 113)
    RESET_SEQ_NUM_FLAG = FIXField('ResetSeqNumFlag', 141)
    ROUTING_ID = FIXField('RoutingID', 217)
    ROUTING_TYPE = FIXField('RoutingType', 216)
    RPT_SEQ = FIXField('RptSeq', 83)
    RULE80_A = FIXField('Rule80A', 47)
    SECONDARY_ORDER_ID = FIXField('SecondaryOrderID', 198)
    SECURE_DATA = FIXField('SecureData', 91)
    SECURE_DATA_LEN = FIXField('SecureDataLen', 90)
    SECURITY_DESC = FIXField('SecurityDesc', 107)
    SECURITY_EXCHANGE = FIXField('SecurityExchange', 207)
    SECURITY_ID = FIXField('SecurityID', 48)
    SECURITY_REQ_ID = FIXField('SecurityReqID', 320)
    SECURITY_REQUEST_TYPE = FIXField('SecurityRequestType', 321)
    SECURITY_RESPONSE_ID = FIXField('SecurityResponseID', 322)
    SECURITY_RESPONSE_TYPE = FIXField('SecurityResponseType', 323)
    SECURITY_SETTL_AGENT_ACCT_NAME = FIXField('SecuritySettlAgentAcctName', 179)
    SECURITY_SETTL_AGENT_ACCT_NUM = FIXField('SecuritySettlAgentAcctNum', 178)
    SECURITY_SETTL_AGENT_CODE = FIXField('SecuritySettlAgentCode', 177)
    SECURITY_SETTL_AGENT_CONTACT_NAME = FIXField('SecuritySettlAgentContactName', 180)
    SECURITY_SETTL_AGENT_CONTACT_PHONE = FIXField('SecuritySettlAgentContactPhone', 181)
    SECURITY_SETTL_AGENT_NAME = FIXField('SecuritySettlAgentName', 176)
    SECURITY_STATUS_REQ_ID = FIXField('SecurityStatusReqID', 324)
    SECURITY_TRADING_STATUS = FIXField('SecurityTradingStatus', 326)
    SECURITY_TYPE = FIXField('SecurityType', 167)
    SELL_VOLUME = FIXField('SellVolume', 331)
    SELLER_DAYS = FIXField('SellerDays', 287)
    SENDER_COMP_ID = FIXField('SenderCompID', 49)
    SENDER_LOCATION_ID = FIXField('SenderLocationID', 142)
    SENDER_SUB_ID = FIXField('SenderSubID', 50)
    SENDING_DATE = FIXField('SendingDate', 51)
    SENDING_TIME = FIXField('SendingTime', 52)
    SESSION_REJECT_REASON = FIXField('SessionRejectReason', 373)
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
    SETTL_INST_REF_ID = FIXField('SettlInstRefID', 214)
    SETTL_INST_SOURCE = FIXField('SettlInstSource', 165)
    SETTL_INST_TRANS_TYPE = FIXField('SettlInstTransType', 163)
    SETTL_LOCATION = FIXField('SettlLocation', 166)
    SETTLMNT_TYP = FIXField('SettlmntTyp', 63)
    SHARES = FIXField('Shares', 53)
    SIDE = FIXField('Side', 54)
    SIDE_VALUE1 = FIXField('SideValue1', 396)
    SIDE_VALUE2 = FIXField('SideValue2', 397)
    SIDE_VALUE_IND = FIXField('SideValueInd', 401)
    SIGNATURE = FIXField('Signature', 89)
    SIGNATURE_LENGTH = FIXField('SignatureLength', 93)
    SOLICITED_FLAG = FIXField('SolicitedFlag', 377)
    SPREAD_TO_BENCHMARK = FIXField('SpreadToBenchmark', 218)
    STAND_INST_DB_ID = FIXField('StandInstDbID', 171)
    STAND_INST_DB_NAME = FIXField('StandInstDbName', 170)
    STAND_INST_DB_TYPE = FIXField('StandInstDbType', 169)
    STOP_PX = FIXField('StopPx', 99)
    STRIKE_PRICE = FIXField('StrikePrice', 202)
    STRIKE_TIME = FIXField('StrikeTime', 443)
    SUBJECT = FIXField('Subject', 147)
    SUBSCRIPTION_REQUEST_TYPE = FIXField('SubscriptionRequestType', 263)
    SYMBOL = FIXField('Symbol', 55)
    SYMBOL_SFX = FIXField('SymbolSfx', 65)
    TARGET_COMP_ID = FIXField('TargetCompID', 56)
    TARGET_LOCATION_ID = FIXField('TargetLocationID', 143)
    TARGET_SUB_ID = FIXField('TargetSubID', 57)
    TEST_REQ_ID = FIXField('TestReqID', 112)
    TEXT = FIXField('Text', 58)
    TICK_DIRECTION = FIXField('TickDirection', 274)
    TIME_IN_FORCE = FIXField('TimeInForce', 59)
    TOT_NO_ORDERS = FIXField('TotNoOrders', 68)
    TOT_NO_STRIKES = FIXField('TotNoStrikes', 422)
    TOT_QUOTE_ENTRIES = FIXField('TotQuoteEntries', 304)
    TOTAL_NUM_SECURITIES = FIXField('TotalNumSecurities', 393)
    TOTAL_VOLUME_TRADED = FIXField('TotalVolumeTraded', 387)
    TRAD_SES_CLOSE_TIME = FIXField('TradSesCloseTime', 344)
    TRAD_SES_END_TIME = FIXField('TradSesEndTime', 345)
    TRAD_SES_METHOD = FIXField('TradSesMethod', 338)
    TRAD_SES_MODE = FIXField('TradSesMode', 339)
    TRAD_SES_OPEN_TIME = FIXField('TradSesOpenTime', 342)
    TRAD_SES_PRE_CLOSE_TIME = FIXField('TradSesPreCloseTime', 343)
    TRAD_SES_REQ_ID = FIXField('TradSesReqID', 335)
    TRAD_SES_START_TIME = FIXField('TradSesStartTime', 341)
    TRAD_SES_STATUS = FIXField('TradSesStatus', 340)
    TRADE_CONDITION = FIXField('TradeCondition', 277)
    TRADE_DATE = FIXField('TradeDate', 75)
    TRADE_TYPE = FIXField('TradeType', 418)
    TRADING_SESSION_ID = FIXField('TradingSessionID', 336)
    TRANSACT_TIME = FIXField('TransactTime', 60)
    URL_LINK = FIXField('URLLink', 149)
    UNDERLYING_CONTRACT_MULTIPLIER = FIXField('UnderlyingContractMultiplier', 436)
    UNDERLYING_COUPON_RATE = FIXField('UnderlyingCouponRate', 435)
    UNDERLYING_CURRENCY = FIXField('UnderlyingCurrency', 318)
    UNDERLYING_ID_SOURCE = FIXField('UnderlyingIDSource', 305)
    UNDERLYING_ISSUER = FIXField('UnderlyingIssuer', 306)
    UNDERLYING_MATURITY_DAY = FIXField('UnderlyingMaturityDay', 314)
    UNDERLYING_MATURITY_MONTH_YEAR = FIXField('UnderlyingMaturityMonthYear', 313)
    UNDERLYING_OPT_ATTRIBUTE = FIXField('UnderlyingOptAttribute', 317)
    UNDERLYING_PUT_OR_CALL = FIXField('UnderlyingPutOrCall', 315)
    UNDERLYING_SECURITY_DESC = FIXField('UnderlyingSecurityDesc', 307)
    UNDERLYING_SECURITY_EXCHANGE = FIXField('UnderlyingSecurityExchange', 308)
    UNDERLYING_SECURITY_ID = FIXField('UnderlyingSecurityID', 309)
    UNDERLYING_SECURITY_TYPE = FIXField('UnderlyingSecurityType', 310)
    UNDERLYING_STRIKE_PRICE = FIXField('UnderlyingStrikePrice', 316)
    UNDERLYING_SYMBOL = FIXField('UnderlyingSymbol', 311)
    UNDERLYING_SYMBOL_SFX = FIXField('UnderlyingSymbolSfx', 312)
    UNSOLICITED_INDICATOR = FIXField('UnsolicitedIndicator', 325)
    URGENCY = FIXField('Urgency', 61)
    VALID_UNTIL_TIME = FIXField('ValidUntilTime', 62)
    VALUE_OF_FUTURES = FIXField('ValueOfFutures', 408)
    WAVE_NO = FIXField('WaveNo', 105)
    WT_AVERAGE_LIQUIDITY = FIXField('WtAverageLiquidity', 410)
    XML_DATA = FIXField('XmlData', 213)
    XML_DATA_LEN = FIXField('XmlDataLen', 212)


class Adjustment(Enum):
    CANCEL = '1'
    ERROR = '2'
    CORRECTION = '3'


class AdvSide(Enum):
    BUY = 'B'
    SELL = 'S'
    TRADE = 'T'
    CROSS = 'X'


class AdvTransType(Enum):
    CANCEL = 'C'
    NEW = 'N'
    REPLACE = 'R'


class AggregatedBook(Enum):
    NO = 'N'
    YES = 'Y'


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
    CALCULATED_WITHOUT_PRELIMINARY = '5'


class BasisPxType(Enum):
    CLOSING_PRICE_AT_MORNING_SESSION = '2'
    CLOSING_PRICE = '3'
    CURRENT_PRICE = '4'
    SQ = '5'
    VWAP_THROUGH_A_DAY = '6'
    VWAP_THROUGH_A_MORNING_SESSION = '7'
    VWAP_THROUGH_AN_AFTERNOON_SESSION = '8'
    VWAP_THROUGH_A_DAY_EXCEPT_YORI = '9'
    VWAP_THROUGH_A_MORNING_SESSION_EXCEPT_YORI = 'A'
    VWAP_THROUGH_AN_AFTERNOON_SESSION_EXCEPT_YORI = 'B'
    STRIKE = 'C'
    OPEN = 'D'
    OTHERS = 'Z'


class Benchmark(Enum):
    CURVE = '1'
    FIVE_YR = '2'
    OLD_5 = '3'
    TEN_YR = '4'
    OLD_10 = '5'
    THIRTY_YR = '6'
    OLD_30 = '7'
    THREE_MO_LIBOR = '8'
    SIX_MO_LIBOR = '9'


class BidRequestTransType(Enum):
    CANCEL = 'C'
    NO = 'N'


class BusinessRejectReason(Enum):
    OTHER = '0'
    UNKOWN_ID = '1'
    UNKNOWN_SECURITY = '2'
    UNSUPPORTED_MESSAGE_TYPE = '3'
    APPLICATION_NOT_AVAILABLE = '4'
    CONDITIONALLY_REQUIRED_FIELD_MISSING = '5'


class CommType(Enum):
    PER_SHARE = '1'
    PERCENTAGE = '2'
    ABSOLUTE = '3'


class CorporateAction(Enum):
    EX_DIVIDEND = 'A'
    EX_DISTRIBUTION = 'B'
    EX_RIGHTS = 'C'
    NEW = 'D'
    EX_INTEREST = 'E'


class CoveredOrUncovered(Enum):
    COVERED = '0'
    UNCOVERED = '1'


class CustomerOrFirm(Enum):
    CUSTOMER = '0'
    FIRM = '1'


class CxlRejReason(Enum):
    TOO_LATE_TO_CANCEL = '0'
    UNKNOWN_ORDER = '1'
    BROKER_OPTION = '2'
    ORDER_ALREADY_IN_PENDING_CANCEL_OR_PENDING_REPLACE_STATUS = '3'


class CxlRejResponseTo(Enum):
    ORDER_CANCEL_REQUEST = '1'
    ORDER_CANCEL_REPLACE_REQUEST = '2'


class DKReason(Enum):
    UNKNOWN_SYMBOL = 'A'
    WRONG_SIDE = 'B'
    QUANTITY_EXCEEDS_ORDER = 'C'
    NO_MATCHING_ORDER = 'D'
    PRICE_EXCEEDS_LIMIT = 'E'
    OTHER = 'Z'


class DeleteReason(Enum):
    CANCELATION = '0'
    ERROR = '1'


class DiscretionInst(Enum):
    RELATED_TO_DISPLAYED_PRICE = '0'
    RELATED_TO_MARKET_PRICE = '1'
    RELATED_TO_PRIMARY_PRICE = '2'
    RELATED_TO_LOCAL_PRIMARY_PRICE = '3'
    RELATED_TO_MIDPOINT_PRICE = '4'
    RELATED_TO_LAST_TRADE_PRICE = '5'


class DueToRelated(Enum):
    NO = 'N'
    YES = 'Y'


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


class ExchangeForPhysical(Enum):
    NO = 'N'
    YES = 'Y'


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
    FIXED_PEG_TO_LOCAL_BEST_BID_OR_OFFER_AT_TIME_OF_ORDER = 'T'
    CUSTOMER_DISPLAY_INSTRUCTION = 'U'
    NETTING = 'V'
    PEG_TO_VWAP = 'W'


class ExecRestatementReason(Enum):
    GT_CORPORATE_ACTION = '0'
    GT_RENEWAL = '1'
    VERBAL_CHANGE = '2'
    REPRICING_OF_ORDER = '3'
    BROKER_OPTION = '4'
    PARTIAL_DECLINE_OF_ORDERQTY = '5'


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
    CANCELED = '4'
    REPLACE = '5'
    PENDING_CANCEL = '6'
    STOPPED = '7'
    REJECTED = '8'
    SUSPENDED = '9'
    PENDING_NEW = 'A'
    CALCULATED = 'B'
    EXPIRED = 'C'
    RESTATED = 'D'
    PENDING_REPLACE = 'E'


class FinancialStatus(Enum):
    BANKRUPT = '1'


class ForexReq(Enum):
    NO = 'N'
    YES = 'Y'


class GTBookingInst(Enum):
    BOOK_OUT_ALL_TRADES_ON_DAY_OF_EXECUTION = '0'
    ACCUMULATE_EXECUTIONS_UNTIL_ORDER_IS_FILLED_OR_EXPIRES = '1'
    ACCUMULATE_UNTIL_VERBALLY_NOTIFIED_OTHERWISE = '2'


class GapFillFlag(Enum):
    NO = 'N'
    YES = 'Y'


class HaltReasonChar(Enum):
    NEWS_DISSEMINATION = 'D'
    ORDER_INFLUX = 'E'
    ORDER_IMBALANCE = 'I'
    ADDITIONAL_INFORMATION = 'M'
    NEWS_PENDING = 'P'
    EQUIPMENT_CHANGEOVER = 'X'


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
    EXCHANGE_SYMBOL = '8'
    CONSOLIDATED_TAPE_ASSOCIATION = '9'


class IOINaturalFlag(Enum):
    NO = 'N'
    YES = 'Y'


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
    READY_TO_TRADE = 'R'
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


class InViewOfCommon(Enum):
    NO = 'N'
    YES = 'Y'


class IncTaxInd(Enum):
    NET = '1'
    GROSS = '2'


class LastCapacity(Enum):
    AGENT = '1'
    CROSS_AS_AGENT = '2'
    CROSS_AS_PRINCIPAL = '3'
    PRINCIPAL = '4'


class LiquidityIndType(Enum):
    FIVE_DAY_MOVING_AVERAGE = '1'
    TWENTY_DAY_MOVING_AVERAGE = '2'
    NORMAL_MARKET_SIZE = '3'
    OTHER = '4'


class ListExecInstType(Enum):
    IMMEDIATE = '1'
    WAIT_FOR_EXECUTE_INSTRUCTION = '2'


class LocateReqd(Enum):
    NO = 'N'
    YES = 'Y'


class MDEntryType(Enum):
    BID = '0'
    OFFER = '1'
    TRADE = '2'
    INDEX_VALUE = '3'
    OPENING_PRICE = '4'
    CLOSING_PRICE = '5'
    SETTLEMENT_PRICE = '6'
    TRADING_SESSION_HIGH_PRICE = '7'
    TRADING_SESSION_LOW_PRICE = '8'
    TRADING_SESSION_VWAP_PRICE = '9'


class MDReqRejReason(Enum):
    UNKNOWN_SYMBOL = '0'
    DUPLICATE_MDREQID = '1'
    INSUFFICIENT_BANDWIDTH = '2'
    INSUFFICIENT_PERMISSIONS = '3'
    UNSUPPORTED_SUBSCRIPTIONREQUESTTYPE = '4'
    UNSUPPORTED_MARKETDEPTH = '5'
    UNSUPPORTED_MDUPDATETYPE = '6'
    UNSUPPORTED_AGGREGATEDBOOK = '7'
    UNSUPPORTED_MDENTRYTYPE = '8'


class MDUpdateAction(Enum):
    NEW = '0'
    CHANGE = '1'
    DELETE = '2'


class MDUpdateType(Enum):
    FULL_REFRESH = '0'
    INCREMENTAL_REFRESH = '1'


class MessageEncoding(Enum):
    EUC_JP = 'EUC-JP'
    ISO_2022_JP = 'ISO-2022-JP'
    SHIFT_JIS = 'SHIFT_JIS'
    UTF_8 = 'UTF-8'


class MiscFeeType(Enum):
    REGULATORY = '1'
    TAX = '2'
    LOCAL_COMMISSION = '3'
    EXCHANGE_FEES = '4'
    STAMP = '5'
    LEVY = '6'
    OTHER = '7'
    MARKUP = '8'
    CONSUMPTION_TAX = '9'


class MsgDirection(Enum):
    RECEIVE = 'R'
    SEND = 'S'


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
    QUOTE_STATUS_REQUEST = 'a'
    LOGON = 'A'
    NEWS = 'B'
    QUOTE_ACKNOWLEDGEMENT = 'b'
    EMAIL = 'C'
    SECURITY_DEFINITION_REQUEST = 'c'
    ORDER_SINGLE = 'D'
    SECURITY_DEFINITION = 'd'
    ORDER_LIST = 'E'
    SECURITY_STATUS_REQUEST = 'e'
    SECURITY_STATUS = 'f'
    ORDER_CANCEL_REQUEST = 'F'
    ORDER_CANCEL_REPLACE_REQUEST = 'G'
    TRADING_SESSION_STATUS_REQUEST = 'g'
    ORDER_STATUS_REQUEST = 'H'
    TRADING_SESSION_STATUS = 'h'
    MASS_QUOTE = 'i'
    BUSINESS_MESSAGE_REJECT = 'j'
    ALLOCATION = 'J'
    LIST_CANCEL_REQUEST = 'K'
    BID_REQUEST = 'k'
    BID_RESPONSE = 'l'
    LIST_EXECUTE = 'L'
    LIST_STRIKE_PRICE = 'm'
    LIST_STATUS_REQUEST = 'M'
    LIST_STATUS = 'N'
    ALLOCATION_ACK = 'P'
    DONT_KNOW_TRADE = 'Q'
    QUOTE_REQUEST = 'R'
    QUOTE = 'S'
    SETTLEMENT_INSTRUCTIONS = 'T'
    MARKET_DATA_REQUEST = 'V'
    MARKET_DATA_SNAPSHOT_FULL_REFRESH = 'W'
    MARKET_DATA_INCREMENTAL_REFRESH = 'X'
    MARKET_DATA_REQUEST_REJECT = 'Y'
    QUOTE_CANCEL = 'Z'


class MultiLegReportingType(Enum):
    SINGLE_SECURITY = '1'
    INDIVIDUAL_LEG_OF_A_MULTI_LEG_SECURITY = '2'
    MULTI_LEG_SECURITY = '3'


class NetGrossInd(Enum):
    NET = '1'
    GROSS = '2'


class NotifyBrokerOfCredit(Enum):
    NO = 'N'
    YES = 'Y'


class OpenClose(Enum):
    CLOSE = 'C'
    OPEN = 'O'


class OpenCloseSettleFlag(Enum):
    DAILY_OPEN = '0'
    SESSION_OPEN = '1'
    DELIVERY_SETTLEMENT_PRICE = '2'


class OrdRejReason(Enum):
    BROKER_OPTION = '0'
    UNKNOWN_SYMBOL = '1'
    EXCHANGE_CLOSED = '2'
    ORDER_EXCEEDS_LIMIT = '3'
    TOO_LATE_TO_ENTER = '4'
    UNKNOWN_ORDER = '5'
    DUPLICATE_ORDER = '6'
    DUPLICATE_OF_A_VERBALLY_COMMUNICATED_ORDER = '7'
    STALE_ORDER = '8'


class OrdStatus(Enum):
    NEW = '0'
    PARTIALLY_FILLED = '1'
    FILLED = '2'
    DONE_FOR_DAY = '3'
    CANCELED = '4'
    REPLACED = '5'
    PENDING_CANCEL = '6'
    STOPPED = '7'
    REJECTED = '8'
    SUSPENDED = '9'
    PENDING_NEW = 'A'
    CALCULATED = 'B'
    EXPIRED = 'C'
    ACCEPTED_FOR_BIDDING = 'D'
    PENDING_REPLACE = 'E'


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
    FUNARI = 'I'
    PEGGED = 'P'


class PossDupFlag(Enum):
    NO = 'N'
    YES = 'Y'


class PossResend(Enum):
    NO = 'N'
    YES = 'Y'


class PriceType(Enum):
    PERCENTAGE = '1'
    PER_SHARE = '2'
    FIXED_AMOUNT = '3'


class ProcessCode(Enum):
    REGULAR = '0'
    SOFT_DOLLAR = '1'
    STEP_IN = '2'
    STEP_OUT = '3'
    SOFT_DOLLAR_STEP_IN = '4'
    SOFT_DOLLAR_STEP_OUT = '5'
    PLAN_SPONSOR = '6'


class ProgRptReqs(Enum):
    BUYSIDE_EXPLICITLY_REQUESTS_STATUS_USING_STATUSREQUEST = '1'
    SELLSIDE_PERIODICALLY_SENDS_STATUS_USING_LISTSTATUS_PERIOD_OPTIONALLY_SPECIFIED_IN_PROGRESSPERIOD = '2'
    REAL_TIME_EXECUTION_REPORTS = '3'


class PutOrCall(Enum):
    PUT = '0'
    CALL = '1'


class QuoteAckStatus(Enum):
    ACCEPTED = '0'
    CANCELED_FOR_SYMBOL = '1'
    CANCELED_FOR_SECURITY_TYPE = '2'
    CANCELED_FOR_UNDERLYING = '3'
    CANCELED_ALL = '4'
    REJECTED = '5'


class QuoteCancelType(Enum):
    CANCEL_FOR_SYMBOL = '1'
    CANCEL_FOR_SECURITY_TYPE = '2'
    CANCEL_FOR_UNDERLYING_SYMBOL = '3'
    CANCEL_FOR_ALL_QUOTES = '4'


class QuoteCondition(Enum):
    OPEN = 'A'
    CLOSED = 'B'
    EXCHANGE_BEST = 'C'
    CONSOLIDATED_BEST = 'D'
    LOCKED = 'E'
    CROSSED = 'F'
    DEPTH = 'G'
    FAST_TRADING = 'H'
    NON_FIRM = 'I'


class QuoteEntryRejectReason(Enum):
    UNKNOWN_SYMBOL = '1'
    EXCHANGE = '2'
    QUOTE_EXCEEDS_LIMIT = '3'
    TOO_LATE_TO_ENTER = '4'
    UNKNOWN_QUOTE = '5'
    DUPLICATE_QUOTE = '6'
    INVALID_BID_ASK_SPREAD = '7'
    INVALID_PRICE = '8'
    NOT_AUTHORIZED_TO_QUOTE_SECURITY = '9'


class QuoteRejectReason(Enum):
    UNKNOWN_SYMBOL = '1'
    EXCHANGE = '2'
    QUOTE_REQUEST_EXCEEDS_LIMIT = '3'
    TOO_LATE_TO_ENTER = '4'
    UNKNOWN_QUOTE = '5'
    DUPLICATE_QUOTE = '6'
    INVALID_BID_ASK_SPREAD = '7'
    INVALID_PRICE = '8'
    NOT_AUTHORIZED_TO_QUOTE_SECURITY = '9'


class QuoteRequestType(Enum):
    MANUAL = '1'
    AUTOMATIC = '2'


class QuoteResponseLevel(Enum):
    NO_ACKNOWLEDGEMENT = '0'
    ACKNOWLEDGE_ONLY_NEGATIVE_OR_ERRONEOUS_QUOTES = '1'
    ACKNOWLEDGE_EACH_QUOTE_MESSAGES = '2'


class ReportToExch(Enum):
    NO = 'N'
    YES = 'Y'


class ResetSeqNumFlag(Enum):
    NO = 'N'
    YES = 'Y'


class RoutingType(Enum):
    TARGET_FIRM = '1'
    TARGET_LIST = '2'
    BLOCK_FIRM = '3'
    BLOCK_LIST = '4'


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


class SecurityRequestType(Enum):
    REQUEST_SECURITY_IDENTITY_AND_SPECIFICATIONS = '0'
    REQUEST_SECURITY_IDENTITY_FOR_THE_SPECIFICATIONS_PROVIDED = '1'
    REQUEST_LIST_SECURITY_TYPES = '2'
    REQUEST_LIST_SECURITIES = '3'


class SecurityResponseType(Enum):
    ACCEPT_SECURITY_PROPOSAL_AS_IS = '1'
    ACCEPT_SECURITY_PROPOSAL_WITH_REVISIONS_AS_INDICATED_IN_THE_MESSAGE = '2'
    LIST_OF_SECURITY_TYPES_RETURNED_PER_REQUEST = '3'
    LIST_OF_SECURITIES_RETURNED_PER_REQUEST = '4'
    REJECT_SECURITY_PROPOSAL = '5'
    CAN_NOT_MATCH_SELECTION_CRITERIA = '6'


class SecurityTradingStatus(Enum):
    OPENING_DELAY = '1'
    MARKET_ON_CLOSE_IMBALANCE_SELL = '10'
    NO_MARKET_IMBALANCE = '12'
    NO_MARKET_ON_CLOSE_IMBALANCE = '13'
    ITS_PRE_OPENING = '14'
    NEW_PRICE_INDICATION = '15'
    TRADE_DISSEMINATION_TIME = '16'
    READY_TO_TRADE = '17'
    NOT_AVAILABLE_FOR_TRADING = '18'
    NOT_TRADED_ON_THIS_MARKET = '19'
    TRADING_HALT = '2'
    UNKNOWN_OR_INVALID = '20'
    RESUME = '3'
    NO_OPEN_NO_RESUME = '4'
    PRICE_INDICATION = '5'
    TRADING_RANGE_INDICATION = '6'
    MARKET_IMBALANCE_BUY = '7'
    MARKET_IMBALANCE_SELL = '8'
    MARKET_ON_CLOSE_IMBALANCE_BUY = '9'


class SecurityType(Enum):
    WILDCARD_ENTRY = '?'
    BANKERS_ACCEPTANCE = 'BA'
    CONVERTIBLE_BOND = 'CB'
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
    MORTGAGE_IOETTE = 'IET'
    MUTUAL_FUND = 'MF'
    MORTGAGE_INTEREST_ONLY = 'MIO'
    MORTGAGE_PRINCIPAL_ONLY = 'MPO'
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


class SessionRejectReason(Enum):
    INVALID_TAG_NUMBER = '0'
    REQUIRED_TAG_MISSING = '1'
    SENDINGTIME_ACCURACY_PROBLEM = '10'
    INVALID_MSGTYPE = '11'
    TAG_NOT_DEFINED_FOR_THIS_MESSAGE_TYPE = '2'
    UNDEFINED_TAG = '3'
    TAG_SPECIFIED_WITHOUT_A_VALUE = '4'
    VALUE_IS_INCORRECT = '5'
    INCORRECT_DATA_FORMAT_FOR_VALUE = '6'
    DECRYPTION_PROBLEM = '7'
    SIGNATURE_PROBLEM = '8'
    COMPID_PROBLEM = '9'


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
    CROSS_SHORT = '9'


class SolicitedFlag(Enum):
    NO = 'N'
    YES = 'Y'


class StandInstDbType(Enum):
    OTHER = '0'
    DTC_SID = '1'
    THOMSON_ALERT = '2'
    A_GLOBAL_CUSTODIAN = '3'


class SubscriptionRequestType(Enum):
    SNAPSHOT = '0'
    SNAPSHOT_PLUS_UPDATES = '1'
    DISABLE_PREVIOUS_SNAPSHOT_PLUS_UPDATE_REQUEST = '2'


class TickDirection(Enum):
    PLUS_TICK = '0'
    ZERO_PLUS_TICK = '1'
    MINUS_TICK = '2'
    ZERO_MINUS_TICK = '3'


class TimeInForce(Enum):
    DAY = '0'
    GOOD_TILL_CANCEL = '1'
    AT_THE_OPENING = '2'
    IMMEDIATE_OR_CANCEL = '3'
    FILL_OR_KILL = '4'
    GOOD_TILL_CROSSING = '5'
    GOOD_TILL_DATE = '6'


class TradSesMethod(Enum):
    ELECTRONIC = '1'
    OPEN_OUTCRY = '2'
    TWO_PARTY = '3'


class TradSesMode(Enum):
    TESTING = '1'
    SIMULATED = '2'
    PRODUCTION = '3'


class TradSesStatus(Enum):
    HALTED = '1'
    OPEN = '2'
    CLOSED = '3'
    PRE_OPEN = '4'
    PRE_CLOSE = '5'


class TradeCondition(Enum):
    CASH = 'A'
    AVERAGE_PRICE_TRADE = 'B'
    CASH_TRADE = 'C'
    NEXT_DAY = 'D'
    OPENING = 'E'
    INTRADAY_TRADE_DETAIL = 'F'
    RULE_127_TRADE = 'G'
    RULE_155_TRADE = 'H'
    SOLD_LAST = 'I'
    NEXT_DAY_TRADE = 'J'
    OPENED = 'K'
    SELLER = 'L'
    SOLD = 'M'
    STOPPED_STOCK = 'N'


class TradeType(Enum):
    AGENCY = 'A'
    VWAP_GUARANTEE = 'G'
    GUARANTEED_CLOSE = 'J'
    RISK_TRADE = 'R'


class UnsolicitedIndicator(Enum):
    NO = 'N'
    YES = 'Y'


class Urgency(Enum):
    NORMAL = '0'
    FLASH = '1'
    BACKGROUND = '2'
