from enum import Enum

from pelicanfix.protocol import FIXField


class Field(Enum):
    ACCOUNT = FIXField('Account', 1)
    ACCOUNT_TYPE = FIXField('AccountType', 581)
    ACCRUED_INTEREST_AMT = FIXField('AccruedInterestAmt', 159)
    ACCRUED_INTEREST_RATE = FIXField('AccruedInterestRate', 158)
    ADJUSTMENT = FIXField('Adjustment', 334)
    ADV_ID = FIXField('AdvId', 2)
    ADV_REF_ID = FIXField('AdvRefID', 3)
    ADV_SIDE = FIXField('AdvSide', 4)
    ADV_TRANS_TYPE = FIXField('AdvTransType', 5)
    AFFECTED_ORDER_ID = FIXField('AffectedOrderID', 535)
    AFFECTED_SECONDARY_ORDER_ID = FIXField('AffectedSecondaryOrderID', 536)
    AGGREGATED_BOOK = FIXField('AggregatedBook', 266)
    ALLOC_ACCOUNT = FIXField('AllocAccount', 79)
    ALLOC_AVG_PX = FIXField('AllocAvgPx', 153)
    ALLOC_HANDL_INST = FIXField('AllocHandlInst', 209)
    ALLOC_ID = FIXField('AllocID', 70)
    ALLOC_LINK_ID = FIXField('AllocLinkID', 196)
    ALLOC_LINK_TYPE = FIXField('AllocLinkType', 197)
    ALLOC_NET_MONEY = FIXField('AllocNetMoney', 154)
    ALLOC_PRICE = FIXField('AllocPrice', 366)
    ALLOC_QTY = FIXField('AllocQty', 80)
    ALLOC_REJ_CODE = FIXField('AllocRejCode', 88)
    ALLOC_STATUS = FIXField('AllocStatus', 87)
    ALLOC_TEXT = FIXField('AllocText', 161)
    ALLOC_TRANS_TYPE = FIXField('AllocTransType', 71)
    ALLOC_TYPE = FIXField('AllocType', 626)
    AVG_PRX_PRECISION = FIXField('AvgPrxPrecision', 74)
    AVG_PX = FIXField('AvgPx', 6)
    BASIS_FEATURE_DATE = FIXField('BasisFeatureDate', 259)
    BASIS_FEATURE_PRICE = FIXField('BasisFeaturePrice', 260)
    BASIS_PX_TYPE = FIXField('BasisPxType', 419)
    BEGIN_SEQ_NO = FIXField('BeginSeqNo', 7)
    BEGIN_STRING = FIXField('BeginString', 8)
    BENCHMARK = FIXField('Benchmark', 219)
    BENCHMARK_CURVE_CURRENCY = FIXField('BenchmarkCurveCurrency', 220)
    BENCHMARK_CURVE_NAME = FIXField('BenchmarkCurveName', 221)
    BENCHMARK_CURVE_POINT = FIXField('BenchmarkCurvePoint', 222)
    BID_DESCRIPTOR = FIXField('BidDescriptor', 400)
    BID_DESCRIPTOR_TYPE = FIXField('BidDescriptorType', 399)
    BID_FORWARD_POINTS = FIXField('BidForwardPoints', 189)
    BID_FORWARD_POINTS2 = FIXField('BidForwardPoints2', 642)
    BID_ID = FIXField('BidID', 390)
    BID_PX = FIXField('BidPx', 132)
    BID_REQUEST_TRANS_TYPE = FIXField('BidRequestTransType', 374)
    BID_SIZE = FIXField('BidSize', 134)
    BID_SPOT_RATE = FIXField('BidSpotRate', 188)
    BID_TYPE = FIXField('BidType', 394)
    BID_YIELD = FIXField('BidYield', 632)
    BODY_LENGTH = FIXField('BodyLength', 9)
    BOOKING_REF_ID = FIXField('BookingRefID', 466)
    BOOKING_UNIT = FIXField('BookingUnit', 590)
    BUSINESS_REJECT_REASON = FIXField('BusinessRejectReason', 380)
    BUSINESS_REJECT_REF_ID = FIXField('BusinessRejectRefID', 379)
    BUY_VOLUME = FIXField('BuyVolume', 330)
    CFI_CODE = FIXField('CFICode', 461)
    CANCELLATION_RIGHTS = FIXField('CancellationRights', 480)
    CARD_EXP_DATE = FIXField('CardExpDate', 490)
    CARD_HOLDER_NAME = FIXField('CardHolderName', 488)
    CARD_ISS_NO = FIXField('CardIssNo', 491)
    CARD_NUMBER = FIXField('CardNumber', 489)
    CARD_START_DATE = FIXField('CardStartDate', 503)
    CASH_DISTRIB_AGENT_ACCT_NUMBER = FIXField('CashDistribAgentAcctNumber', 500)
    CASH_DISTRIB_AGENT_CODE = FIXField('CashDistribAgentCode', 499)
    CASH_DISTRIB_AGENT_NAME = FIXField('CashDistribAgentName', 498)
    CASH_DISTRIB_CURR = FIXField('CashDistribCurr', 478)
    CASH_DISTRIB_PAY_REF = FIXField('CashDistribPayRef', 501)
    CASH_MARGIN = FIXField('CashMargin', 544)
    CASH_ORDER_QTY = FIXField('CashOrderQty', 152)
    CASH_SETTL_AGENT_ACCT_NAME = FIXField('CashSettlAgentAcctName', 185)
    CASH_SETTL_AGENT_ACCT_NUM = FIXField('CashSettlAgentAcctNum', 184)
    CASH_SETTL_AGENT_CODE = FIXField('CashSettlAgentCode', 183)
    CASH_SETTL_AGENT_CONTACT_NAME = FIXField('CashSettlAgentContactName', 186)
    CASH_SETTL_AGENT_CONTACT_PHONE = FIXField('CashSettlAgentContactPhone', 187)
    CASH_SETTL_AGENT_NAME = FIXField('CashSettlAgentName', 182)
    CHECK_SUM = FIXField('CheckSum', 10)
    CL_ORD_ID = FIXField('ClOrdID', 11)
    CL_ORD_LINK_ID = FIXField('ClOrdLinkID', 583)
    CLEARING_FEE_INDICATOR = FIXField('ClearingFeeIndicator', 635)
    CLEARING_INSTRUCTION = FIXField('ClearingInstruction', 577)
    CLIENT_BID_ID = FIXField('ClientBidID', 391)
    COMM_CURRENCY = FIXField('CommCurrency', 479)
    COMM_TYPE = FIXField('CommType', 13)
    COMMISSION = FIXField('Commission', 12)
    COMPLIANCE_ID = FIXField('ComplianceID', 376)
    CONCESSION = FIXField('Concession', 238)
    CONT_AMT_CURR = FIXField('ContAmtCurr', 521)
    CONT_AMT_TYPE = FIXField('ContAmtType', 519)
    CONT_AMT_VALUE = FIXField('ContAmtValue', 520)
    CONTRA_BROKER = FIXField('ContraBroker', 375)
    CONTRA_LEG_REF_ID = FIXField('ContraLegRefID', 655)
    CONTRA_TRADE_QTY = FIXField('ContraTradeQty', 437)
    CONTRA_TRADE_TIME = FIXField('ContraTradeTime', 438)
    CONTRA_TRADER = FIXField('ContraTrader', 337)
    CONTRACT_MULTIPLIER = FIXField('ContractMultiplier', 231)
    CORPORATE_ACTION = FIXField('CorporateAction', 292)
    COUNTRY = FIXField('Country', 421)
    COUNTRY_OF_ISSUE = FIXField('CountryOfIssue', 470)
    COUPON_PAYMENT_DATE = FIXField('CouponPaymentDate', 224)
    COUPON_RATE = FIXField('CouponRate', 223)
    COVERED_OR_UNCOVERED = FIXField('CoveredOrUncovered', 203)
    CREDIT_RATING = FIXField('CreditRating', 255)
    CROSS_ID = FIXField('CrossID', 548)
    CROSS_PERCENT = FIXField('CrossPercent', 413)
    CROSS_PRIORITIZATION = FIXField('CrossPrioritization', 550)
    CROSS_TYPE = FIXField('CrossType', 549)
    CUM_QTY = FIXField('CumQty', 14)
    CURRENCY = FIXField('Currency', 15)
    CUST_ORDER_CAPACITY = FIXField('CustOrderCapacity', 582)
    CXL_QTY = FIXField('CxlQty', 84)
    CXL_REJ_REASON = FIXField('CxlRejReason', 102)
    CXL_REJ_RESPONSE_TO = FIXField('CxlRejResponseTo', 434)
    DK_REASON = FIXField('DKReason', 127)
    DATE_OF_BIRTH = FIXField('DateOfBirth', 486)
    DAY_AVG_PX = FIXField('DayAvgPx', 426)
    DAY_BOOKING_INST = FIXField('DayBookingInst', 589)
    DAY_CUM_QTY = FIXField('DayCumQty', 425)
    DAY_ORDER_QTY = FIXField('DayOrderQty', 424)
    DEF_BID_SIZE = FIXField('DefBidSize', 293)
    DEF_OFFER_SIZE = FIXField('DefOfferSize', 294)
    DELETE_REASON = FIXField('DeleteReason', 285)
    DELIVER_TO_COMP_ID = FIXField('DeliverToCompID', 128)
    DELIVER_TO_LOCATION_ID = FIXField('DeliverToLocationID', 145)
    DELIVER_TO_SUB_ID = FIXField('DeliverToSubID', 129)
    DESIGNATION = FIXField('Designation', 494)
    DESK_ID = FIXField('DeskID', 284)
    DISCRETION_INST = FIXField('DiscretionInst', 388)
    DISCRETION_OFFSET = FIXField('DiscretionOffset', 389)
    DISTRIB_PAYMENT_METHOD = FIXField('DistribPaymentMethod', 477)
    DISTRIB_PERCENTAGE = FIXField('DistribPercentage', 512)
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
    ENCODED_LEG_ISSUER = FIXField('EncodedLegIssuer', 619)
    ENCODED_LEG_ISSUER_LEN = FIXField('EncodedLegIssuerLen', 618)
    ENCODED_LEG_SECURITY_DESC = FIXField('EncodedLegSecurityDesc', 622)
    ENCODED_LEG_SECURITY_DESC_LEN = FIXField('EncodedLegSecurityDescLen', 621)
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
    EX_DATE = FIXField('ExDate', 230)
    EX_DESTINATION = FIXField('ExDestination', 100)
    EXCHANGE_FOR_PHYSICAL = FIXField('ExchangeForPhysical', 411)
    EXEC_ID = FIXField('ExecID', 17)
    EXEC_INST = FIXField('ExecInst', 18)
    EXEC_PRICE_ADJUSTMENT = FIXField('ExecPriceAdjustment', 485)
    EXEC_PRICE_TYPE = FIXField('ExecPriceType', 484)
    EXEC_REF_ID = FIXField('ExecRefID', 19)
    EXEC_RESTATEMENT_REASON = FIXField('ExecRestatementReason', 378)
    EXEC_TYPE = FIXField('ExecType', 150)
    EXEC_VALUATION_POINT = FIXField('ExecValuationPoint', 515)
    EXPIRE_DATE = FIXField('ExpireDate', 432)
    EXPIRE_TIME = FIXField('ExpireTime', 126)
    FACTOR = FIXField('Factor', 228)
    FAIR_VALUE = FIXField('FairValue', 406)
    FINANCIAL_STATUS = FIXField('FinancialStatus', 291)
    FOREX_REQ = FIXField('ForexReq', 121)
    FUND_RENEW_WAIV = FIXField('FundRenewWaiv', 497)
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
    HOP_COMP_ID = FIXField('HopCompID', 628)
    HOP_REF_ID = FIXField('HopRefID', 630)
    HOP_SENDING_TIME = FIXField('HopSendingTime', 629)
    IOI_NATURAL_FLAG = FIXField('IOINaturalFlag', 130)
    IOI_QLTY_IND = FIXField('IOIQltyInd', 25)
    IOI_QTY = FIXField('IOIQty', 27)
    IOI_QUALIFIER = FIXField('IOIQualifier', 104)
    IOI_REF_ID = FIXField('IOIRefID', 26)
    IOI_TRANS_TYPE = FIXField('IOITransType', 28)
    IO_IID = FIXField('IOIid', 23)
    IN_VIEW_OF_COMMON = FIXField('InViewOfCommon', 328)
    INC_TAX_IND = FIXField('IncTaxInd', 416)
    INDIVIDUAL_ALLOC_ID = FIXField('IndividualAllocID', 467)
    INSTR_REGISTRY = FIXField('InstrRegistry', 543)
    INVESTOR_COUNTRY_OF_RESIDENCE = FIXField('InvestorCountryOfResidence', 475)
    ISSUE_DATE = FIXField('IssueDate', 225)
    ISSUER = FIXField('Issuer', 106)
    LAST_CAPACITY = FIXField('LastCapacity', 29)
    LAST_FORWARD_POINTS = FIXField('LastForwardPoints', 195)
    LAST_FORWARD_POINTS2 = FIXField('LastForwardPoints2', 641)
    LAST_MKT = FIXField('LastMkt', 30)
    LAST_MSG_SEQ_NUM_PROCESSED = FIXField('LastMsgSeqNumProcessed', 369)
    LAST_PX = FIXField('LastPx', 31)
    LAST_QTY = FIXField('LastQty', 32)
    LAST_SPOT_RATE = FIXField('LastSpotRate', 194)
    LEAVES_QTY = FIXField('LeavesQty', 151)
    LEG_CFI_CODE = FIXField('LegCFICode', 608)
    LEG_CONTRACT_MULTIPLIER = FIXField('LegContractMultiplier', 614)
    LEG_COUNTRY_OF_ISSUE = FIXField('LegCountryOfIssue', 596)
    LEG_COUPON_PAYMENT_DATE = FIXField('LegCouponPaymentDate', 248)
    LEG_COUPON_RATE = FIXField('LegCouponRate', 615)
    LEG_COVERED_OR_UNCOVERED = FIXField('LegCoveredOrUncovered', 565)
    LEG_CREDIT_RATING = FIXField('LegCreditRating', 257)
    LEG_CURRENCY = FIXField('LegCurrency', 556)
    LEG_FACTOR = FIXField('LegFactor', 253)
    LEG_FUT_SETT_DATE = FIXField('LegFutSettDate', 588)
    LEG_INSTR_REGISTRY = FIXField('LegInstrRegistry', 599)
    LEG_ISSUE_DATE = FIXField('LegIssueDate', 249)
    LEG_ISSUER = FIXField('LegIssuer', 617)
    LEG_LAST_PX = FIXField('LegLastPx', 637)
    LEG_LOCALE_OF_ISSUE = FIXField('LegLocaleOfIssue', 598)
    LEG_MATURITY_DATE = FIXField('LegMaturityDate', 611)
    LEG_MATURITY_MONTH_YEAR = FIXField('LegMaturityMonthYear', 610)
    LEG_OPT_ATTRIBUTE = FIXField('LegOptAttribute', 613)
    LEG_POSITION_EFFECT = FIXField('LegPositionEffect', 564)
    LEG_PRICE = FIXField('LegPrice', 566)
    LEG_PRODUCT = FIXField('LegProduct', 607)
    LEG_RATIO_QTY = FIXField('LegRatioQty', 623)
    LEG_REDEMPTION_DATE = FIXField('LegRedemptionDate', 254)
    LEG_REF_ID = FIXField('LegRefID', 654)
    LEG_REPO_COLLATERAL_SECURITY_TYPE = FIXField('LegRepoCollateralSecurityType', 250)
    LEG_REPURCHASE_RATE = FIXField('LegRepurchaseRate', 252)
    LEG_REPURCHASE_TERM = FIXField('LegRepurchaseTerm', 251)
    LEG_SECURITY_ALT_ID = FIXField('LegSecurityAltID', 605)
    LEG_SECURITY_ALT_ID_SOURCE = FIXField('LegSecurityAltIDSource', 606)
    LEG_SECURITY_DESC = FIXField('LegSecurityDesc', 620)
    LEG_SECURITY_EXCHANGE = FIXField('LegSecurityExchange', 616)
    LEG_SECURITY_ID = FIXField('LegSecurityID', 602)
    LEG_SECURITY_ID_SOURCE = FIXField('LegSecurityIDSource', 603)
    LEG_SECURITY_TYPE = FIXField('LegSecurityType', 609)
    LEG_SETTLMNT_TYP = FIXField('LegSettlmntTyp', 587)
    LEG_SIDE = FIXField('LegSide', 624)
    LEG_STATE_OR_PROVINCE_OF_ISSUE = FIXField('LegStateOrProvinceOfIssue', 597)
    LEG_STRIKE_PRICE = FIXField('LegStrikePrice', 612)
    LEG_SYMBOL = FIXField('LegSymbol', 600)
    LEG_SYMBOL_SFX = FIXField('LegSymbolSfx', 601)
    LEGAL_CONFIRM = FIXField('LegalConfirm', 650)
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
    LOCALE_OF_ISSUE = FIXField('LocaleOfIssue', 472)
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
    MD_IMPLICIT_DELETE = FIXField('MDImplicitDelete', 547)
    MD_MKT = FIXField('MDMkt', 275)
    MD_REQ_ID = FIXField('MDReqID', 262)
    MD_REQ_REJ_REASON = FIXField('MDReqRejReason', 281)
    MD_UPDATE_ACTION = FIXField('MDUpdateAction', 279)
    MD_UPDATE_TYPE = FIXField('MDUpdateType', 265)
    MAILING_DTLS = FIXField('MailingDtls', 474)
    MAILING_INST = FIXField('MailingInst', 482)
    MARKET_DEPTH = FIXField('MarketDepth', 264)
    MASS_CANCEL_REJECT_REASON = FIXField('MassCancelRejectReason', 532)
    MASS_CANCEL_REQUEST_TYPE = FIXField('MassCancelRequestType', 530)
    MASS_CANCEL_RESPONSE = FIXField('MassCancelResponse', 531)
    MASS_STATUS_REQ_ID = FIXField('MassStatusReqID', 584)
    MASS_STATUS_REQ_TYPE = FIXField('MassStatusReqType', 585)
    MATCH_STATUS = FIXField('MatchStatus', 573)
    MATCH_TYPE = FIXField('MatchType', 574)
    MATURITY_DATE = FIXField('MaturityDate', 541)
    MATURITY_MONTH_YEAR = FIXField('MaturityMonthYear', 200)
    MAX_FLOOR = FIXField('MaxFloor', 111)
    MAX_MESSAGE_SIZE = FIXField('MaxMessageSize', 383)
    MAX_SHOW = FIXField('MaxShow', 210)
    MESSAGE_ENCODING = FIXField('MessageEncoding', 347)
    MID_PX = FIXField('MidPx', 631)
    MID_YIELD = FIXField('MidYield', 633)
    MIN_BID_SIZE = FIXField('MinBidSize', 647)
    MIN_OFFER_SIZE = FIXField('MinOfferSize', 648)
    MIN_QTY = FIXField('MinQty', 110)
    MIN_TRADE_VOL = FIXField('MinTradeVol', 562)
    MISC_FEE_AMT = FIXField('MiscFeeAmt', 137)
    MISC_FEE_CURR = FIXField('MiscFeeCurr', 138)
    MISC_FEE_TYPE = FIXField('MiscFeeType', 139)
    MKT_BID_PX = FIXField('MktBidPx', 645)
    MKT_OFFER_PX = FIXField('MktOfferPx', 646)
    MONEY_LAUNDERING_STATUS = FIXField('MoneyLaunderingStatus', 481)
    MSG_DIRECTION = FIXField('MsgDirection', 385)
    MSG_SEQ_NUM = FIXField('MsgSeqNum', 34)
    MSG_TYPE = FIXField('MsgType', 35)
    MULTI_LEG_REPORTING_TYPE = FIXField('MultiLegReportingType', 442)
    MULTI_LEG_RPT_TYPE_REQ = FIXField('MultiLegRptTypeReq', 563)
    NESTED_PARTY_ID = FIXField('NestedPartyID', 524)
    NESTED_PARTY_ID_SOURCE = FIXField('NestedPartyIDSource', 525)
    NESTED_PARTY_ROLE = FIXField('NestedPartyRole', 538)
    NESTED_PARTY_SUB_ID = FIXField('NestedPartySubID', 545)
    NET_CHG_PREV_DAY = FIXField('NetChgPrevDay', 451)
    NET_GROSS_IND = FIXField('NetGrossInd', 430)
    NET_MONEY = FIXField('NetMoney', 118)
    NEW_SEQ_NO = FIXField('NewSeqNo', 36)
    NO_AFFECTED_ORDERS = FIXField('NoAffectedOrders', 534)
    NO_ALLOCS = FIXField('NoAllocs', 78)
    NO_BID_COMPONENTS = FIXField('NoBidComponents', 420)
    NO_BID_DESCRIPTORS = FIXField('NoBidDescriptors', 398)
    NO_CLEARING_INSTRUCTIONS = FIXField('NoClearingInstructions', 576)
    NO_CONT_AMTS = FIXField('NoContAmts', 518)
    NO_CONTRA_BROKERS = FIXField('NoContraBrokers', 382)
    NO_DATES = FIXField('NoDates', 580)
    NO_DISTRIB_INSTS = FIXField('NoDistribInsts', 510)
    NO_EXECS = FIXField('NoExecs', 124)
    NO_HOPS = FIXField('NoHops', 627)
    NO_IOI_QUALIFIERS = FIXField('NoIOIQualifiers', 199)
    NO_LEG_SECURITY_ALT_ID = FIXField('NoLegSecurityAltID', 604)
    NO_LEGS = FIXField('NoLegs', 555)
    NO_MD_ENTRIES = FIXField('NoMDEntries', 268)
    NO_MD_ENTRY_TYPES = FIXField('NoMDEntryTypes', 267)
    NO_MISC_FEES = FIXField('NoMiscFees', 136)
    NO_MSG_TYPES = FIXField('NoMsgTypes', 384)
    NO_NESTED_PARTY_I_DS = FIXField('NoNestedPartyIDs', 539)
    NO_ORDERS = FIXField('NoOrders', 73)
    NO_PARTY_I_DS = FIXField('NoPartyIDs', 453)
    NO_QUOTE_ENTRIES = FIXField('NoQuoteEntries', 295)
    NO_QUOTE_SETS = FIXField('NoQuoteSets', 296)
    NO_REGIST_DTLS = FIXField('NoRegistDtls', 473)
    NO_RELATED_SYM = FIXField('NoRelatedSym', 146)
    NO_ROUTING_I_DS = FIXField('NoRoutingIDs', 215)
    NO_RPTS = FIXField('NoRpts', 82)
    NO_SECURITY_ALT_ID = FIXField('NoSecurityAltID', 454)
    NO_SECURITY_TYPES = FIXField('NoSecurityTypes', 558)
    NO_SIDES = FIXField('NoSides', 552)
    NO_STIPULATIONS = FIXField('NoStipulations', 232)
    NO_STRIKES = FIXField('NoStrikes', 428)
    NO_TRADING_SESSIONS = FIXField('NoTradingSessions', 386)
    NO_UNDERLYING_SECURITY_ALT_ID = FIXField('NoUnderlyingSecurityAltID', 457)
    NOTIFY_BROKER_OF_CREDIT = FIXField('NotifyBrokerOfCredit', 208)
    NUM_BIDDERS = FIXField('NumBidders', 417)
    NUM_DAYS_INTEREST = FIXField('NumDaysInterest', 157)
    NUM_TICKETS = FIXField('NumTickets', 395)
    NUMBER_OF_ORDERS = FIXField('NumberOfOrders', 346)
    ODD_LOT = FIXField('OddLot', 575)
    OFFER_FORWARD_POINTS = FIXField('OfferForwardPoints', 191)
    OFFER_FORWARD_POINTS2 = FIXField('OfferForwardPoints2', 643)
    OFFER_PX = FIXField('OfferPx', 133)
    OFFER_SIZE = FIXField('OfferSize', 135)
    OFFER_SPOT_RATE = FIXField('OfferSpotRate', 190)
    OFFER_YIELD = FIXField('OfferYield', 634)
    ON_BEHALF_OF_COMP_ID = FIXField('OnBehalfOfCompID', 115)
    ON_BEHALF_OF_LOCATION_ID = FIXField('OnBehalfOfLocationID', 144)
    ON_BEHALF_OF_SENDING_TIME = FIXField('OnBehalfOfSendingTime', 370)
    ON_BEHALF_OF_SUB_ID = FIXField('OnBehalfOfSubID', 116)
    OPEN_CLOSE_SETTLE_FLAG = FIXField('OpenCloseSettleFlag', 286)
    OPT_ATTRIBUTE = FIXField('OptAttribute', 206)
    ORD_REJ_REASON = FIXField('OrdRejReason', 103)
    ORD_STATUS = FIXField('OrdStatus', 39)
    ORD_TYPE = FIXField('OrdType', 40)
    ORDER_CAPACITY = FIXField('OrderCapacity', 528)
    ORDER_ID = FIXField('OrderID', 37)
    ORDER_PERCENT = FIXField('OrderPercent', 516)
    ORDER_QTY = FIXField('OrderQty', 38)
    ORDER_QTY2 = FIXField('OrderQty2', 192)
    ORDER_RESTRICTIONS = FIXField('OrderRestrictions', 529)
    ORIG_CL_ORD_ID = FIXField('OrigClOrdID', 41)
    ORIG_CROSS_ID = FIXField('OrigCrossID', 551)
    ORIG_ORD_MOD_TIME = FIXField('OrigOrdModTime', 586)
    ORIG_SENDING_TIME = FIXField('OrigSendingTime', 122)
    ORIG_TIME = FIXField('OrigTime', 42)
    OUT_MAIN_CNTRY_U_INDEX = FIXField('OutMainCntryUIndex', 412)
    OUTSIDE_INDEX_PCT = FIXField('OutsideIndexPct', 407)
    OWNER_TYPE = FIXField('OwnerType', 522)
    OWNERSHIP_TYPE = FIXField('OwnershipType', 517)
    PARTY_ID = FIXField('PartyID', 448)
    PARTY_ID_SOURCE = FIXField('PartyIDSource', 447)
    PARTY_ROLE = FIXField('PartyRole', 452)
    PARTY_SUB_ID = FIXField('PartySubID', 523)
    PASSWORD = FIXField('Password', 554)
    PAYMENT_DATE = FIXField('PaymentDate', 504)
    PAYMENT_METHOD = FIXField('PaymentMethod', 492)
    PAYMENT_REF = FIXField('PaymentRef', 476)
    PAYMENT_REMITTER_ID = FIXField('PaymentRemitterID', 505)
    PEG_DIFFERENCE = FIXField('PegDifference', 211)
    POSITION_EFFECT = FIXField('PositionEffect', 77)
    POSS_DUP_FLAG = FIXField('PossDupFlag', 43)
    POSS_RESEND = FIXField('PossResend', 97)
    PREALLOC_METHOD = FIXField('PreallocMethod', 591)
    PREV_CLOSE_PX = FIXField('PrevClosePx', 140)
    PREVIOUSLY_REPORTED = FIXField('PreviouslyReported', 570)
    PRICE = FIXField('Price', 44)
    PRICE2 = FIXField('Price2', 640)
    PRICE_IMPROVEMENT = FIXField('PriceImprovement', 639)
    PRICE_TYPE = FIXField('PriceType', 423)
    PRIORITY_INDICATOR = FIXField('PriorityIndicator', 638)
    PROCESS_CODE = FIXField('ProcessCode', 81)
    PRODUCT = FIXField('Product', 460)
    PROG_PERIOD_INTERVAL = FIXField('ProgPeriodInterval', 415)
    PROG_RPT_REQS = FIXField('ProgRptReqs', 414)
    QUANTITY = FIXField('Quantity', 53)
    QUANTITY_TYPE = FIXField('QuantityType', 465)
    QUOTE_CANCEL_TYPE = FIXField('QuoteCancelType', 298)
    QUOTE_CONDITION = FIXField('QuoteCondition', 276)
    QUOTE_ENTRY_ID = FIXField('QuoteEntryID', 299)
    QUOTE_ENTRY_REJECT_REASON = FIXField('QuoteEntryRejectReason', 368)
    QUOTE_ID = FIXField('QuoteID', 117)
    QUOTE_REJECT_REASON = FIXField('QuoteRejectReason', 300)
    QUOTE_REQ_ID = FIXField('QuoteReqID', 131)
    QUOTE_REQUEST_REJECT_REASON = FIXField('QuoteRequestRejectReason', 658)
    QUOTE_REQUEST_TYPE = FIXField('QuoteRequestType', 303)
    QUOTE_RESPONSE_LEVEL = FIXField('QuoteResponseLevel', 301)
    QUOTE_SET_ID = FIXField('QuoteSetID', 302)
    QUOTE_SET_VALID_UNTIL_TIME = FIXField('QuoteSetValidUntilTime', 367)
    QUOTE_STATUS = FIXField('QuoteStatus', 297)
    QUOTE_STATUS_REQ_ID = FIXField('QuoteStatusReqID', 649)
    QUOTE_TYPE = FIXField('QuoteType', 537)
    RFQ_REQ_ID = FIXField('RFQReqID', 644)
    RAW_DATA = FIXField('RawData', 96)
    RAW_DATA_LENGTH = FIXField('RawDataLength', 95)
    REDEMPTION_DATE = FIXField('RedemptionDate', 240)
    REF_ALLOC_ID = FIXField('RefAllocID', 72)
    REF_MSG_TYPE = FIXField('RefMsgType', 372)
    REF_SEQ_NUM = FIXField('RefSeqNum', 45)
    REF_TAG_ID = FIXField('RefTagID', 371)
    REGIST_ACCT_TYPE = FIXField('RegistAcctType', 493)
    REGIST_DETLS = FIXField('RegistDetls', 509)
    REGIST_EMAIL = FIXField('RegistEmail', 511)
    REGIST_ID = FIXField('RegistID', 513)
    REGIST_REF_ID = FIXField('RegistRefID', 508)
    REGIST_REJ_REASON_CODE = FIXField('RegistRejReasonCode', 507)
    REGIST_REJ_REASON_TEXT = FIXField('RegistRejReasonText', 496)
    REGIST_STATUS = FIXField('RegistStatus', 506)
    REGIST_TRANS_TYPE = FIXField('RegistTransType', 514)
    REPO_COLLATERAL_SECURITY_TYPE = FIXField('RepoCollateralSecurityType', 239)
    REPORT_TO_EXCH = FIXField('ReportToExch', 113)
    REPURCHASE_RATE = FIXField('RepurchaseRate', 227)
    REPURCHASE_TERM = FIXField('RepurchaseTerm', 226)
    RESET_SEQ_NUM_FLAG = FIXField('ResetSeqNumFlag', 141)
    ROUND_LOT = FIXField('RoundLot', 561)
    ROUNDING_DIRECTION = FIXField('RoundingDirection', 468)
    ROUNDING_MODULUS = FIXField('RoundingModulus', 469)
    ROUTING_ID = FIXField('RoutingID', 217)
    ROUTING_TYPE = FIXField('RoutingType', 216)
    RPT_SEQ = FIXField('RptSeq', 83)
    RULE80_A = FIXField('Rule80A', 47)
    SCOPE = FIXField('Scope', 546)
    SECONDARY_CL_ORD_ID = FIXField('SecondaryClOrdID', 526)
    SECONDARY_EXEC_ID = FIXField('SecondaryExecID', 527)
    SECONDARY_ORDER_ID = FIXField('SecondaryOrderID', 198)
    SECURE_DATA = FIXField('SecureData', 91)
    SECURE_DATA_LEN = FIXField('SecureDataLen', 90)
    SECURITY_ALT_ID = FIXField('SecurityAltID', 455)
    SECURITY_ALT_ID_SOURCE = FIXField('SecurityAltIDSource', 456)
    SECURITY_DESC = FIXField('SecurityDesc', 107)
    SECURITY_EXCHANGE = FIXField('SecurityExchange', 207)
    SECURITY_ID = FIXField('SecurityID', 48)
    SECURITY_ID_SOURCE = FIXField('SecurityIDSource', 22)
    SECURITY_LIST_REQUEST_TYPE = FIXField('SecurityListRequestType', 559)
    SECURITY_REQ_ID = FIXField('SecurityReqID', 320)
    SECURITY_REQUEST_RESULT = FIXField('SecurityRequestResult', 560)
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
    SENDING_TIME = FIXField('SendingTime', 52)
    SESSION_REJECT_REASON = FIXField('SessionRejectReason', 373)
    SETTL_BRKR_CODE = FIXField('SettlBrkrCode', 174)
    SETTL_CURR_AMT = FIXField('SettlCurrAmt', 119)
    SETTL_CURR_BID_FX_RATE = FIXField('SettlCurrBidFxRate', 656)
    SETTL_CURR_FX_RATE = FIXField('SettlCurrFxRate', 155)
    SETTL_CURR_FX_RATE_CALC = FIXField('SettlCurrFxRateCalc', 156)
    SETTL_CURR_OFFER_FX_RATE = FIXField('SettlCurrOfferFxRate', 657)
    SETTL_CURRENCY = FIXField('SettlCurrency', 120)
    SETTL_DELIVERY_TYPE = FIXField('SettlDeliveryType', 172)
    SETTL_DEPOSITORY_CODE = FIXField('SettlDepositoryCode', 173)
    SETTL_INST_CODE = FIXField('SettlInstCode', 175)
    SETTL_INST_ID = FIXField('SettlInstID', 162)
    SETTL_INST_MODE = FIXField('SettlInstMode', 160)
    SETTL_INST_REF_ID = FIXField('SettlInstRefID', 214)
    SETTL_INST_SOURCE = FIXField('SettlInstSource', 165)
    SETTL_INST_TRANS_TYPE = FIXField('SettlInstTransType', 163)
    SETTLMNT_TYP = FIXField('SettlmntTyp', 63)
    SIDE = FIXField('Side', 54)
    SIDE_COMPLIANCE_ID = FIXField('SideComplianceID', 659)
    SIDE_VALUE1 = FIXField('SideValue1', 396)
    SIDE_VALUE2 = FIXField('SideValue2', 397)
    SIDE_VALUE_IND = FIXField('SideValueInd', 401)
    SIGNATURE = FIXField('Signature', 89)
    SIGNATURE_LENGTH = FIXField('SignatureLength', 93)
    SOLICITED_FLAG = FIXField('SolicitedFlag', 377)
    SPREAD = FIXField('Spread', 218)
    STAND_INST_DB_ID = FIXField('StandInstDbID', 171)
    STAND_INST_DB_NAME = FIXField('StandInstDbName', 170)
    STAND_INST_DB_TYPE = FIXField('StandInstDbType', 169)
    STATE_OR_PROVINCE_OF_ISSUE = FIXField('StateOrProvinceOfIssue', 471)
    STIPULATION_TYPE = FIXField('StipulationType', 233)
    STIPULATION_VALUE = FIXField('StipulationValue', 234)
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
    TAX_ADVANTAGE_TYPE = FIXField('TaxAdvantageType', 495)
    TEST_MESSAGE_INDICATOR = FIXField('TestMessageIndicator', 464)
    TEST_REQ_ID = FIXField('TestReqID', 112)
    TEXT = FIXField('Text', 58)
    TICK_DIRECTION = FIXField('TickDirection', 274)
    TIME_IN_FORCE = FIXField('TimeInForce', 59)
    TOT_NO_ORDERS = FIXField('TotNoOrders', 68)
    TOT_NO_STRIKES = FIXField('TotNoStrikes', 422)
    TOT_QUOTE_ENTRIES = FIXField('TotQuoteEntries', 304)
    TOTAL_ACCRUED_INTEREST_AMT = FIXField('TotalAccruedInterestAmt', 540)
    TOTAL_AFFECTED_ORDERS = FIXField('TotalAffectedOrders', 533)
    TOTAL_NUM_SECURITIES = FIXField('TotalNumSecurities', 393)
    TOTAL_NUM_SECURITY_TYPES = FIXField('TotalNumSecurityTypes', 557)
    TOTAL_TAKEDOWN = FIXField('TotalTakedown', 237)
    TOTAL_VOLUME_TRADED = FIXField('TotalVolumeTraded', 387)
    TOTAL_VOLUME_TRADED_DATE = FIXField('TotalVolumeTradedDate', 449)
    TOTAL_VOLUME_TRADED_TIME = FIXField('TotalVolumeTradedTime', 450)
    TRAD_SES_CLOSE_TIME = FIXField('TradSesCloseTime', 344)
    TRAD_SES_END_TIME = FIXField('TradSesEndTime', 345)
    TRAD_SES_METHOD = FIXField('TradSesMethod', 338)
    TRAD_SES_MODE = FIXField('TradSesMode', 339)
    TRAD_SES_OPEN_TIME = FIXField('TradSesOpenTime', 342)
    TRAD_SES_PRE_CLOSE_TIME = FIXField('TradSesPreCloseTime', 343)
    TRAD_SES_REQ_ID = FIXField('TradSesReqID', 335)
    TRAD_SES_START_TIME = FIXField('TradSesStartTime', 341)
    TRAD_SES_STATUS = FIXField('TradSesStatus', 340)
    TRAD_SES_STATUS_REJ_REASON = FIXField('TradSesStatusRejReason', 567)
    TRADE_CONDITION = FIXField('TradeCondition', 277)
    TRADE_DATE = FIXField('TradeDate', 75)
    TRADE_INPUT_DEVICE = FIXField('TradeInputDevice', 579)
    TRADE_INPUT_SOURCE = FIXField('TradeInputSource', 578)
    TRADE_ORIGINATION_DATE = FIXField('TradeOriginationDate', 229)
    TRADE_REPORT_ID = FIXField('TradeReportID', 571)
    TRADE_REPORT_REF_ID = FIXField('TradeReportRefID', 572)
    TRADE_REPORT_TRANS_TYPE = FIXField('TradeReportTransType', 487)
    TRADE_REQUEST_ID = FIXField('TradeRequestID', 568)
    TRADE_REQUEST_TYPE = FIXField('TradeRequestType', 569)
    TRADE_TYPE = FIXField('TradeType', 418)
    TRADED_FLAT_SWITCH = FIXField('TradedFlatSwitch', 258)
    TRADING_SESSION_ID = FIXField('TradingSessionID', 336)
    TRADING_SESSION_SUB_ID = FIXField('TradingSessionSubID', 625)
    TRANS_BKD_TIME = FIXField('TransBkdTime', 483)
    TRANSACT_TIME = FIXField('TransactTime', 60)
    URL_LINK = FIXField('URLLink', 149)
    UNDERLYING_CFI_CODE = FIXField('UnderlyingCFICode', 463)
    UNDERLYING_CONTRACT_MULTIPLIER = FIXField('UnderlyingContractMultiplier', 436)
    UNDERLYING_COUNTRY_OF_ISSUE = FIXField('UnderlyingCountryOfIssue', 592)
    UNDERLYING_COUPON_PAYMENT_DATE = FIXField('UnderlyingCouponPaymentDate', 241)
    UNDERLYING_COUPON_RATE = FIXField('UnderlyingCouponRate', 435)
    UNDERLYING_CREDIT_RATING = FIXField('UnderlyingCreditRating', 256)
    UNDERLYING_FACTOR = FIXField('UnderlyingFactor', 246)
    UNDERLYING_INSTR_REGISTRY = FIXField('UnderlyingInstrRegistry', 595)
    UNDERLYING_ISSUE_DATE = FIXField('UnderlyingIssueDate', 242)
    UNDERLYING_ISSUER = FIXField('UnderlyingIssuer', 306)
    UNDERLYING_LAST_PX = FIXField('UnderlyingLastPx', 651)
    UNDERLYING_LAST_QTY = FIXField('UnderlyingLastQty', 652)
    UNDERLYING_LOCALE_OF_ISSUE = FIXField('UnderlyingLocaleOfIssue', 594)
    UNDERLYING_MATURITY_DATE = FIXField('UnderlyingMaturityDate', 542)
    UNDERLYING_MATURITY_MONTH_YEAR = FIXField('UnderlyingMaturityMonthYear', 313)
    UNDERLYING_OPT_ATTRIBUTE = FIXField('UnderlyingOptAttribute', 317)
    UNDERLYING_PRODUCT = FIXField('UnderlyingProduct', 462)
    UNDERLYING_PUT_OR_CALL = FIXField('UnderlyingPutOrCall', 315)
    UNDERLYING_REDEMPTION_DATE = FIXField('UnderlyingRedemptionDate', 247)
    UNDERLYING_REPO_COLLATERAL_SECURITY_TYPE = FIXField('UnderlyingRepoCollateralSecurityType', 243)
    UNDERLYING_REPURCHASE_RATE = FIXField('UnderlyingRepurchaseRate', 245)
    UNDERLYING_REPURCHASE_TERM = FIXField('UnderlyingRepurchaseTerm', 244)
    UNDERLYING_SECURITY_ALT_ID = FIXField('UnderlyingSecurityAltID', 458)
    UNDERLYING_SECURITY_ALT_ID_SOURCE = FIXField('UnderlyingSecurityAltIDSource', 459)
    UNDERLYING_SECURITY_DESC = FIXField('UnderlyingSecurityDesc', 307)
    UNDERLYING_SECURITY_EXCHANGE = FIXField('UnderlyingSecurityExchange', 308)
    UNDERLYING_SECURITY_ID = FIXField('UnderlyingSecurityID', 309)
    UNDERLYING_SECURITY_ID_SOURCE = FIXField('UnderlyingSecurityIDSource', 305)
    UNDERLYING_SECURITY_TYPE = FIXField('UnderlyingSecurityType', 310)
    UNDERLYING_STATE_OR_PROVINCE_OF_ISSUE = FIXField('UnderlyingStateOrProvinceOfIssue', 593)
    UNDERLYING_STRIKE_PRICE = FIXField('UnderlyingStrikePrice', 316)
    UNDERLYING_SYMBOL = FIXField('UnderlyingSymbol', 311)
    UNDERLYING_SYMBOL_SFX = FIXField('UnderlyingSymbolSfx', 312)
    UNSOLICITED_INDICATOR = FIXField('UnsolicitedIndicator', 325)
    URGENCY = FIXField('Urgency', 61)
    USERNAME = FIXField('Username', 553)
    VALID_UNTIL_TIME = FIXField('ValidUntilTime', 62)
    VALUE_OF_FUTURES = FIXField('ValueOfFutures', 408)
    WORKING_INDICATOR = FIXField('WorkingIndicator', 636)
    WT_AVERAGE_LIQUIDITY = FIXField('WtAverageLiquidity', 410)
    XML_DATA = FIXField('XmlData', 213)
    XML_DATA_LEN = FIXField('XmlDataLen', 212)
    YIELD = FIXField('Yield', 236)
    YIELD_TYPE = FIXField('YieldType', 235)


class AccountType(Enum):
    HOUSE_TRADER = '3'
    ACCOUNT_IS_HOUSE_TRADER_AND_IS_CROSS_MARGINED = '7'
    ACCOUNT_IS_CARRIED_ON_NON_CUSTOMER_SIDE_OF_BOOKS_AND_IS_CROSS_MARGINED = '6'
    FLOOR_TRADER = '4'
    ACCOUNT_IS_CARRIED_ON_NON_CUSTOMER_SIDE_OF_BOOKS = '2'
    ACCOUNT_IS_CARRIED_ON_CUSTOMER_SIDE_OF_BOOKS = '1'
    JOINT_BACKOFFICE_ACCOUNT = '8'


class Adjustment(Enum):
    CANCEL = '1'
    ERROR = '2'
    CORRECTION = '3'


class AdvSide(Enum):
    BUY = 'B'
    SELL = 'S'
    CROSS = 'X'
    TRADE = 'T'


class AdvTransType(Enum):
    NEW = 'N'
    CANCEL = 'C'
    REPLACE = 'R'


class AggregatedBook(Enum):
    YES = 'Y'
    NO = 'N'


class AllocHandlInst(Enum):
    FORWARD_AND_MATCH = '3'
    FORWARD = '2'
    MATCH = '1'


class AllocLinkType(Enum):
    F_X_NETTING = '0'
    F_X_SWAP = '1'


class AllocRejCode(Enum):
    UNKNOWN_ACCOUNT = '0'
    UNKNOWN_LISTID = '6'
    UNKNOWN_EXECUTING_BROKER_MNEMONIC = '3'
    UNKNOWN_ORDERID = '5'
    OTHER = '7'
    COMMISSION_DIFFERENCE = '4'
    INCORRECT_QUANTITY = '1'
    INCORRECT_AVERAGE_PRICE = '2'


class AllocStatus(Enum):
    REJECTED = '1'
    PARTIAL_ACCEPT = '2'
    RECEIVED = '3'
    ACCEPTED = '0'


class AllocTransType(Enum):
    CALCULATED_WITHOUT_PRELIMINARY = '5'
    CALCULATED = '4'
    PRELIMINARY = '3'
    CANCEL = '2'
    REPLACE = '1'
    NEW = '0'


class AllocType(Enum):
    BUYSIDE_READY_TO_BOOK_6 = '6'
    BUYSIDE_PRELIMINARY = '2'
    SELLSIDE_CALCULATED_USING_PRELIMINARY = '3'
    BUYSIDE_READY_TO_BOOK_5 = '5'
    BUYSIDE_CALCULATED = '1'
    SELLSIDE_CALCULATED_WITHOUT_PRELIMINARY = '4'


class BasisPxType(Enum):
    VWAP_THROUGH_AN_AFTERNOON_SESSION = '8'
    OPEN = 'D'
    OTHERS = 'Z'
    STRIKE = 'C'
    VWAP_THROUGH_AN_AFTERNOON_SESSION_EXCEPT_YORI = 'B'
    VWAP_THROUGH_A_DAY_EXCEPT_YORI = '9'
    VWAP_THROUGH_A_MORNING_SESSION = '7'
    VWAP_THROUGH_A_DAY = '6'
    SQ = '5'
    CURRENT_PRICE = '4'
    CLOSING_PRICE = '3'
    CLOSING_PRICE_AT_MORNING_SESSION = '2'
    VWAP_THROUGH_A_MORNING_SESSION_EXCEPT_YORI = 'A'


class Benchmark(Enum):
    OLD_10 = '5'
    CURVE = '1'
    FIVE_YR = '2'
    TEN_YR = '4'
    THIRTY_YR = '6'
    OLD_30 = '7'
    THREE_MO_LIBOR = '8'
    SIX_MO_LIBOR = '9'
    OLD_5 = '3'


class BenchmarkCurveName(Enum):
    SWAP = 'SWAP'
    LIBID = 'LIBID'
    OTHER = 'OTHER'
    TREASURY = 'Treasury'
    EURIBOR = 'Euribor'
    PFANDBRIEFE = 'Pfandbriefe'
    FUTURESWAP = 'FutureSWAP'
    MUNIAAA = 'MuniAAA'
    LIBOR = 'LIBOR'


class BidDescriptorType(Enum):
    INDEX = '3'
    COUNTRY = '2'
    SECTOR = '1'


class BidRequestTransType(Enum):
    NEW = 'N'
    CANCEL = 'C'


class BidType(Enum):
    NON_DISCLOSED_STYLE = '1'
    DISCLOSED_STYLE = '2'
    NO_BIDDING_PROCESS = '3'


class BookingUnit(Enum):
    AGGREGATE_PARTIAL_EXECUTIONS_ON_THIS_ORDER_AND_BOOK_ONE_TRADE_PER_ORDER = '1'
    AGGREGATE_EXECUTIONS_FOR_THIS_SYMBOL_SIDE_AND_SETTLEMENT_DATE = '2'
    EACH_PARTIAL_EXECUTION_IS_A_BOOKABLE_UNIT = '0'


class BusinessRejectReason(Enum):
    UNSUPPORTED_MESSAGE_TYPE = '3'
    DELIVERTO_FIRM_NOT_AVAILABLE_AT_THIS_TIME = '7'
    APPLICATION_NOT_AVAILABLE = '4'
    NOT_AUTHORIZED = '6'
    OTHER = '0'
    CONDITIONALLY_REQUIRED_FIELD_MISSING = '5'
    UNKOWN_ID = '1'
    UNKNOWN_SECURITY = '2'


class CancellationRights(Enum):
    NO_WAIVER_AGREEMENT = 'M'
    NO_EXECUTION_ONLY = 'N'
    YES = 'Y'
    NO_INSTITUTIONAL = 'O'


class CashMargin(Enum):
    MARGIN_OPEN = '2'
    MARGIN_CLOSE = '3'
    CASH = '1'


class ClearingFeeIndicator(Enum):
    ONE_HUNDRED_AND_SIX_H_AND_106_J_FIRMS = 'H'
    FIVE_TH_YEAR_DELEGATE_TRADING_FOR_HIS_OWN_ACCOUNT = '5'
    FOUR_TH_YEAR_DELEGATE_TRADING_FOR_HIS_OWN_ACCOUNT = '4'
    THREE_RD_YEAR_DELEGATE_TRADING_FOR_HIS_OWN_ACCOUNT = '3'
    TWO_ND_YEAR_DELEGATE_TRADING_FOR_HIS_OWN_ACCOUNT = '2'
    ONE_ST_YEAR_DELEGATE_TRADING_FOR_HIS_OWN_ACCOUNT = '1'
    ALL_OTHER_OWNERSHIP_TYPES = 'M'
    GIM_IDEM_AND_COM_MEMBERSHIP_INTEREST_HOLDERS = 'I'
    SIX_TH_YEAR_AND_BEYOND_DELEGATE_TRADING_FOR_HIS_OWN_ACCOUNT = '9'
    FULL_AND_ASSOCIATE_MEMBER_TRADING_FOR_OWN_ACCOUNT_AND_AS_FLOOR = 'F'
    EQUITY_MEMBER_AND_CLEARING_MEMBER = 'E'
    NON_MEMBER_AND_CUSTOMER = 'C'
    CBOE_MEMBER = 'B'
    LESSEE_AND_106_F_EMPLOYEES = 'L'


class ClearingInstruction(Enum):
    MANUAL_MODE = '8'
    MULTILATERAL_NETTING = '5'
    AUTOMATIC_POSTING_MODE = '9'
    BILATERAL_NETTING_ONLY = '2'
    CLEAR_AGAINST_CENTRAL_COUNTERPARTY = '6'
    AUTOMATIC_GIVE_UP_MODE = '10'
    SPECIAL_TRADE = '4'
    EX_CLEARING = '3'
    PROCESS_NORMALLY = '0'
    EXCLUDE_FROM_CENTRAL_COUNTERPARTY = '7'
    EXCLUDE_FROM_ALL_NETTING = '1'


class CommType(Enum):
    PER_BOND = '6'
    PER_SHARE = '1'
    PERCENTAGE = '2'
    ABSOLUTE = '3'
    FIVE = '5'
    FOUR = '4'


class ContAmtType(Enum):
    NET_SETTLEMENT_AMOUNT = '15'
    COMMISSION_AMOUNT = '1'
    COMMISSION = '2'
    INITIAL_CHARGE_AMOUNT = '3'
    INITIAL_CHARGE = '4'
    DISCOUNT_AMOUNT = '5'
    DISCOUNT = '6'
    DILUTION_LEVY_AMOUNT = '7'
    DILUTION_LEVY = '8'
    EXIT_CHARGE_AMOUNT = '9'
    EXIT_CHARGE = '10'
    FUND_BASED_RENEWAL_COMMISSION = '11'
    PROJECTED_FUND_VALUE = '12'
    FUND_BASED_RENEWAL_COMMISSION_AMOUNT_14 = '14'
    FUND_BASED_RENEWAL_COMMISSION_AMOUNT_13 = '13'


class CorporateAction(Enum):
    EX_DISTRIBUTION = 'B'
    EX_INTEREST = 'E'
    EX_RIGHTS = 'C'
    EX_DIVIDEND = 'A'
    NEW = 'D'


class CoveredOrUncovered(Enum):
    UNCOVERED = '1'
    COVERED = '0'


class CrossPrioritization(Enum):
    SELLSIDE_PRIORITIZED = '2'
    NONE = '0'
    BUYSIDE_PRIORITIZED = '1'


class CrossType(Enum):
    CROSS_TRADE_WHICH_IS_EXECUTED_COMPLETELY_OR_NOT_BOTH_SIDES_ARE_TREATED_IN_THE_SAME_MANNER_THIS_IS_EQUIVALENT_TO_AN_ALL_OR_NONE = '1'
    CROSS_TRADE_WHICH_IS_EXECUTED_PARTIALLY_AND_THE_REST_IS_CANCELLED_ONE_SIDE_IS_FULLY_EXECUTED_THE_OTHER_SIDE_IS_PARTIALLY_EXECUTED_WITH_THE_REMAINDER_BEING_CANCELLED_THIS_IS_EQUIVALENT_TO_AN_IMMEDIATE_OR_CANCEL_ON_THE_OTHER_SIDE = '2'
    CROSS_TRADE_WHICH_IS_PARTIALLY_EXECUTED_WITH_THE_UNFILLED_PORTIONS_REMAINING_ACTIVE_ONE_SIDE_OF_THE_CROSS_IS_FULLY_EXECUTED = '3'
    CROSS_TRADE_IS_EXECUTED_WITH_EXISTING_ORDERS_WITH_THE_SAME_PRICE = '4'


class CxlRejReason(Enum):
    UNKNOWN_ORDER = '1'
    TOO_LATE_TO_CANCEL = '0'
    DUPLICATE_CLORDID_RECEIVED = '6'
    ORIGORDMODTIME_DID_NOT_MATCH_LAST_TRANSACTTIME_OF_ORDER = '5'
    UNABLE_TO_PROCESS_ORDER_MASS_CANCEL_REQUEST = '4'
    ORDER_ALREADY_IN_PENDING_CANCEL_OR_PENDING_REPLACE_STATUS = '3'
    BROKER = '2'


class CxlRejResponseTo(Enum):
    ORDER_CANCEL_REPLACE_REQUEST = '2'
    ORDER_CANCEL_REQUEST = '1'


class DKReason(Enum):
    WRONG_SIDE = 'B'
    QUANTITY_EXCEEDS_ORDER = 'C'
    NO_MATCHING_ORDER = 'D'
    PRICE_EXCEEDS_LIMIT = 'E'
    OTHER = 'Z'
    UNKNOWN_SYMBOL = 'A'


class DayBookingInst(Enum):
    CAN_TRIGGER_BOOKING_WITHOUT_REFERENCE_TO_THE_ORDER_INITIATOR = '0'
    SPEAK_WITH_ORDER_INITIATOR_BEFORE_BOOKING = '1'


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
    YES = 'Y'
    NO = 'N'


class EmailType(Enum):
    NEW = '0'
    REPLY = '1'
    ADMIN_REPLY = '2'


class EncryptMethod(Enum):
    DES = '2'
    PEM_DES_MD5 = '6'
    PGP_DES_MD5 = '5'
    PKCS_DES = '3'
    NONE = '0'
    PKCS = '1'
    PGP_DES = '4'


class ExchangeForPhysical(Enum):
    NO = 'N'
    YES = 'Y'


class ExecInst(Enum):
    TRYTOSTOP = 'Y'
    MIDPRCPEG = 'M'
    MARKPEG = 'P'
    CANCELONSYSFAIL = 'Q'
    PRIMPEG = 'R'
    SUSPEND = 'S'
    CUSTDISPINST = 'U'
    NETTING = 'V'
    PEGVWAP = 'W'
    TRADEALONG = 'X'
    PERCVOL = 'D'
    STAYOFFER = '0'
    WORK = '2'
    OVERDAY = '4'
    HELD = '5'
    PARTNOTINIT = '6'
    STRICTSCALE = '7'
    TRYTOSCALE = '8'
    STAYBID = '9'
    NOCROSS = 'A'
    OPENPEG = 'O'
    CALLFIRST = 'C'
    NONNEGO = 'N'
    DNI = 'E'
    DNR = 'F'
    AON = 'G'
    RESTATEONSYSFAIL = 'H'
    INSTITONLY = 'I'
    RESTATEONTRADINGHALT = 'J'
    CANCELONTRADINGHALT = 'K'
    LASTPEG = 'L'
    GOALONG = '3'
    OKCROSS = 'B'
    NOTHELD = '1'


class ExecPriceType(Enum):
    SINGLE_PRICE = 'S'
    OFFER_PRICE_MINUS_ADJUSTMENT_AMOUNT = 'Q'
    OFFER_PRICE_MINUS_ADJUSTMENT = 'P'
    OFFER_PRICE = 'O'
    CREATION_PRICE_PLUS_ADJUSTMENT_AMOUNT = 'E'
    CREATION_PRICE_PLUS_ADJUSTMENT = 'D'
    CREATION_PRICE = 'C'
    BID_PRICE = 'B'


class ExecRestatementReason(Enum):
    CANCEL_ON_SYSTEM_FAILURE = '7'
    GT_CORPORATE_ACTION = '0'
    MARKET = '8'
    CANCEL_ON_TRADING_HALT = '6'
    PARTIAL_DECLINE_OF_ORDERQTY = '5'
    BROKER_OPTION = '4'
    REPRICING_OF_ORDER = '3'
    GT_RENEWAL = '1'
    VERBAL_CHANGE = '2'


class ExecType(Enum):
    PENDING_CANCEL = '6'
    NEW = '0'
    PARTIAL_FILL = '1'
    FILL = '2'
    CANCELED = '4'
    REPLACE = '5'
    REJECTED = '8'
    SUSPENDED = '9'
    PENDING_NEW = 'A'
    CALCULATED = 'B'
    EXPIRED = 'C'
    RESTATED = 'D'
    PENDING_REPLACE = 'E'
    TRADE = 'F'
    TRADE_CORRECT = 'G'
    TRADE_CANCEL = 'H'
    ORDER_STATUS = 'I'
    DONE_FOR_DAY = '3'
    STOPPED = '7'


class FinancialStatus(Enum):
    BANKRUPT = '1'
    PENDING_DELISTING = '2'


class ForexReq(Enum):
    YES = 'Y'
    NO = 'N'


class FundRenewWaiv(Enum):
    NO = 'N'
    YES = 'Y'


class GTBookingInst(Enum):
    BOOK_OUT_ALL_TRADES_ON_DAY_OF_EXECUTION = '0'
    ACCUMULATE_UNTIL_VERBALLY_NOTIFIED_OTHERWISE = '2'
    ACCUMULATE_EXECUTIONS_UNTIL_ORDER_IS_FILLED_OR_EXPIRES = '1'


class GapFillFlag(Enum):
    YES = 'Y'
    NO = 'N'


class HaltReasonChar(Enum):
    EQUIPMENT_CHANGEOVER = 'X'
    ADDITIONAL_INFORMATION = 'M'
    ORDER_INFLUX = 'E'
    NEWS_PENDING = 'P'
    ORDER_IMBALANCE = 'I'
    NEWS_DISSEMINATION = 'D'


class HandlInst(Enum):
    AUTOMATED_EXECUTION_ORDER_PRIVATE_NO_BROKER_INTERVENTION = '1'
    AUTOMATED_EXECUTION_ORDER_PUBLIC_BROKER_INTERVENTION_OK = '2'
    MANUAL_ORDER_BEST_EXECUTION = '3'


class IOINaturalFlag(Enum):
    YES = 'Y'
    NO = 'N'


class IOIQltyInd(Enum):
    MEDIUM = 'M'
    HIGH = 'H'
    LOW = 'L'


class IOIQty(Enum):
    LARGE = 'L'
    MEDIUM = 'M'
    SMALL = 'S'


class IOIQualifier(Enum):
    AT_THE_OPEN = 'O'
    CROSSING_OPPORTUNITY = 'X'
    INDICATION = 'W'
    VERSUS = 'V'
    THROUGH_THE_DAY = 'T'
    PORTFOLIO_SHOWN = 'S'
    READY_TO_TRADE = 'R'
    ALL_OR_NONE = 'A'
    TAKING_A_POSITION = 'P'
    MORE_BEHIND = 'M'
    LIMIT = 'L'
    IN_TOUCH_WITH = 'I'
    VWAP = 'D'
    AT_THE_CLOSE = 'C'
    MARKET_ON_CLOSE = 'B'
    AT_THE_MARKET = 'Q'
    AT_THE_MIDPOINT = 'Y'
    PRE_OPEN = 'Z'


class IOITransType(Enum):
    CANCEL = 'C'
    NEW = 'N'
    REPLACE = 'R'


class InViewOfCommon(Enum):
    YES = 'Y'
    NO = 'N'


class IncTaxInd(Enum):
    GROSS = '2'
    NET = '1'


class LastCapacity(Enum):
    PRINCIPAL = '4'
    CROSS_AS_PRINCIPAL = '3'
    AGENT = '1'
    CROSS_AS_AGENT = '2'


class LegalConfirm(Enum):
    YES = 'Y'
    NO = 'N'


class LiquidityIndType(Enum):
    NORMAL_MARKET_SIZE = '3'
    OTHER = '4'
    TWENTY_DAY_MOVING_AVERAGE = '2'
    FIVE_DAY_MOVING_AVERAGE = '1'


class ListExecInstType(Enum):
    EXCHANGE_SWITCH_CIV_ORDER_BUY_DRIVEN_CASH_WITHDRAW = '5'
    EXCHANGE_SWITCH_CIV_ORDER_BUY_DRIVEN_CASH_TOP_UP = '4'
    WAIT_FOR_EXECUTE_INSTRUCTION = '2'
    IMMEDIATE = '1'
    EXCHANGE_SWITCH_CIV_ORDER_SELL_DRIVEN = '3'


class ListOrderStatus(Enum):
    CANCELING = '4'
    EXECUTING = '3'
    REJECT = '7'
    ALL_DONE = '6'
    ALERT = '5'
    RECEIVEDFOREXECUTION = '2'
    INBIDDINGPROCESS = '1'


class ListStatusType(Enum):
    ALERT = '6'
    EXECSTARTED = '4'
    TIMED = '3'
    RESPONSE = '2'
    ACK = '1'
    ALLDONE = '5'


class LocateReqd(Enum):
    YES = 'Y'
    NO = 'N'


class MDEntryType(Enum):
    TRADING_SESSION_HIGH_PRICE = '7'
    OFFER = '1'
    IMBALANCE = 'A'
    TRADING_SESSION_VWAP_PRICE = '9'
    TRADING_SESSION_LOW_PRICE = '8'
    CLOSING_PRICE = '5'
    OPENING_PRICE = '4'
    BID = '0'
    TRADE = '2'
    INDEX_VALUE = '3'
    SETTLEMENT_PRICE = '6'


class MDImplicitDelete(Enum):
    YES = 'Y'
    NO = 'N'


class MDReqRejReason(Enum):
    UNSUPPORTED_AGGREGATEDBOOK = '7'
    DUPLICATE_MDREQID = '1'
    UNSUPPORTED_MDIMPLICITDELETE = 'C'
    UNSUPPORTED_OPENCLOSESETTLEFLAG = 'B'
    UNSUPPORTED_SCOPE = 'A'
    UNSUPPORTED_TRADINGSESSIONID = '9'
    UNSUPPORTED_MDENTRYTYPE = '8'
    UNSUPPORTED_MDUPDATETYPE = '6'
    UNSUPPORTED_MARKETDEPTH = '5'
    UNSUPPORTED_SUBSCRIPTIONREQUESTTYPE = '4'
    INSUFFICIENT_BANDWIDTH = '2'
    UNKNOWN_SYMBOL = '0'
    INSUFFICIENT_PERMISSIONS = '3'


class MDUpdateAction(Enum):
    NEW = '0'
    CHANGE = '1'
    DELETE = '2'


class MDUpdateType(Enum):
    FULL_REFRESH = '0'
    INCREMENTAL_REFRESH = '1'


class MassCancelRejectReason(Enum):
    INVALID_OR_UNKNOWN_UNDERLYING = '2'
    INVALID_OR_UNKNOWN_TRADING_SESSION = '6'
    INVALID_OR_UNKNOWN_SECURITY_TYPE = '5'
    INVALID_OR_UNKNOWN_PRODUCT = '3'
    INVALID_OR_UNKNOWN_SECURITY = '1'
    MASS_CANCEL_NOT_SUPPORTED = '0'
    INVALID_OR_UNKNOWN_CFICODE = '4'


class MassCancelRequestType(Enum):
    CANCEL_ORDERS_FOR_A_SECURITY = '1'
    CANCEL_ALL_ORDERS = '7'
    CANCEL_ORDERS_FOR_A_TRADING_SESSION = '6'
    CANCEL_ORDERS_FOR_A_SECURITYTYPE = '5'
    CANCEL_ORDERS_FOR_A_CFICODE = '4'
    CANCEL_ORDERS_FOR_AN_UNDERLYING_SECURITY = '2'
    CANCEL_ORDERS_FOR_A_PRODUCT = '3'


class MassCancelResponse(Enum):
    CANCEL_ORDERS_FOR_A_TRADING_SESSION = '6'
    CANCEL_REQUEST_REJECTED = '0'
    CANCEL_ALL_ORDERS = '7'
    CANCEL_ORDERS_FOR_A_PRODUCT = '3'
    CANCEL_ORDERS_FOR_A_SECURITYTYPE = '5'
    CANCEL_ORDERS_FOR_A_CFICODE = '4'
    CANCEL_ORDERS_FOR_A_SECURITY = '1'
    CANCEL_ORDERS_FOR_AN_UNDERLYING_SECURITY = '2'


class MassStatusReqType(Enum):
    STATUS_FOR_ORDERS_FOR_A_SECURITY = '1'
    STATUS_FOR_ORDERS_FOR_AN_UNDERLYING_SECURITY = '2'
    STATUS_FOR_ORDERS_FOR_A_PRODUCT = '3'
    STATUS_FOR_ORDERS_FOR_A_CFICODE = '4'
    STATUS_FOR_ORDERS_FOR_A_SECURITYTYPE = '5'
    STATUS_FOR_ORDERS_FOR_A_TRADING_SESSION = '6'
    STATUS_FOR_ORDERS_FOR_A_PARTYID = '8'
    STATUS_FOR_ALL_ORDERS = '7'


class MatchStatus(Enum):
    COMPARED_MATCHED_OR_AFFIRMED = '0'
    UNCOMPARED_UNMATCHED_OR_UNAFFIRMED = '1'
    ADVISORY_OR_ALERT = '2'


class MatchType(Enum):
    SUMMARIZED_MATCH_USING_A1_TO_A5_EXACT_MATCH_CRITERIA_EXCEPT_QUANTITY_IS_SUMMARIZED_S5 = 'S5'
    ACT_M1_MATCH = 'M1'
    ACT_M6_MATCH = 'M6'
    ACT_DEFAULT_AFTER_M2 = 'M5'
    ACT_ACCEPTED_TRADE = 'M3'
    SUMMARIZED_MATCH_USING_A1_TO_A5_EXACT_MATCH_CRITERIA_EXCEPT_QUANTITY_IS_SUMMARIZED_S2 = 'S2'
    SUMMARIZED_MATCH_USING_A1_TO_A5_EXACT_MATCH_CRITERIA_EXCEPT_QUANTITY_IS_SUMMARIZED_S3 = 'S3'
    SUMMARIZED_MATCH_USING_A1_TO_A5_EXACT_MATCH_CRITERIA_EXCEPT_QUANTITY_IS_SUMMARIZED_S4 = 'S4'
    ACT_M2_MATCH = 'M2'
    EXACT_MATCH_ON_TRADE_DATE_STOCK_SYMBOL_QUANTITY_PRICE_TRADE_TYPE_AND_SPECIAL_TRADE_INDICATOR_PLUS_FOUR_BADGES = 'A2'
    EXACT_MATCH_ON_TRADE_DATE_STOCK_SYMBOL_QUANTITY_PRICE_TRADE_TYPE_AND_SPECIAL_TRADE_INDICATOR_PLUS_TWO_BADGES_AND_EXECUTION_TIME = 'A3'
    EXACT_MATCH_ON_TRADE_DATE_STOCK_SYMBOL_QUANTITY_PRICE_TRADE_TYPE_AND = 'A4'
    COMPARED_RECORDS_RESULTING_FROM_STAMPED_ADVISORIES_OR_SPECIALIST = 'AQ'
    NON_ACT = 'MT'
    ACT_DEFAULT_TRADE = 'M4'
    EXACT_MATCH_ON_TRADE_DATE_STOCK_SYMBOL_QUANTITY_PRICE_TRADE_TYPE_AND_SPECIAL_TRADE_INDICATOR_PLUS_FOUR_BADGES_AND_EXECUTION_TIME = 'A1'
    SUMMARIZED_MATCH_USING_A1_TO_A5_EXACT_MATCH_CRITERIA_EXCEPT_QUANTITY_IS_SUMMARIZED_S1 = 'S1'
    EXACT_MATCH_ON_TRADE_DATE_STOCK_SYMBOL_QUANTITY_PRICE_TRADE_TYPE_AND_SPECIAL_TRADE_INDICATOR_PLUS_EXECUTION_TIME = 'A5'


class MessageEncoding(Enum):
    UTF_8 = 'UTF-8'
    ISO_2022_JP = 'ISO-2022-JP'
    EUC_JP = 'EUC-JP'
    SHIFT_JIS = 'SHIFT_JIS'


class MiscFeeType(Enum):
    LOCAL_COMMISSION = '3'
    EXCHANGE_FEES = '4'
    STAMP = '5'
    LEVY = '6'
    OTHER = '7'
    MARKUP = '8'
    CONSUMPTION_TAX = '9'
    REGULATORY = '1'
    TAX = '2'


class MoneyLaunderingStatus(Enum):
    EXEMPT_AUTHORISED_CREDIT_OR_FINANCIAL_INSTITUTION = '3'
    EXEMPT_CLIENT_MONEY_TYPE_EXEMPTION = '2'
    EXEMPT_BELOW_THE_LIMIT = '1'
    PASSED = 'Y'
    NOT_CHECKED = 'N'


class MsgDirection(Enum):
    SEND = 'S'
    RECEIVE = 'R'


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
    DERIVATIVE_SECURITY_LIST = 'AA'
    NEW_ORDER_AB = 'AB'
    MULTILEG_ORDER_CANCEL_REPLACE = 'AC'
    TRADE_CAPTURE_REPORT_REQUEST = 'AD'
    TRADE_CAPTURE_REPORT = 'AE'
    ORDER_MASS_STATUS_REQUEST = 'AF'
    QUOTE_REQUEST_REJECT = 'AG'
    RFQ_REQUEST = 'AH'
    QUOTE_STATUS_REPORT = 'AI'
    MASS_QUOTE_ACKNOWLEDGEMENT = 'b'
    NEWS = 'B'
    SECURITY_DEFINITION_REQUEST = 'c'
    EMAIL = 'C'
    SECURITY_DEFINITION = 'd'
    ORDER_SINGLE = 'D'
    SECURITY_STATUS_REQUEST = 'e'
    ORDER_LIST = 'E'
    SECURITY_STATUS = 'f'
    ORDER_CANCEL_REQUEST = 'F'
    ORDER_CANCEL_REPLACE_REQUEST = 'G'
    TRADING_SESSION_STATUS_REQUEST = 'g'
    TRADING_SESSION_STATUS = 'h'
    ORDER_STATUS_REQUEST = 'H'
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
    XML_MESSAGE = 'n'
    REGISTRATION_INSTRUCTIONS = 'o'
    ALLOCATION_ACK = 'P'
    REGISTRATION_INSTRUCTIONS_RESPONSE = 'p'
    ORDER_MASS_CANCEL_REQUEST = 'q'
    DONT_KNOW_TRADE = 'Q'
    ORDER_MASS_CANCEL_REPORT = 'r'
    QUOTE_REQUEST = 'R'
    NEW_ORDER_S = 's'
    QUOTE = 'S'
    CROSS_ORDER_CANCEL_REPLACE_REQUEST = 't'
    SETTLEMENT_INSTRUCTIONS = 'T'
    CROSS_ORDER_CANCEL_REQUEST = 'u'
    SECURITY_TYPE_REQUEST = 'v'
    MARKET_DATA_REQUEST = 'V'
    SECURITY_TYPES = 'w'
    MARKET_DATA_SNAPSHOT_FULL_REFRESH = 'W'
    SECURITY_LIST_REQUEST = 'x'
    MARKET_DATA_INCREMENTAL_REFRESH = 'X'
    SECURITY_LIST = 'y'
    MARKET_DATA_REQUEST_REJECT = 'Y'
    DERIVATIVE_SECURITY_LIST_REQUEST = 'z'
    QUOTE_CANCEL = 'Z'


class MultiLegReportingType(Enum):
    SINGLE_SECURITY = '1'
    INDIVIDUAL_LEG_OF_A_MULTI_LEG_SECURITY = '2'
    MULTI_LEG_SECURITY = '3'


class NetGrossInd(Enum):
    NET = '1'
    GROSS = '2'


class NoSides(Enum):
    ONE_SIDE = '1'
    BOTH_SIDES = '2'


class NotifyBrokerOfCredit(Enum):
    NO = 'N'
    YES = 'Y'


class OpenCloseSettleFlag(Enum):
    SESSION_OPEN = '1'
    DELIVERY_SETTLEMENT_PRICE = '2'
    EXPECTED_PRICE = '3'
    PRICE_FROM_PREVIOUS_BUSINESS_DAY = '4'
    DAILY_OPEN = '0'


class OrdRejReason(Enum):
    EXCHANGE_CLOSED = '2'
    UNKNOWN_SYMBOL = '1'
    ORDER_EXCEEDS_LIMIT = '3'
    TOO_LATE_TO_ENTER = '4'
    UNKNOWN_ORDER = '5'
    DUPLICATE_OF_A_VERBALLY_COMMUNICATED_ORDER = '7'
    TRADE_ALONG_REQUIRED = '9'
    INVALID_INVESTOR_ID = '10'
    DUPLICATE_ORDER = '6'
    UNSUPPORTED_ORDER_CHARACTERISTIC = '11'
    SURVEILLENCE_OPTION = '12'
    BROKER = '0'
    STALE_ORDER = '8'


class OrdStatus(Enum):
    NEW = '0'
    PARTIALLY_FILLED = '1'
    REPLACED = '5'
    FILLED = '2'
    PENDING_CANCEL = '6'
    STOPPED = '7'
    REJECTED = '8'
    SUSPENDED = '9'
    PENDING_NEW = 'A'
    CALCULATED = 'B'
    EXPIRED = 'C'
    ACCEPTED_FOR_BIDDING = 'D'
    PENDING_REPLACE = 'E'
    DONE_FOR_DAY = '3'
    CANCELED = '4'


class OrdType(Enum):
    PREVIOUSLY_QUOTED = 'D'
    LIMIT = '2'
    STOP = '3'
    STOP_LIMIT = '4'
    MARKET_ON_CLOSE = '5'
    WITH_OR_WITHOUT = '6'
    LIMIT_OR_BETTER = '7'
    LIMIT_WITH_OR_WITHOUT = '8'
    ON_BASIS = '9'
    ON_CLOSE = 'A'
    MARKET = '1'
    FOREX_C = 'C'
    FOREX_F = 'F'
    PREVIOUSLY_INDICATED = 'E'
    FOREX_G = 'G'
    FUNARI = 'I'
    MARKET_IF_TOUCHED = 'J'
    MARKET_WITH_LEFTOVER_AS_LIMIT = 'K'
    PREVIOUS_FUND_VALUATION_POINT = 'L'
    NEXT_FUND_VALUATION_POINT = 'M'
    PEGGED = 'P'
    LIMIT_ON_CLOSE = 'B'
    FOREX_H = 'H'


class OrderCapacity(Enum):
    RISKLESS_PRINCIPAL = 'R'
    INDIVIDUAL = 'I'
    PRINCIPAL = 'P'
    AGENT_FOR_OTHER_MEMBER = 'W'
    AGENCY = 'A'
    PROPRIETARY = 'G'


class OrderRestrictions(Enum):
    FOREIGN_ENTITY = '7'
    RISKLESS_ARBITRAGE = 'A'
    PROGRAM_TRADE = '1'
    EXTERNAL_MARKET_PARTICIPANT = '8'
    ACTING_AS_MARKET_MAKER_OR_SPECIALIST_IN_THE_UNDERLYING_SECURITY_OF_A_DERIVATIVE_SECURITY = '6'
    ACTING_AS_MARKET_MAKER_OR_SPECIALIST_IN_THE_SECURITY = '5'
    NON_INDEX_ARBITRAGE = '3'
    INDEX_ARBITRAGE = '2'
    COMPETING_MARKET_MAKER = '4'
    EXTERNAL_INTER_CONNECTED_MARKET_LINKAGE = '9'


class OwnerType(Enum):
    COMPANY_TRUSTEE = '5'
    NOMINEE = '13'
    CORPORATE_BODY = '12'
    NON_PROFIT_ORGANIZATION = '11'
    NETWORKING_SUB_ACCOUNT = '10'
    FIDUCIARIES = '9'
    TRUSTS = '8'
    PENSION_PLAN = '6'
    INDIVIDUAL_TRUSTEE = '4'
    PUBLIC_COMPANY = '2'
    PRIVATE_COMPANY = '3'
    INDIVIDUAL_INVESTOR = '1'
    CUSTODIAN_UNDER_GIFTS_TO_MINORS_ACT = '7'


class PartyIDSource(Enum):
    CHINESE_B_SHARE = '5'
    US_EMPLOYER_IDENTIFICATION_NUMBER = '8'
    AUSTRALIAN_TAX_FILE_NUMBER = 'A'
    AUSTRALIAN_BUSINESS_NUMBER = '9'
    ISO_COUNTRY_CODE = 'E'
    BIC = 'B'
    US_SOCIAL_SECURITY_NUMBER = '7'
    PROPRIETARY_CUSTOM_CODE = 'D'
    SETTLEMENT_ENTITY_LOCATION = 'F'
    KOREAN_INVESTOR_ID = '1'
    TAIWANESE_QUALIFIED_FOREIGN_INVESTOR_ID_QFII = '2'
    TAIWANESE_TRADING_ACCOUNT = '3'
    MALAYSIAN_CENTRAL_DEPOSITORY = '4'
    UK_NATIONAL_INSURANCE_OR_PENSION_NUMBER = '6'
    GENERALLY_ACCEPTED_MARKET_PARTICIPANT_IDENTIFIER = 'C'


class PartyRole(Enum):
    CORRESPONDANT_CLEARING_FIRM = '15'
    CLIENT_ID = '3'
    UNDERLYING_CONTRA_FIRM = '20'
    SPONSORING_FIRM = '19'
    CONTRA_CLEARING_FIRM = '18'
    CONTRA_FIRM = '17'
    EXECUTING_SYSTEM = '16'
    ENTERING_FIRM = '7'
    EXECUTING_FIRM = '1'
    BROKER_OF_CREDIT = '2'
    INVESTOR_ID = '5'
    INTRODUCING_FIRM = '6'
    GIVEUP_CLEARING_FIRM = '14'
    LOCATE_LENDING_FIRM = '8'
    FUND_MANAGER_CLIENT_ID = '9'
    SETTLEMENT_LOCATION = '10'
    ORDER_ORIGINATION_TRADER = '11'
    EXECUTING_TRADER = '12'
    ORDER_ORIGINATION_FIRM = '13'
    CLEARING_FIRM = '4'


class PaymentMethod(Enum):
    BPAY = '14'
    ACH_CREDIT = '13'
    ACH_DEBIT = '12'
    CREDIT_CARD = '11'
    DIRECT_CREDIT = '10'
    DIRECT_DEBIT = '9'
    DEBIT_CARD = '8'
    FEDWIRE = '7'
    HIGH_VALUE_CLEARING_SYSTEM = '15'
    EUROCLEAR = '3'
    TELEGRAPHIC_TRANSFER = '6'
    CLEARSTREAM = '4'
    CREST = '1'
    NSCC = '2'
    CHEQUE = '5'


class PositionEffect(Enum):
    FIFO = 'F'
    ROLLED = 'R'
    CLOSE = 'C'
    OPEN = 'O'


class PossDupFlag(Enum):
    NO = 'N'
    YES = 'Y'


class PossResend(Enum):
    NO = 'N'
    YES = 'Y'


class PreallocMethod(Enum):
    PRO_RATA = '0'
    DO_NOT_PRO_RATA_DISCUSS_FIRST = '1'


class PreviouslyReported(Enum):
    NO = 'N'
    YES = 'Y'


class PriceType(Enum):
    FIXED_AMOUNT = '3'
    PERCENTAGE = '1'
    DISCOUNT = '4'
    BASIS_POINTS_RELATIVE_TO_BENCHMARK = '6'
    TED_PRICE = '7'
    TED_YIELD = '8'
    PREMIUM = '5'
    PER_SHARE = '2'


class PriorityIndicator(Enum):
    PRIORITY_UNCHANGED = '0'
    LOST_PRIORITY_AS_RESULT_OF_ORDER_CHANGE = '1'


class ProcessCode(Enum):
    PLAN_SPONSOR = '6'
    REGULAR = '0'
    SOFT_DOLLAR = '1'
    STEP_IN = '2'
    STEP_OUT = '3'
    SOFT_DOLLAR_STEP_IN = '4'
    SOFT_DOLLAR_STEP_OUT = '5'


class Product(Enum):
    LOAN = '8'
    OTHER = '12'
    MUNICIPAL = '11'
    AGENCY = '1'
    CORPORATE = '3'
    CURRENCY = '4'
    COMMODITY = '2'
    GOVERNMENT = '6'
    MORTGAGE = '10'
    INDEX = '7'
    MONEYMARKET = '9'
    EQUITY = '5'


class ProgRptReqs(Enum):
    REAL_TIME_EXECUTION_REPORTS = '3'
    SELLSIDE_PERIODICALLY_SENDS_STATUS_USING_LISTSTATUS_PERIOD_OPTIONALLY_SPECIFIED_IN_PROGRESSPERIOD = '2'
    BUYSIDE_EXPLICITLY_REQUESTS_STATUS_USING_STATUSREQUEST = '1'


class QuantityType(Enum):
    CONTRACTS = '6'
    OTHER = '7'
    CURRENCY = '5'
    ORIGINALFACE = '4'
    CURRENTFACE = '3'
    BONDS = '2'
    SHARES = '1'
    PAR = '8'


class QuoteCancelType(Enum):
    CANCEL_ALL_QUOTES = '4'
    CANCEL_FOR_SECURITY_TYPE = '2'
    CANCEL_FOR_SYMBOL = '1'
    CANCEL_FOR_UNDERLYING_SYMBOL = '3'


class QuoteCondition(Enum):
    LOCKED = 'E'
    NON_FIRM = 'I'
    FAST_TRADING = 'H'
    CROSSED = 'F'
    CONSOLIDATED_BEST = 'D'
    EXCHANGE_BEST = 'C'
    CLOSED = 'B'
    OPEN = 'A'
    DEPTH = 'G'


class QuoteRejectReason(Enum):
    NOT_AUTHORIZED_TO_QUOTE_SECURITY = '9'
    UNKNOWN_SYMBOL = '1'
    EXCHANGE = '2'
    QUOTE_REQUEST_EXCEEDS_LIMIT = '3'
    TOO_LATE_TO_ENTER = '4'
    UNKNOWN_QUOTE = '5'
    DUPLICATE_QUOTE = '6'
    INVALID_BID_ASK_SPREAD = '7'
    INVALID_PRICE = '8'


class QuoteRequestRejectReason(Enum):
    UNKNOWN_SYMBOL = '1'
    EXCHANGE = '2'
    QUOTE_REQUEST_EXCEEDS_LIMIT = '3'
    TOO_LATE_TO_ENTER = '4'
    INVALID_PRICE = '5'
    NOT_AUTHORIZED_TO_REQUEST_QUOTE = '6'


class QuoteRequestType(Enum):
    AUTOMATIC = '2'
    MANUAL = '1'


class QuoteResponseLevel(Enum):
    ACKNOWLEDGE_ONLY_NEGATIVE_OR_ERRONEOUS_QUOTES = '1'
    NO_ACKNOWLEDGEMENT = '0'
    ACKNOWLEDGE_EACH_QUOTE_MESSAGES = '2'


class QuoteStatus(Enum):
    REMOVED_FROM_MARKET = '6'
    CANCELED_FOR_SYMBOL = '1'
    PENDING = '10'
    QUOTE_NOT_FOUND = '9'
    QUERY = '8'
    EXPIRED = '7'
    REJECTED = '5'
    CANCELED_ALL = '4'
    CANCELED_FOR_UNDERLYING = '3'
    CANCELED_FOR_SECURITY_TYPE = '2'
    ACCEPTED = '0'


class QuoteType(Enum):
    INDICATIVE = '0'
    TRADEABLE = '1'
    RESTRICTED_TRADEABLE = '2'


class RegistRejReasonCode(Enum):
    INVALID_UNACCEPTABLE_NODISTRIBINSTNS = '13'
    INVALID_UNACCEPTABLE_CASH_DISTRIB_AGENT_CODE = '17'
    INVALID_UNACCEPTABLE_CASH_DISTRIB_AGENT_ACCT_NAME = '16'
    INVALID_UNACCEPTABLE_NO_REG_DETLS = '4'
    INVALID_UNACCEPTABLE_DISTRIB_PAYMENT_METHOD = '15'
    INVALID_UNACCEPTABLE_DISTRIB_PERCENTAGE = '14'
    INVALID_UNACCEPTABLE_OWNERSHIP_TYPE = '3'
    INVALID_UNACCEPTABLE_TAX_EXEMPT_TYPE = '2'
    INVALID_UNACCEPTABLE_INVESTOR_COUNTRY_OF_RESIDENCE = '12'
    INVALID_UNACCEPTABLE_DATE_OF_BIRTH = '11'
    INVALID_UNACCEPTABLE_INVESTOR_ID_SOURCE = '10'
    INVALID_UNACCEPTABLE_INVESTOR_ID = '9'
    INVALID_UNACCEPTABLE_MAILING_INST = '8'
    INVALID_UNACCEPTABLE_MAILING_DTLS = '7'
    INVALID_UNACCEPTABLE_REG_SEQ_NO = '5'
    INVALID_UNACCEPTABLE_ACCOUNT_TYPE = '1'
    INVALID_UNACCEPTABLE_CASH_DISTRIB_AGENT_ACCT_NUM = '18'
    INVALID_UNACCEPTABLE_REG_DTLS = '6'


class RegistStatus(Enum):
    ACCEPT = 'A'
    REMINDER = 'N'
    REJECT = 'R'
    HELD = 'H'


class RegistTransType(Enum):
    CANCEL = '2'
    NEW = '0'
    REPLACE = '1'


class ReportToExch(Enum):
    YES = 'Y'
    NO = 'N'


class ResetSeqNumFlag(Enum):
    YES = 'Y'
    NO = 'N'


class RoundingDirection(Enum):
    ROUND_TO_NEAREST = '0'
    ROUND_DOWN = '1'
    ROUND_UP = '2'


class RoutingType(Enum):
    TARGET_FIRM = '1'
    TARGET_LIST = '2'
    BLOCK_FIRM = '3'
    BLOCK_LIST = '4'


class Rule80A(Enum):
    PROGRAM_ORDER_NON_INDEX_ARB_FOR_OTHER_MEMBER = 'N'
    SHORT_EXEMPT_TRANSACTION_B = 'B'
    PROGRAM_ORDER_INDEX_ARB_FOR_MEMBER_FIRM_ORG = 'D'
    SHORT_EXEMPT_TRANSACTION_FOR_PRINCIPAL = 'E'
    SHORT_EXEMPT_TRANSACTION_F = 'F'
    SHORT_EXEMPT_TRANSACTION_H = 'H'
    INDIVIDUAL_INVESTOR_SINGLE_ORDER = 'I'
    PROGRAM_ORDER_INDEX_ARB_FOR_INDIVIDUAL_CUSTOMER = 'J'
    PROGRAM_ORDER_NON_INDEX_ARB_FOR_INDIVIDUAL_CUSTOMER = 'K'
    PROGRAM_ORDER_INDEX_ARB_FOR_OTHER_MEMBER = 'M'
    AGENCY_SINGLE_ORDER = 'A'
    PROPRIETARY_TRANSACTIONS_FOR_COMPETING_MARKET_MAKER_THAT_IS_AFFILIATED_WITH_THE_CLEARING_MEMBER = 'O'
    PRINCIPAL = 'P'
    TRANSACTIONS_FOR_THE_ACCOUNT_OF_A_NON_MEMBER_COMPETING_MARKET_MAKER = 'R'
    SPECIALIST_TRADES = 'S'
    TRANSACTIONS_FOR_THE_ACCOUNT_OF_AN_UNAFFILIATED_MEMBERS_COMPETING_MARKET_MAKER = 'T'
    PROGRAM_ORDER_INDEX_ARB_FOR_OTHER_AGENCY = 'U'
    ALL_OTHER_ORDERS_AS_AGENT_FOR_OTHER_MEMBER = 'W'
    SHORT_EXEMPT_TRANSACTION_FOR_MEMBER_COMPETING_MARKET_MAKER_NOT_AFFILIATED_WITH_THE_FIRM_CLEARING_THE_TRADE = 'X'
    PROGRAM_ORDER_NON_INDEX_ARB_FOR_OTHER_AGENCY = 'Y'
    SHORT_EXEMPT_TRANSACTION_FOR_NON_MEMBER_COMPETING_MARKET_MAKER = 'Z'
    SHORT_EXEMPT_TRANSACTION_FOR_MEMBER_COMPETING_MARKET_MAKER_AFFILIATED_WITH_THE_FIRM_CLEARING_THE_TRADE = 'L'
    PROGRAM_ORDER_NON_INDEX_ARB_FOR_MEMBER_FIRM_ORG = 'C'


class Scope(Enum):
    LOCAL = '1'
    NATIONAL = '2'
    GLOBAL = '3'


class SecurityIDSource(Enum):
    SICOVAM = 'E'
    SEDOL = '2'
    CUSIP = '1'
    QUIK = '3'
    BELGIAN = 'F'
    VALOREN = 'D'
    DUTCH = 'C'
    WERTPAPIER = 'B'
    BLOOMBERG_SYMBOL = 'A'
    CONSOLIDATED_TAPE_ASSOCIATION = '9'
    EXCHANGE_SYMBOL = '8'
    ISO_COUNTRY_CODE = '7'
    ISO_CURRENCY_CODE = '6'
    RIC_CODE = '5'
    ISIN_NUMBER = '4'
    COMMON = 'G'


class SecurityListRequestType(Enum):
    SECURITYTYPE_AND_OR_CFICODE = '1'
    PRODUCT = '2'
    TRADINGSESSIONID = '3'
    ALL_SECURITIES = '4'
    SYMBOL = '0'


class SecurityRequestResult(Enum):
    INSTRUMENT_DATA_TEMPORARILY_UNAVAILABLE = '4'
    VALID_REQUEST = '0'
    INVALID_OR_UNSUPPORTED_REQUEST = '1'
    REQUEST_FOR_INSTRUMENT_DATA_NOT_SUPPORTED = '5'
    NOT_AUTHORIZED_TO_RETRIEVE_INSTRUMENT_DATA = '3'
    NO_INSTRUMENTS_FOUND_THAT_MATCH_SELECTION_CRITERIA = '2'


class SecurityRequestType(Enum):
    REQUEST_SECURITY_IDENTITY_AND_SPECIFICATIONS = '0'
    REQUEST_SECURITY_IDENTITY_FOR_THE_SPECIFICATIONS_PROVIDED = '1'
    REQUEST_LIST_SECURITY_TYPES = '2'
    REQUEST_LIST_SECURITIES = '3'


class SecurityResponseType(Enum):
    REJECT_SECURITY_PROPOSAL = '5'
    ACCEPT_SECURITY_PROPOSAL_AS_IS = '1'
    CAN_NOT_MATCH_SELECTION_CRITERIA = '6'
    ACCEPT_SECURITY_PROPOSAL_WITH_REVISIONS_AS_INDICATED_IN_THE_MESSAGE = '2'
    LIST_OF_SECURITIES_RETURNED_PER_REQUEST = '4'
    LIST_OF_SECURITY_TYPES_RETURNED_PER_REQUEST = '3'


class SecurityTradingStatus(Enum):
    UNKNOWN_OR_INVALID = '20'
    NO_MARKET_ON_CLOSE_IMBALANCE = '13'
    ITS_PRE_OPENING = '14'
    NEW_PRICE_INDICATION = '15'
    TRADE_DISSEMINATION_TIME = '16'
    READY_TO_TRADE = '17'
    NOT_TRADED_ON_THIS_MARKET = '19'
    OPENING_ROTATION = '22'
    PRE_OPEN = '21'
    NO_MARKET_IMBALANCE = '12'
    NOT_AVAILABLE_FOR_TRADING = '18'
    MARKET_ON_CLOSE_IMBALANCE_SELL = '10'
    MARKET_ON_CLOSE_IMBALANCE_BUY = '9'
    MARKET_IMBALANCE_SELL = '8'
    MARKET_IMBALANCE_BUY = '7'
    TRADING_RANGE_INDICATION = '6'
    PRICE_INDICATION = '5'
    NO_OPEN_NO_RESUME = '4'
    RESUME = '3'
    OPENING_DELAY = '1'
    TRADING_HALT = '2'
    FAST_MARKET = '23'


class SecurityType(Enum):
    COMMERCIAL_PAPER = 'CP'
    VARIABLE_RATE_DEMAND_NOTE = 'VRDN'
    PLAZOS_FIJOS = 'PZFJ'
    PROMISSORY_NOTE = 'PN'
    OVERNIGHT = 'ONITE'
    MEDIUM_TERM_NOTES = 'MTN'
    TAX_EXEMPT_COMMERCIAL_PAPER = 'TECP'
    AMENDED_RESTATED = 'AMENDED'
    BRIDGE_LOAN = 'BRIDGE'
    LETTER_OF_CREDIT = 'LOFC'
    SWING_LINE_FACILITY = 'SWING'
    DEBTOR_IN_POSSESSION = 'DINP'
    DEFAULTED = 'DEFLTED'
    WITHDRAWN = 'WITHDRN'
    LIQUIDITY_NOTE = 'LQN'
    MATURED = 'MATURED'
    DEPOSIT_NOTES = 'DN'
    RETIRED = 'RETIRED'
    BANKERS_ACCEPTANCE = 'BA'
    BANK_NOTES = 'BN'
    BILL_OF_EXCHANGES = 'BOX'
    CERTIFICATE_OF_DEPOSIT = 'CD'
    CALL_LOANS = 'CL'
    REPLACED = 'REPLACD'
    MANDATORY_TENDER = 'MT'
    REVOLVER_TERM_LOAN = 'RVLVTRM'
    MORTGAGE_PRIVATE_PLACEMENT = 'MPP'
    SHORT_TERM_LOAN_NOTE = 'STN'
    MISCELLANEOUS_PASS_THROUGH = 'MPT'
    TO_BE_ANNOUNCED = 'TBA'
    OTHER_ANTICIPATION_NOTES_BAN_GAN_ETC = 'AN'
    MORTGAGE_INTEREST_ONLY = 'MIO'
    CERTIFICATE_OF_PARTICIPATION = 'COFP'
    MORTGAGE_BACKED_SECURITIES = 'MBS'
    REVENUE_BONDS = 'REV'
    SPECIAL_ASSESSMENT = 'SPCLA'
    SPECIAL_OBLIGATION = 'SPCLO'
    SPECIAL_TAX = 'SPCLT'
    TAX_ANTICIPATION_NOTE = 'TAN'
    TAX_ALLOCATION = 'TAXA'
    CERTIFICATE_OF_OBLIGATION = 'COFO'
    TIME_DEPOSIT = 'TD'
    GENERAL_OBLIGATION_BONDS = 'GO'
    WILDCARD_ENTRY = '?'
    WARRANT = 'WAR'
    MUTUAL_FUND = 'MF'
    MULTI_LEG_INSTRUMENT = 'MLEG'
    TAX_REVENUE_ANTICIPATION_NOTE = 'TRAN'
    MORTGAGE_PRINCIPAL_ONLY = 'MPO'
    REPURCHASE_AGREEMENT = 'RP'
    NO_SECURITY_TYPE = 'NONE'
    EXTENDED_COMM_NOTE = 'XCN'
    AGENCY_POOLS = 'POOL'
    ASSET_BACKED_SECURITIES = 'ABS'
    CORP_MORTGAGE_BACKED_SECURITIES = 'CMBS'
    COLLATERALIZED_MORTGAGE_OBLIGATION = 'CMO'
    IOETTE_MORTGAGE = 'IET'
    REVERSE_REPURCHASE_AGREEMENT = 'RVRP'
    FOREIGN_EXCHANGE_CONTRACT = 'FOR'
    REVENUE_ANTICIPATION_NOTE = 'RAN'
    REVOLVER_LOAN = 'RVLV'
    FEDERAL_AGENCY_COUPON = 'FAC'
    FEDERAL_AGENCY_DISCOUNT_NOTE = 'FADN'
    PRIVATE_EXPORT_FUNDING = 'PEF'
    CORPORATE_BOND = 'CORP'
    CORPORATE_PRIVATE_PLACEMENT = 'CPP'
    CONVERTIBLE_BOND = 'CB'
    DUAL_CURRENCY = 'DUAL'
    INDEXED_LINKED = 'XLINKD'
    YANKEE_CORPORATE_BOND = 'YANK'
    COMMON_STOCK = 'CS'
    PREFERRED_STOCK = 'PS'
    BRADY_BOND = 'BRADY'
    US_TREASURY_BOND = 'TBOND'
    INTEREST_STRIP_FROM_ANY_BOND_OR_NOTE = 'TINT'
    TREASURY_INFLATION_PROTECTED_SECURITIES = 'TIPS'
    PRINCIPAL_STRIP_OF_A_CALLABLE_BOND_OR_NOTE = 'TCAL'
    PRINCIPAL_STRIP_FROM_A_NON_CALLABLE_BOND_OR_NOTE = 'TPRN'
    US_TREASURY_NOTE_BOND = 'UST'
    US_TREASURY_BILL = 'USTB'
    TERM_LOAN = 'TERM'
    STRUCTURED_NOTES = 'STRUCT'


class SessionRejectReason(Enum):
    XML_VALIDATION_ERROR = '12'
    NON_DATA_VALUE_INCLUDES_FIELD_DELIMITER = '17'
    INCORRECT_NUMINGROUP_COUNT_FOR_REPEATING_GROUP = '16'
    REPEATING_GROUP_FIELDS_OUT_OF_ORDER = '15'
    TAG_SPECIFIED_OUT_OF_REQUIRED_ORDER = '14'
    INVALID_MSGTYPE = '11'
    INVALID_TAG_NUMBER = '0'
    COMPID_PROBLEM = '9'
    SIGNATURE_PROBLEM = '8'
    DECRYPTION_PROBLEM = '7'
    INCORRECT_DATA_FORMAT_FOR_VALUE = '6'
    VALUE_IS_INCORRECT = '5'
    TAG_SPECIFIED_WITHOUT_A_VALUE = '4'
    UNDEFINED_TAG = '3'
    SENDINGTIME_ACCURACY_PROBLEM = '10'
    TAG_APPEARS_MORE_THAN_ONCE = '13'
    TAG_NOT_DEFINED_FOR_THIS_MESSAGE_TYPE = '2'
    REQUIRED_TAG_MISSING = '1'


class SettlCurrFxRateCalc(Enum):
    DIVIDE = 'D'
    MULTIPLY = 'M'


class SettlDeliveryType(Enum):
    FREE = '1'
    VERSUS_PAYMENT = '0'


class SettlInstMode(Enum):
    DEFAULT = '0'
    SPECIFIC_ORDER_FOR_A_SINGLE_ACCOUNT = '4'
    SPECIFIC_ALLOCATION_ACCOUNT_STANDING = '3'
    STANDING_INSTRUCTIONS_PROVIDED = '1'
    SPECIFIC_ALLOCATION_ACCOUNT_OVERRIDING = '2'


class SettlInstSource(Enum):
    INSTITUTIONS_INSTRUCTIONS = '2'
    INVESTOR = '3'
    BROKERS_INSTRUCTIONS = '1'


class SettlInstTransType(Enum):
    NEW = 'N'
    REPLACE = 'R'
    CANCEL = 'C'


class SettlmntTyp(Enum):
    T_PLUS_4 = '5'
    T_PLUS_1 = 'A'
    FUTURE = '6'
    T_PLUS_2 = '3'
    NEXT_DAY = '2'
    SELLERS_OPTION = '8'
    CASH = '1'
    WHEN_AND_IF_ISSUED = '7'
    REGULAR = '0'
    T_PLUS_5 = '9'
    T_PLUS_3 = '4'


class Side(Enum):
    SELL_SHORT_EXEMPT = '6'
    AS_DEFINED = 'B'
    OPPOSITE = 'C'
    CROSS = '8'
    CROSS_SHORT = '9'
    BUY = '1'
    SELL = '2'
    BUY_MINUS = '3'
    SELL_PLUS = '4'
    CROSS_SHORT_EXEMPT = 'A'
    SELL_SHORT = '5'
    UNDISCLOSED = '7'


class SideValueInd(Enum):
    SIDEVALUE1 = '1'
    SIDEVALUE_2 = '2'


class SolicitedFlag(Enum):
    NO = 'N'
    YES = 'Y'


class StandInstDbType(Enum):
    OTHER = '0'
    DTC_SID = '1'
    A_GLOBAL_CUSTODIAN = '3'
    THOMSON_ALERT = '2'


class StipulationType(Enum):
    ABSOLUTE_PREPAYMENT_SPEED = 'ABS'
    WEIGHTED_AVERAGE_LOAN_AGE = 'WALA'
    WEIGHTED_AVERAGE_MATURITY = 'WAM'
    CONSTANT_PREPAYMENT_RATE = 'CPR'
    FINAL_CPR_OF_HOME_EQUITY_PREPAYMENT_CURVE = 'HEP'
    WEIGHTED_AVERAGE_LIFE = 'WAL'
    OF_MANUFACTURED_HOUSING_PREPAYMENT_CURVE = 'MHP'
    SINGLE_MONTHLY_MORTALITY = 'SMM'
    MONTHLY_PREPAYMENT_RATE = 'MPR'
    OF_BMA_PREPAYMENT_CURVE = 'PSA'
    OF_PROSPECTUS_PREPAYMENT_CURVE = 'PPC'
    CONSTANT_PREPAYMENT_PENALTY = 'CPP'
    LOT_VARIANCE = 'LOTVAR'
    CONSTANT_PREPAYMENT_YIELD = 'CPY'
    WEIGHTED_AVERAGE_COUPON = 'WAC'
    YEAR_OF_ISSUE = 'ISSUE'
    MATURITY_YEAR = 'MAT'
    NUMBER_OF_PIECES = 'PIECES'
    POOLS_MAXIMUM = 'PMAX'
    POOLS_PER_MILLION = 'PPM'
    POOLS_PER_LOT = 'PPL'
    POOLS_PER_TRADE = 'PPT'
    PRODUCTION_YEAR = 'PROD'
    TRADE_VARIANCE = 'TRDVAR'
    GEOGRAPHICS = 'GEOG'


class SubscriptionRequestType(Enum):
    SNAPSHOT_PLUS_UPDATES = '1'
    DISABLE_PREVIOUS_SNAPSHOT_PLUS_UPDATE_REQUEST = '2'
    SNAPSHOT = '0'


class TaxAdvantageType(Enum):
    PROFIT_SHARING_PLAN = '19'
    EMPLOYER = '11'
    EMPLOYER_CURRENT_YEAR = '12'
    NON_FUND_PROTOTYPE_IRA = '13'
    NON_FUND_QUALIFIED_PLAN = '14'
    DEFINED_CONTRIBUTION_PLAN = '15'
    EMPLOYEE_CURRENT_YEAR = '10'
    INDIVIDUAL_RETIREMENT_ACCOUNT_ROLLOVER = '17'
    MINI_INSURANCE_ISA = '5'
    INDIVIDUAL_RETIREMENT_ACCOUNT = '16'
    EMPLOYEE = '9'
    ASSET_TRANSFER = '8'
    SELF_DIRECTED_IRA = '21'
    CURRENT_YEAR_PAYMENT = '6'
    FOUR_HUNDRED_AND_ONE_K = '20'
    MINI_STOCKS_AND_SHARES_ISA = '4'
    MINI_CASH_ISA = '3'
    TESSA = '2'
    MAXI_ISA = '1'
    NONE_NOT_APPLICABLE = '0'
    PRIOR_YEAR_PAYMENT = '7'
    FOUR_HUNDRED_AND_FIFTY_SEVEN = '23'
    ROTH_IRA_24 = '24'
    ROTH_IRA_25 = '25'
    ROTH_CONVERSION_IRA_26 = '26'
    ROTH_CONVERSION_IRA_27 = '27'
    EDUCATION_IRA_28 = '28'
    EDUCATION_IRA_29 = '29'
    KEOGH = '18'
    FOUR_HUNDRED_AND_THREE = '22'


class TestMessageIndicator(Enum):
    YES = 'Y'
    NO = 'N'


class TickDirection(Enum):
    PLUS_TICK = '0'
    ZERO_PLUS_TICK = '1'
    MINUS_TICK = '2'
    ZERO_MINUS_TICK = '3'


class TimeInForce(Enum):
    AT_THE_CLOSE = '7'
    DAY = '0'
    GOOD_TILL_CANCEL = '1'
    AT_THE_OPENING = '2'
    IMMEDIATE_OR_CANCEL = '3'
    FILL_OR_KILL = '4'
    GOOD_TILL_CROSSING = '5'
    GOOD_TILL_DATE = '6'


class TradSesMethod(Enum):
    TWO_PARTY = '3'
    ELECTRONIC = '1'
    OPEN_OUTCRY = '2'


class TradSesMode(Enum):
    PRODUCTION = '3'
    TESTING = '1'
    SIMULATED = '2'


class TradSesStatus(Enum):
    PRE_CLOSE = '5'
    REQUEST_REJECTED = '6'
    PRE_OPEN = '4'
    CLOSED = '3'
    OPEN = '2'
    HALTED = '1'
    UNKNOWN = '0'


class TradSesStatusRejReason(Enum):
    UNKNOWN_OR_INVALID_TRADINGSESSIONID = '1'


class TradeCondition(Enum):
    NEXT_DAY_TRADE = 'J'
    OPENED = 'K'
    SELLER = 'L'
    AVERAGE_PRICE_TRADE = 'B'
    SOLD = 'M'
    RULE_155_TRADE = 'H'
    STOPPED_STOCK = 'N'
    IMBALANCE_MORE_BUYERS = 'P'
    IMBALANCE_MORE_SELLERS = 'Q'
    OPENING_PRICE = 'R'
    SOLD_LAST = 'I'
    CASH = 'A'
    CASH_TRADE = 'C'
    OPENING = 'E'
    INTRADAY_TRADE_DETAIL = 'F'
    RULE_127_TRADE = 'G'
    NEXT_DAY = 'D'


class TradeReportTransType(Enum):
    NEW = 'N'
    REPLACE = 'R'
    CANCEL = 'C'


class TradeRequestType(Enum):
    ADVISORIES_THAT_MATCH_CRITERIA = '4'
    UNREPORTED_TRADES_THAT_MATCH_CRITERIA = '3'
    UNMATCHED_TRADES_THAT_MATCH_CRITERIA = '2'
    MATCHED_TRADES_MATCHING_CRITERIA_PROVIDED_ON_REQUEST = '1'
    ALL_TRADES = '0'


class TradeType(Enum):
    VWAP_GUARANTEE = 'G'
    AGENCY = 'A'
    GUARANTEED_CLOSE = 'J'
    RISK_TRADE = 'R'


class TradedFlatSwitch(Enum):
    NO = 'N'
    YES = 'Y'


class UnsolicitedIndicator(Enum):
    YES = 'Y'
    NO = 'N'


class Urgency(Enum):
    FLASH = '1'
    BACKGROUND = '2'
    NORMAL = '0'


class WorkingIndicator(Enum):
    NO = 'N'
    YES = 'Y'


class YieldType(Enum):
    TRUE_YIELD_THE_YIELD_CALCULATED_WITH_COUPON_DATES_MOVED_FROM_A_WEEKEND_OR_HOLIDAY_TO_THE_NEXT_VALID_SETTLEMENT_DATE = 'TRUE'
    PREVIOUS_CLOSE_YIELD_THE_YIELD_OF_A_BOND_BASED_ON_THE_CLOSING_PRICE_1_DAY_AGO = 'PREVCLOSE'
    YIELD_TO_LONGEST_AVERAGE = 'LONGEST'
    YIELD_TO_LONGEST_AVERAGE_LIFE_THE_YIELD_ASSUMING_ONLY_MANDATORY_SINKS_ARE_TAKEN_THIS_RESULTS_IN_A_LOWER_PAYDOWN_OF_DEBT_THE_YIELD_IS_THEN_CALCULATED_TO_THE_FINAL_PAYMENT_DATE = 'LONGAVGLIFE'
    YIELD_TO_MATURITY_THE_YIELD_OF_A_BOND_TO_ITS_MATURITY_DATE = 'MATURITY'
    MARK_TO_MARKET_YIELD_AN_ADJUSTMENT_IN_THE_VALUATION_OF_A_SECURITIES_PORTFOLIO_TO_REFLECT_THE_CURRENT_MARKET_VALUES_OF_THE_RESPECTIVE_SECURITIES_IN_THE_PORTFOLIO = 'MARK'
    OPEN_AVERAGE_YIELD_THE_AVERAGE_YIELD_OF_THE_RESPECTIVE_SECURITIES_IN_THE_PORTFOLIO = 'OPENAVG'
    YIELD_TO_NEXT_PUT_THE_YIELD_TO_THE_DATE_AT_WHICH_THE_BOND_HOLDER_CAN_NEXT_PUT_THE_BOND_TO_THE_ISSUER = 'PUT'
    PROCEEDS_YIELD_THE_CD_EQUIVALENT_YIELD_WHEN_THE_REMAINING_TIME_TO_MATURITY_IS_LESS_THAN_TWO_YEARS = 'PROCEEDS'
    SEMI_ANNUAL_YIELD_THE_YIELD_OF_A_BOND_WHOSE_COUPON_PAYMENTS_ARE_REINVESTED_SEMI_ANNUALLY = 'SEMIANNUAL'
    YIELD_TO_SHORTEST_AVERAGE_LIFE_SAME_AS_AVGLIFE_ABOVE = 'SHORTAVGLIFE'
    YIELD_TO_SHORTEST_AVERAGE = 'SHORTEST'
    SIMPLE_YIELD_THE_YIELD_OF_A_BOND_ASSUMING_NO_REINVESTMENT_OF_COUPON_PAYMENTS = 'SIMPLE'
    YIELD_TO_TENDER_DATE_THE_YIELD_ON_A_MUNICIPAL_BOND_TO_ITS_MANDATORY_TENDER_DATE = 'TENDER'
    YIELD_VALUE_OF_1_32_THE_AMOUNT_THAT_THE_YIELD_WILL_CHANGE_FOR_A_1_32_ND_CHANGE_IN_PRICE = 'VALUE1/32'
    YIELD_TO_WORST_CONVENTION_THE_LOWEST_YIELD_TO_ALL_POSSIBLE_REDEMPTION_DATE_SCENARIOS = 'WORST'
    TAX_EQUIVALENT_YIELD_THE_AFTER_TAX_YIELD_GROSSED_UP_BY_THE_MAXIMUM_FEDERAL_TAX_RATE_OF_396_FOR_COMPARISON_TO_TAXABLE_YIELDS = 'TAXEQUIV'
    ANNUAL_YIELD_THE_ANNUAL_INTEREST_OR_DIVIDEND_INCOME_AN_INVESTMENT_EARNS_EXPRESSED_AS_A_PERCENTAGE_OF_THE_INVESTMENTS_TOTAL_VALUE = 'ANNUAL'
    CLOSING_YIELD_MOST_RECENT_YEAR_THE_YIELD_OF_A_BOND_BASED_ON_THE_CLOSING_PRICE_AS_OF_THE_MOST_RECENT_YEARS_END = 'LASTYEAR'
    YIELD_TO_NEXT_REFUND = 'NEXTREFUND'
    AFTER_TAX_YIELD = 'AFTERTAX'
    YIELD_AT_ISSUE = 'ATISSUE'
    YIELD_TO_AVERAGE_LIFE_THE_YIELD_ASSUMING_THAT_ALL_SINKS = 'AVGLIFE'
    YIELD_TO_AVERAGE_MATURITY_THE_YIELD_ACHIEVED_BY_SUBSTITUTING_A_BONDS_AVERAGE_MATURITY_FOR_THE_ISSUES_FINAL_MATURITY_DATE = 'AVGMATURITY'
    BOOK_YIELD_THE_YIELD_OF_A_SECURITY_CALCULATED_BY_USING_ITS_BOOK_VALUE_INSTEAD_OF_THE_CURRENT_MARKET_PRICE_THIS_TERM_IS_TYPICALLY_USED_IN_THE_US_DOMESTIC_MARKET = 'BOOK'
    YIELD_TO_NEXT_CALL_THE_YIELD_OF_A_BOND_TO_THE_NEXT_POSSIBLE_CALL_DATE = 'CALL'
    YIELD_CHANGE_SINCE_CLOSE_THE_CHANGE_IN_THE_YIELD_SINCE_THE_PREVIOUS_DAYS_CLOSING_YIELD = 'CHANGE'
    COMPOUND_YIELD_THE_YIELD_OF_CERTAIN_JAPANESE_BONDS_BASED_ON_ITS_PRICE_CERTAIN_JAPANESE_BONDS_HAVE_IRREGULAR_FIRST_OR_LAST_COUPONS_AND_THE_YIELD_IS_CALCULATED_COMPOUND_FOR_THESE_IRREGULAR_PERIODS = 'COMPOUND'
    CURRENT_YIELD_ANNUAL_INTEREST_ON_A_BOND_DIVIDED_BY_THE_MARKET_VALUE_THE_ACTUAL_INCOME_RATE_OF_RETURN_AS_OPPOSED_TO_THE_COUPON_RATE_EXPRESSED_AS_A_PERCENTAGE = 'CURRENT'
    TRUE_GROSS_YIELD_YIELD_CALCULATED_USING_THE_PRICE_INCLUDING_ACCRUED_INTEREST_WHERE_COUPON_DATES_ARE_MOVED_FROM_HOLIDAYS_AND_WEEKENDS_TO_THE_NEXT_TRADING_DAY = 'GROSS'
    GOVERNMENT_EQUIVALENT_YIELD_ASK_YIELD_BASED_ON_SEMI_ANNUAL_COUPONS_COMPOUNDING_IN_ALL_PERIODS_AND_ACTUAL_ACTUAL_CALENDAR = 'GOVTEQUIV'
    YIELD_WITH_INFLATION_ASSUMPTION_BASED_ON_PRICE_THE_RETURN_AN_INVESTOR_WOULD_REQUIRE_ON_A_NORMAL_BOND_THAT_WOULD_MAKE_THE_REAL_RETURN_EQUAL_TO_THAT_OF_THE_INFLATION_INDEXED_BOND_ASSUMING_A_CONSTANT_INFLATION_RATE = 'INFLATION'
    INVERSE_FLOATER_BOND_YIELD_INVERSE_FLOATER_SEMI_ANNUAL_BOND_EQUIVALENT_RATE = 'INVERSEFLOATER'
    CLOSING_YIELD_MOST_RECENT_QUARTER_THE_YIELD_OF_A_BOND_BASED_ON_THE_CLOSING_PRICE_AS_OF_THE_MOST_RECENT_QUARTERS_END = 'LASTQUARTER'
    MOST_RECENT_CLOSING_YIELD_THE_LAST_AVAILABLE_YIELD_STORED_IN_HISTORY_COMPUTED_USING_PRICE = 'LASTCLOSE'
    CLOSING_YIELD_MOST_RECENT_MONTH_THE_YIELD_OF_A_BOND_BASED_ON_THE_CLOSING_PRICE_AS_OF_THE_MOST_RECENT_MONTHS_END = 'LASTMONTH'
    CLOSING_YIELD_THE_YIELD_OF_A_BOND_BASED_ON_THE_CLOSING_PRICE = 'CLOSE'
