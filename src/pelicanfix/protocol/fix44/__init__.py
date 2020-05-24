from enum import Enum

from pelicanfix.protocol import FIXField


class Field(Enum):
    ACCOUNT = FIXField('Account', 1)
    ACCOUNT_TYPE = FIXField('AccountType', 581)
    ACCRUED_INTEREST_AMT = FIXField('AccruedInterestAmt', 159)
    ACCRUED_INTEREST_RATE = FIXField('AccruedInterestRate', 158)
    ACCT_ID_SOURCE = FIXField('AcctIDSource', 660)
    ADJUSTMENT = FIXField('Adjustment', 334)
    ADJUSTMENT_TYPE = FIXField('AdjustmentType', 718)
    ADV_ID = FIXField('AdvId', 2)
    ADV_REF_ID = FIXField('AdvRefID', 3)
    ADV_SIDE = FIXField('AdvSide', 4)
    ADV_TRANS_TYPE = FIXField('AdvTransType', 5)
    AFFECTED_ORDER_ID = FIXField('AffectedOrderID', 535)
    AFFECTED_SECONDARY_ORDER_ID = FIXField('AffectedSecondaryOrderID', 536)
    AFFIRM_STATUS = FIXField('AffirmStatus', 940)
    AGGREGATED_BOOK = FIXField('AggregatedBook', 266)
    AGREEMENT_CURRENCY = FIXField('AgreementCurrency', 918)
    AGREEMENT_DATE = FIXField('AgreementDate', 915)
    AGREEMENT_DESC = FIXField('AgreementDesc', 913)
    AGREEMENT_ID = FIXField('AgreementID', 914)
    ALLOC_ACCOUNT = FIXField('AllocAccount', 79)
    ALLOC_ACCOUNT_TYPE = FIXField('AllocAccountType', 798)
    ALLOC_ACCRUED_INTEREST_AMT = FIXField('AllocAccruedInterestAmt', 742)
    ALLOC_ACCT_ID_SOURCE = FIXField('AllocAcctIDSource', 661)
    ALLOC_AVG_PX = FIXField('AllocAvgPx', 153)
    ALLOC_CANC_REPLACE_REASON = FIXField('AllocCancReplaceReason', 796)
    ALLOC_HANDL_INST = FIXField('AllocHandlInst', 209)
    ALLOC_ID = FIXField('AllocID', 70)
    ALLOC_INTEREST_AT_MATURITY = FIXField('AllocInterestAtMaturity', 741)
    ALLOC_INTERMED_REQ_TYPE = FIXField('AllocIntermedReqType', 808)
    ALLOC_LINK_ID = FIXField('AllocLinkID', 196)
    ALLOC_LINK_TYPE = FIXField('AllocLinkType', 197)
    ALLOC_NET_MONEY = FIXField('AllocNetMoney', 154)
    ALLOC_NO_ORDERS_TYPE = FIXField('AllocNoOrdersType', 857)
    ALLOC_PRICE = FIXField('AllocPrice', 366)
    ALLOC_QTY = FIXField('AllocQty', 80)
    ALLOC_REJ_CODE = FIXField('AllocRejCode', 88)
    ALLOC_REPORT_ID = FIXField('AllocReportID', 755)
    ALLOC_REPORT_REF_ID = FIXField('AllocReportRefID', 795)
    ALLOC_REPORT_TYPE = FIXField('AllocReportType', 794)
    ALLOC_SETTL_CURR_AMT = FIXField('AllocSettlCurrAmt', 737)
    ALLOC_SETTL_CURRENCY = FIXField('AllocSettlCurrency', 736)
    ALLOC_SETTL_INST_TYPE = FIXField('AllocSettlInstType', 780)
    ALLOC_STATUS = FIXField('AllocStatus', 87)
    ALLOC_TEXT = FIXField('AllocText', 161)
    ALLOC_TRANS_TYPE = FIXField('AllocTransType', 71)
    ALLOC_TYPE = FIXField('AllocType', 626)
    ALLOWABLE_ONE_SIDEDNESS_CURR = FIXField('AllowableOneSidednessCurr', 767)
    ALLOWABLE_ONE_SIDEDNESS_PCT = FIXField('AllowableOneSidednessPct', 765)
    ALLOWABLE_ONE_SIDEDNESS_VALUE = FIXField('AllowableOneSidednessValue', 766)
    ALT_MD_SOURCE_ID = FIXField('AltMDSourceID', 817)
    APPL_QUEUE_ACTION = FIXField('ApplQueueAction', 815)
    APPL_QUEUE_DEPTH = FIXField('ApplQueueDepth', 813)
    APPL_QUEUE_MAX = FIXField('ApplQueueMax', 812)
    APPL_QUEUE_RESOLUTION = FIXField('ApplQueueResolution', 814)
    ASGN_RPT_ID = FIXField('AsgnRptID', 833)
    ASSIGNMENT_METHOD = FIXField('AssignmentMethod', 744)
    ASSIGNMENT_UNIT = FIXField('AssignmentUnit', 745)
    AUTO_ACCEPT_INDICATOR = FIXField('AutoAcceptIndicator', 754)
    AVG_PAR_PX = FIXField('AvgParPx', 860)
    AVG_PX = FIXField('AvgPx', 6)
    AVG_PX_INDICATOR = FIXField('AvgPxIndicator', 819)
    AVG_PX_PRECISION = FIXField('AvgPxPrecision', 74)
    BASIS_FEATURE_DATE = FIXField('BasisFeatureDate', 259)
    BASIS_FEATURE_PRICE = FIXField('BasisFeaturePrice', 260)
    BASIS_PX_TYPE = FIXField('BasisPxType', 419)
    BEGIN_SEQ_NO = FIXField('BeginSeqNo', 7)
    BEGIN_STRING = FIXField('BeginString', 8)
    BENCHMARK_CURVE_CURRENCY = FIXField('BenchmarkCurveCurrency', 220)
    BENCHMARK_CURVE_NAME = FIXField('BenchmarkCurveName', 221)
    BENCHMARK_CURVE_POINT = FIXField('BenchmarkCurvePoint', 222)
    BENCHMARK_PRICE = FIXField('BenchmarkPrice', 662)
    BENCHMARK_PRICE_TYPE = FIXField('BenchmarkPriceType', 663)
    BENCHMARK_SECURITY_ID = FIXField('BenchmarkSecurityID', 699)
    BENCHMARK_SECURITY_ID_SOURCE = FIXField('BenchmarkSecurityIDSource', 761)
    BID_DESCRIPTOR = FIXField('BidDescriptor', 400)
    BID_DESCRIPTOR_TYPE = FIXField('BidDescriptorType', 399)
    BID_FORWARD_POINTS = FIXField('BidForwardPoints', 189)
    BID_FORWARD_POINTS2 = FIXField('BidForwardPoints2', 642)
    BID_ID = FIXField('BidID', 390)
    BID_PX = FIXField('BidPx', 132)
    BID_REQUEST_TRANS_TYPE = FIXField('BidRequestTransType', 374)
    BID_SIZE = FIXField('BidSize', 134)
    BID_SPOT_RATE = FIXField('BidSpotRate', 188)
    BID_TRADE_TYPE = FIXField('BidTradeType', 418)
    BID_TYPE = FIXField('BidType', 394)
    BID_YIELD = FIXField('BidYield', 632)
    BODY_LENGTH = FIXField('BodyLength', 9)
    BOOKING_REF_ID = FIXField('BookingRefID', 466)
    BOOKING_TYPE = FIXField('BookingType', 775)
    BOOKING_UNIT = FIXField('BookingUnit', 590)
    BUSINESS_REJECT_REASON = FIXField('BusinessRejectReason', 380)
    BUSINESS_REJECT_REF_ID = FIXField('BusinessRejectRefID', 379)
    BUY_VOLUME = FIXField('BuyVolume', 330)
    CFI_CODE = FIXField('CFICode', 461)
    CP_PROGRAM = FIXField('CPProgram', 875)
    CP_REG_TYPE = FIXField('CPRegType', 876)
    CANCELLATION_RIGHTS = FIXField('CancellationRights', 480)
    CARD_EXP_DATE = FIXField('CardExpDate', 490)
    CARD_HOLDER_NAME = FIXField('CardHolderName', 488)
    CARD_ISS_NUM = FIXField('CardIssNum', 491)
    CARD_NUMBER = FIXField('CardNumber', 489)
    CARD_START_DATE = FIXField('CardStartDate', 503)
    CASH_DISTRIB_AGENT_ACCT_NAME = FIXField('CashDistribAgentAcctName', 502)
    CASH_DISTRIB_AGENT_ACCT_NUMBER = FIXField('CashDistribAgentAcctNumber', 500)
    CASH_DISTRIB_AGENT_CODE = FIXField('CashDistribAgentCode', 499)
    CASH_DISTRIB_AGENT_NAME = FIXField('CashDistribAgentName', 498)
    CASH_DISTRIB_CURR = FIXField('CashDistribCurr', 478)
    CASH_DISTRIB_PAY_REF = FIXField('CashDistribPayRef', 501)
    CASH_MARGIN = FIXField('CashMargin', 544)
    CASH_ORDER_QTY = FIXField('CashOrderQty', 152)
    CASH_OUTSTANDING = FIXField('CashOutstanding', 901)
    CHECK_SUM = FIXField('CheckSum', 10)
    CL_ORD_ID = FIXField('ClOrdID', 11)
    CL_ORD_LINK_ID = FIXField('ClOrdLinkID', 583)
    CLEARING_BUSINESS_DATE = FIXField('ClearingBusinessDate', 715)
    CLEARING_FEE_INDICATOR = FIXField('ClearingFeeIndicator', 635)
    CLEARING_INSTRUCTION = FIXField('ClearingInstruction', 577)
    CLIENT_BID_ID = FIXField('ClientBidID', 391)
    COLL_ACTION = FIXField('CollAction', 944)
    COLL_ASGN_ID = FIXField('CollAsgnID', 902)
    COLL_ASGN_REASON = FIXField('CollAsgnReason', 895)
    COLL_ASGN_REF_ID = FIXField('CollAsgnRefID', 907)
    COLL_ASGN_REJECT_REASON = FIXField('CollAsgnRejectReason', 906)
    COLL_ASGN_RESP_TYPE = FIXField('CollAsgnRespType', 905)
    COLL_ASGN_TRANS_TYPE = FIXField('CollAsgnTransType', 903)
    COLL_INQUIRY_ID = FIXField('CollInquiryID', 909)
    COLL_INQUIRY_QUALIFIER = FIXField('CollInquiryQualifier', 896)
    COLL_INQUIRY_RESULT = FIXField('CollInquiryResult', 946)
    COLL_INQUIRY_STATUS = FIXField('CollInquiryStatus', 945)
    COLL_REQ_ID = FIXField('CollReqID', 894)
    COLL_RESP_ID = FIXField('CollRespID', 904)
    COLL_RPT_ID = FIXField('CollRptID', 908)
    COLL_STATUS = FIXField('CollStatus', 910)
    COMM_CURRENCY = FIXField('CommCurrency', 479)
    COMM_TYPE = FIXField('CommType', 13)
    COMMISSION = FIXField('Commission', 12)
    COMPLIANCE_ID = FIXField('ComplianceID', 376)
    CONCESSION = FIXField('Concession', 238)
    CONFIRM_ID = FIXField('ConfirmID', 664)
    CONFIRM_REF_ID = FIXField('ConfirmRefID', 772)
    CONFIRM_REJ_REASON = FIXField('ConfirmRejReason', 774)
    CONFIRM_REQ_ID = FIXField('ConfirmReqID', 859)
    CONFIRM_STATUS = FIXField('ConfirmStatus', 665)
    CONFIRM_TRANS_TYPE = FIXField('ConfirmTransType', 666)
    CONFIRM_TYPE = FIXField('ConfirmType', 773)
    CONT_AMT_CURR = FIXField('ContAmtCurr', 521)
    CONT_AMT_TYPE = FIXField('ContAmtType', 519)
    CONT_AMT_VALUE = FIXField('ContAmtValue', 520)
    CONTRA_BROKER = FIXField('ContraBroker', 375)
    CONTRA_LEG_REF_ID = FIXField('ContraLegRefID', 655)
    CONTRA_TRADE_QTY = FIXField('ContraTradeQty', 437)
    CONTRA_TRADE_TIME = FIXField('ContraTradeTime', 438)
    CONTRA_TRADER = FIXField('ContraTrader', 337)
    CONTRACT_MULTIPLIER = FIXField('ContractMultiplier', 231)
    CONTRACT_SETTL_MONTH = FIXField('ContractSettlMonth', 667)
    CONTRARY_INSTRUCTION_INDICATOR = FIXField('ContraryInstructionIndicator', 719)
    COPY_MSG_INDICATOR = FIXField('CopyMsgIndicator', 797)
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
    DATED_DATE = FIXField('DatedDate', 873)
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
    DELIVERY_DATE = FIXField('DeliveryDate', 743)
    DELIVERY_FORM = FIXField('DeliveryForm', 668)
    DELIVERY_TYPE = FIXField('DeliveryType', 919)
    DESIGNATION = FIXField('Designation', 494)
    DESK_ID = FIXField('DeskID', 284)
    DISCRETION_INST = FIXField('DiscretionInst', 388)
    DISCRETION_LIMIT_TYPE = FIXField('DiscretionLimitType', 843)
    DISCRETION_MOVE_TYPE = FIXField('DiscretionMoveType', 841)
    DISCRETION_OFFSET_TYPE = FIXField('DiscretionOffsetType', 842)
    DISCRETION_OFFSET_VALUE = FIXField('DiscretionOffsetValue', 389)
    DISCRETION_PRICE = FIXField('DiscretionPrice', 845)
    DISCRETION_ROUND_DIRECTION = FIXField('DiscretionRoundDirection', 844)
    DISCRETION_SCOPE = FIXField('DiscretionScope', 846)
    DISTRIB_PAYMENT_METHOD = FIXField('DistribPaymentMethod', 477)
    DISTRIB_PERCENTAGE = FIXField('DistribPercentage', 512)
    DLVY_INST_TYPE = FIXField('DlvyInstType', 787)
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
    END_ACCRUED_INTEREST_AMT = FIXField('EndAccruedInterestAmt', 920)
    END_CASH = FIXField('EndCash', 922)
    END_DATE = FIXField('EndDate', 917)
    END_SEQ_NO = FIXField('EndSeqNo', 16)
    EVENT_DATE = FIXField('EventDate', 866)
    EVENT_PX = FIXField('EventPx', 867)
    EVENT_TEXT = FIXField('EventText', 868)
    EVENT_TYPE = FIXField('EventType', 865)
    EX_DATE = FIXField('ExDate', 230)
    EX_DESTINATION = FIXField('ExDestination', 100)
    EXCHANGE_FOR_PHYSICAL = FIXField('ExchangeForPhysical', 411)
    EXCHANGE_RULE = FIXField('ExchangeRule', 825)
    EXEC_ID = FIXField('ExecID', 17)
    EXEC_INST = FIXField('ExecInst', 18)
    EXEC_PRICE_ADJUSTMENT = FIXField('ExecPriceAdjustment', 485)
    EXEC_PRICE_TYPE = FIXField('ExecPriceType', 484)
    EXEC_REF_ID = FIXField('ExecRefID', 19)
    EXEC_RESTATEMENT_REASON = FIXField('ExecRestatementReason', 378)
    EXEC_TYPE = FIXField('ExecType', 150)
    EXEC_VALUATION_POINT = FIXField('ExecValuationPoint', 515)
    EXERCISE_METHOD = FIXField('ExerciseMethod', 747)
    EXPIRATION_CYCLE = FIXField('ExpirationCycle', 827)
    EXPIRE_DATE = FIXField('ExpireDate', 432)
    EXPIRE_TIME = FIXField('ExpireTime', 126)
    FACTOR = FIXField('Factor', 228)
    FAIR_VALUE = FIXField('FairValue', 406)
    FINANCIAL_STATUS = FIXField('FinancialStatus', 291)
    FOREX_REQ = FIXField('ForexReq', 121)
    FUND_RENEW_WAIV = FIXField('FundRenewWaiv', 497)
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
    IOIID = FIXField('IOIID', 23)
    IOI_NATURAL_FLAG = FIXField('IOINaturalFlag', 130)
    IOI_QLTY_IND = FIXField('IOIQltyInd', 25)
    IOI_QTY = FIXField('IOIQty', 27)
    IOI_QUALIFIER = FIXField('IOIQualifier', 104)
    IOI_REF_ID = FIXField('IOIRefID', 26)
    IOI_TRANS_TYPE = FIXField('IOITransType', 28)
    IN_VIEW_OF_COMMON = FIXField('InViewOfCommon', 328)
    INC_TAX_IND = FIXField('IncTaxInd', 416)
    INDIVIDUAL_ALLOC_ID = FIXField('IndividualAllocID', 467)
    INDIVIDUAL_ALLOC_REJ_CODE = FIXField('IndividualAllocRejCode', 776)
    INSTR_ATTRIB_TYPE = FIXField('InstrAttribType', 871)
    INSTR_ATTRIB_VALUE = FIXField('InstrAttribValue', 872)
    INSTR_REGISTRY = FIXField('InstrRegistry', 543)
    INTEREST_ACCRUAL_DATE = FIXField('InterestAccrualDate', 874)
    INTEREST_AT_MATURITY = FIXField('InterestAtMaturity', 738)
    INVESTOR_COUNTRY_OF_RESIDENCE = FIXField('InvestorCountryOfResidence', 475)
    ISSUE_DATE = FIXField('IssueDate', 225)
    ISSUER = FIXField('Issuer', 106)
    LAST_CAPACITY = FIXField('LastCapacity', 29)
    LAST_FORWARD_POINTS = FIXField('LastForwardPoints', 195)
    LAST_FORWARD_POINTS2 = FIXField('LastForwardPoints2', 641)
    LAST_FRAGMENT = FIXField('LastFragment', 893)
    LAST_LIQUIDITY_IND = FIXField('LastLiquidityInd', 851)
    LAST_MKT = FIXField('LastMkt', 30)
    LAST_MSG_SEQ_NUM_PROCESSED = FIXField('LastMsgSeqNumProcessed', 369)
    LAST_NETWORK_RESPONSE_ID = FIXField('LastNetworkResponseID', 934)
    LAST_PAR_PX = FIXField('LastParPx', 669)
    LAST_PX = FIXField('LastPx', 31)
    LAST_QTY = FIXField('LastQty', 32)
    LAST_RPT_REQUESTED = FIXField('LastRptRequested', 912)
    LAST_SPOT_RATE = FIXField('LastSpotRate', 194)
    LAST_UPDATE_TIME = FIXField('LastUpdateTime', 779)
    LEAVES_QTY = FIXField('LeavesQty', 151)
    LEG_ALLOC_ACCOUNT = FIXField('LegAllocAccount', 671)
    LEG_ALLOC_ACCT_ID_SOURCE = FIXField('LegAllocAcctIDSource', 674)
    LEG_ALLOC_QTY = FIXField('LegAllocQty', 673)
    LEG_BENCHMARK_CURVE_CURRENCY = FIXField('LegBenchmarkCurveCurrency', 676)
    LEG_BENCHMARK_CURVE_NAME = FIXField('LegBenchmarkCurveName', 677)
    LEG_BENCHMARK_CURVE_POINT = FIXField('LegBenchmarkCurvePoint', 678)
    LEG_BENCHMARK_PRICE = FIXField('LegBenchmarkPrice', 679)
    LEG_BENCHMARK_PRICE_TYPE = FIXField('LegBenchmarkPriceType', 680)
    LEG_BID_PX = FIXField('LegBidPx', 681)
    LEG_CFI_CODE = FIXField('LegCFICode', 608)
    LEG_CONTRACT_MULTIPLIER = FIXField('LegContractMultiplier', 614)
    LEG_CONTRACT_SETTL_MONTH = FIXField('LegContractSettlMonth', 955)
    LEG_COUNTRY_OF_ISSUE = FIXField('LegCountryOfIssue', 596)
    LEG_COUPON_PAYMENT_DATE = FIXField('LegCouponPaymentDate', 248)
    LEG_COUPON_RATE = FIXField('LegCouponRate', 615)
    LEG_COVERED_OR_UNCOVERED = FIXField('LegCoveredOrUncovered', 565)
    LEG_CREDIT_RATING = FIXField('LegCreditRating', 257)
    LEG_CURRENCY = FIXField('LegCurrency', 556)
    LEG_DATED_DATE = FIXField('LegDatedDate', 739)
    LEG_FACTOR = FIXField('LegFactor', 253)
    LEG_IOI_QTY = FIXField('LegIOIQty', 682)
    LEG_INDIVIDUAL_ALLOC_ID = FIXField('LegIndividualAllocID', 672)
    LEG_INSTR_REGISTRY = FIXField('LegInstrRegistry', 599)
    LEG_INTEREST_ACCRUAL_DATE = FIXField('LegInterestAccrualDate', 956)
    LEG_ISSUE_DATE = FIXField('LegIssueDate', 249)
    LEG_ISSUER = FIXField('LegIssuer', 617)
    LEG_LAST_PX = FIXField('LegLastPx', 637)
    LEG_LOCALE_OF_ISSUE = FIXField('LegLocaleOfIssue', 598)
    LEG_MATURITY_DATE = FIXField('LegMaturityDate', 611)
    LEG_MATURITY_MONTH_YEAR = FIXField('LegMaturityMonthYear', 610)
    LEG_OFFER_PX = FIXField('LegOfferPx', 684)
    LEG_OPT_ATTRIBUTE = FIXField('LegOptAttribute', 613)
    LEG_POOL = FIXField('LegPool', 740)
    LEG_POSITION_EFFECT = FIXField('LegPositionEffect', 564)
    LEG_PRICE = FIXField('LegPrice', 566)
    LEG_PRICE_TYPE = FIXField('LegPriceType', 686)
    LEG_PRODUCT = FIXField('LegProduct', 607)
    LEG_QTY = FIXField('LegQty', 687)
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
    LEG_SECURITY_SUB_TYPE = FIXField('LegSecuritySubType', 764)
    LEG_SECURITY_TYPE = FIXField('LegSecurityType', 609)
    LEG_SETTL_CURRENCY = FIXField('LegSettlCurrency', 675)
    LEG_SETTL_DATE = FIXField('LegSettlDate', 588)
    LEG_SETTL_TYPE = FIXField('LegSettlType', 587)
    LEG_SIDE = FIXField('LegSide', 624)
    LEG_STATE_OR_PROVINCE_OF_ISSUE = FIXField('LegStateOrProvinceOfIssue', 597)
    LEG_STIPULATION_TYPE = FIXField('LegStipulationType', 688)
    LEG_STIPULATION_VALUE = FIXField('LegStipulationValue', 689)
    LEG_STRIKE_CURRENCY = FIXField('LegStrikeCurrency', 942)
    LEG_STRIKE_PRICE = FIXField('LegStrikePrice', 612)
    LEG_SWAP_TYPE = FIXField('LegSwapType', 690)
    LEG_SYMBOL = FIXField('LegSymbol', 600)
    LEG_SYMBOL_SFX = FIXField('LegSymbolSfx', 601)
    LEGAL_CONFIRM = FIXField('LegalConfirm', 650)
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
    LONG_QTY = FIXField('LongQty', 704)
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
    MARGIN_EXCESS = FIXField('MarginExcess', 899)
    MARGIN_RATIO = FIXField('MarginRatio', 898)
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
    MATURITY_NET_MONEY = FIXField('MaturityNetMoney', 890)
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
    MISC_FEE_BASIS = FIXField('MiscFeeBasis', 891)
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
    NESTED2_PARTY_ID = FIXField('Nested2PartyID', 757)
    NESTED2_PARTY_ID_SOURCE = FIXField('Nested2PartyIDSource', 758)
    NESTED2_PARTY_ROLE = FIXField('Nested2PartyRole', 759)
    NESTED2_PARTY_SUB_ID = FIXField('Nested2PartySubID', 760)
    NESTED2_PARTY_SUB_ID_TYPE = FIXField('Nested2PartySubIDType', 807)
    NESTED3_PARTY_ID = FIXField('Nested3PartyID', 949)
    NESTED3_PARTY_ID_SOURCE = FIXField('Nested3PartyIDSource', 950)
    NESTED3_PARTY_ROLE = FIXField('Nested3PartyRole', 951)
    NESTED3_PARTY_SUB_ID = FIXField('Nested3PartySubID', 953)
    NESTED3_PARTY_SUB_ID_TYPE = FIXField('Nested3PartySubIDType', 954)
    NESTED_PARTY_ID = FIXField('NestedPartyID', 524)
    NESTED_PARTY_ID_SOURCE = FIXField('NestedPartyIDSource', 525)
    NESTED_PARTY_ROLE = FIXField('NestedPartyRole', 538)
    NESTED_PARTY_SUB_ID = FIXField('NestedPartySubID', 545)
    NESTED_PARTY_SUB_ID_TYPE = FIXField('NestedPartySubIDType', 805)
    NET_CHG_PREV_DAY = FIXField('NetChgPrevDay', 451)
    NET_GROSS_IND = FIXField('NetGrossInd', 430)
    NET_MONEY = FIXField('NetMoney', 118)
    NETWORK_REQUEST_ID = FIXField('NetworkRequestID', 933)
    NETWORK_REQUEST_TYPE = FIXField('NetworkRequestType', 935)
    NETWORK_RESPONSE_ID = FIXField('NetworkResponseID', 932)
    NETWORK_STATUS_RESPONSE_TYPE = FIXField('NetworkStatusResponseType', 937)
    NEW_PASSWORD = FIXField('NewPassword', 925)
    NEW_SEQ_NO = FIXField('NewSeqNo', 36)
    NEXT_EXPECTED_MSG_SEQ_NUM = FIXField('NextExpectedMsgSeqNum', 789)
    NO_AFFECTED_ORDERS = FIXField('NoAffectedOrders', 534)
    NO_ALLOCS = FIXField('NoAllocs', 78)
    NO_ALT_MD_SOURCE = FIXField('NoAltMDSource', 816)
    NO_BID_COMPONENTS = FIXField('NoBidComponents', 420)
    NO_BID_DESCRIPTORS = FIXField('NoBidDescriptors', 398)
    NO_CAPACITIES = FIXField('NoCapacities', 862)
    NO_CLEARING_INSTRUCTIONS = FIXField('NoClearingInstructions', 576)
    NO_COLL_INQUIRY_QUALIFIER = FIXField('NoCollInquiryQualifier', 938)
    NO_COMP_I_DS = FIXField('NoCompIDs', 936)
    NO_CONT_AMTS = FIXField('NoContAmts', 518)
    NO_CONTRA_BROKERS = FIXField('NoContraBrokers', 382)
    NO_DATES = FIXField('NoDates', 580)
    NO_DISTRIB_INSTS = FIXField('NoDistribInsts', 510)
    NO_DLVY_INST = FIXField('NoDlvyInst', 85)
    NO_EVENTS = FIXField('NoEvents', 864)
    NO_EXECS = FIXField('NoExecs', 124)
    NO_HOPS = FIXField('NoHops', 627)
    NO_IOI_QUALIFIERS = FIXField('NoIOIQualifiers', 199)
    NO_INSTR_ATTRIB = FIXField('NoInstrAttrib', 870)
    NO_LEG_ALLOCS = FIXField('NoLegAllocs', 670)
    NO_LEG_SECURITY_ALT_ID = FIXField('NoLegSecurityAltID', 604)
    NO_LEG_STIPULATIONS = FIXField('NoLegStipulations', 683)
    NO_LEGS = FIXField('NoLegs', 555)
    NO_LINES_OF_TEXT = FIXField('NoLinesOfText', 33)
    NO_MD_ENTRIES = FIXField('NoMDEntries', 268)
    NO_MD_ENTRY_TYPES = FIXField('NoMDEntryTypes', 267)
    NO_MISC_FEES = FIXField('NoMiscFees', 136)
    NO_MSG_TYPES = FIXField('NoMsgTypes', 384)
    NO_NESTED2_PARTY_I_DS = FIXField('NoNested2PartyIDs', 756)
    NO_NESTED2_PARTY_SUB_I_DS = FIXField('NoNested2PartySubIDs', 806)
    NO_NESTED3_PARTY_I_DS = FIXField('NoNested3PartyIDs', 948)
    NO_NESTED3_PARTY_SUB_I_DS = FIXField('NoNested3PartySubIDs', 952)
    NO_NESTED_PARTY_I_DS = FIXField('NoNestedPartyIDs', 539)
    NO_NESTED_PARTY_SUB_I_DS = FIXField('NoNestedPartySubIDs', 804)
    NO_ORDERS = FIXField('NoOrders', 73)
    NO_PARTY_I_DS = FIXField('NoPartyIDs', 453)
    NO_PARTY_SUB_I_DS = FIXField('NoPartySubIDs', 802)
    NO_POS_AMT = FIXField('NoPosAmt', 753)
    NO_POSITIONS = FIXField('NoPositions', 702)
    NO_QUOTE_ENTRIES = FIXField('NoQuoteEntries', 295)
    NO_QUOTE_QUALIFIERS = FIXField('NoQuoteQualifiers', 735)
    NO_QUOTE_SETS = FIXField('NoQuoteSets', 296)
    NO_REGIST_DTLS = FIXField('NoRegistDtls', 473)
    NO_RELATED_SYM = FIXField('NoRelatedSym', 146)
    NO_ROUTING_I_DS = FIXField('NoRoutingIDs', 215)
    NO_RPTS = FIXField('NoRpts', 82)
    NO_SECURITY_ALT_ID = FIXField('NoSecurityAltID', 454)
    NO_SECURITY_TYPES = FIXField('NoSecurityTypes', 558)
    NO_SETTL_INST = FIXField('NoSettlInst', 778)
    NO_SETTL_PARTY_I_DS = FIXField('NoSettlPartyIDs', 781)
    NO_SETTL_PARTY_SUB_I_DS = FIXField('NoSettlPartySubIDs', 801)
    NO_SIDES = FIXField('NoSides', 552)
    NO_STIPULATIONS = FIXField('NoStipulations', 232)
    NO_STRIKES = FIXField('NoStrikes', 428)
    NO_TRADES = FIXField('NoTrades', 897)
    NO_TRADING_SESSIONS = FIXField('NoTradingSessions', 386)
    NO_TRD_REG_TIMESTAMPS = FIXField('NoTrdRegTimestamps', 768)
    NO_UNDERLYING_SECURITY_ALT_ID = FIXField('NoUnderlyingSecurityAltID', 457)
    NO_UNDERLYING_STIPS = FIXField('NoUnderlyingStips', 887)
    NO_UNDERLYINGS = FIXField('NoUnderlyings', 711)
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
    ON_BEHALF_OF_SUB_ID = FIXField('OnBehalfOfSubID', 116)
    OPEN_CLOSE_SETTL_FLAG = FIXField('OpenCloseSettlFlag', 286)
    OPEN_INTEREST = FIXField('OpenInterest', 746)
    OPT_ATTRIBUTE = FIXField('OptAttribute', 206)
    ORD_REJ_REASON = FIXField('OrdRejReason', 103)
    ORD_STATUS = FIXField('OrdStatus', 39)
    ORD_STATUS_REQ_ID = FIXField('OrdStatusReqID', 790)
    ORD_TYPE = FIXField('OrdType', 40)
    ORDER_AVG_PX = FIXField('OrderAvgPx', 799)
    ORDER_BOOKING_QTY = FIXField('OrderBookingQty', 800)
    ORDER_CAPACITY = FIXField('OrderCapacity', 528)
    ORDER_CAPACITY_QTY = FIXField('OrderCapacityQty', 863)
    ORDER_ID = FIXField('OrderID', 37)
    ORDER_INPUT_DEVICE = FIXField('OrderInputDevice', 821)
    ORDER_PERCENT = FIXField('OrderPercent', 516)
    ORDER_QTY = FIXField('OrderQty', 38)
    ORDER_QTY2 = FIXField('OrderQty2', 192)
    ORDER_RESTRICTIONS = FIXField('OrderRestrictions', 529)
    ORIG_CL_ORD_ID = FIXField('OrigClOrdID', 41)
    ORIG_CROSS_ID = FIXField('OrigCrossID', 551)
    ORIG_ORD_MOD_TIME = FIXField('OrigOrdModTime', 586)
    ORIG_POS_REQ_REF_ID = FIXField('OrigPosReqRefID', 713)
    ORIG_SENDING_TIME = FIXField('OrigSendingTime', 122)
    ORIG_TIME = FIXField('OrigTime', 42)
    OUT_MAIN_CNTRY_U_INDEX = FIXField('OutMainCntryUIndex', 412)
    OUTSIDE_INDEX_PCT = FIXField('OutsideIndexPct', 407)
    OWNER_TYPE = FIXField('OwnerType', 522)
    OWNERSHIP_TYPE = FIXField('OwnershipType', 517)
    PARTICIPATION_RATE = FIXField('ParticipationRate', 849)
    PARTY_ID = FIXField('PartyID', 448)
    PARTY_ID_SOURCE = FIXField('PartyIDSource', 447)
    PARTY_ROLE = FIXField('PartyRole', 452)
    PARTY_SUB_ID = FIXField('PartySubID', 523)
    PARTY_SUB_ID_TYPE = FIXField('PartySubIDType', 803)
    PASSWORD = FIXField('Password', 554)
    PAYMENT_DATE = FIXField('PaymentDate', 504)
    PAYMENT_METHOD = FIXField('PaymentMethod', 492)
    PAYMENT_REF = FIXField('PaymentRef', 476)
    PAYMENT_REMITTER_ID = FIXField('PaymentRemitterID', 505)
    PCT_AT_RISK = FIXField('PctAtRisk', 869)
    PEG_LIMIT_TYPE = FIXField('PegLimitType', 837)
    PEG_MOVE_TYPE = FIXField('PegMoveType', 835)
    PEG_OFFSET_TYPE = FIXField('PegOffsetType', 836)
    PEG_OFFSET_VALUE = FIXField('PegOffsetValue', 211)
    PEG_ROUND_DIRECTION = FIXField('PegRoundDirection', 838)
    PEG_SCOPE = FIXField('PegScope', 840)
    PEGGED_PRICE = FIXField('PeggedPrice', 839)
    POOL = FIXField('Pool', 691)
    POS_AMT = FIXField('PosAmt', 708)
    POS_AMT_TYPE = FIXField('PosAmtType', 707)
    POS_MAINT_ACTION = FIXField('PosMaintAction', 712)
    POS_MAINT_RESULT = FIXField('PosMaintResult', 723)
    POS_MAINT_RPT_ID = FIXField('PosMaintRptID', 721)
    POS_MAINT_RPT_REF_ID = FIXField('PosMaintRptRefID', 714)
    POS_MAINT_STATUS = FIXField('PosMaintStatus', 722)
    POS_QTY_STATUS = FIXField('PosQtyStatus', 706)
    POS_REQ_ID = FIXField('PosReqID', 710)
    POS_REQ_RESULT = FIXField('PosReqResult', 728)
    POS_REQ_STATUS = FIXField('PosReqStatus', 729)
    POS_REQ_TYPE = FIXField('PosReqType', 724)
    POS_TRANS_TYPE = FIXField('PosTransType', 709)
    POS_TYPE = FIXField('PosType', 703)
    POSITION_EFFECT = FIXField('PositionEffect', 77)
    POSS_DUP_FLAG = FIXField('PossDupFlag', 43)
    POSS_RESEND = FIXField('PossResend', 97)
    PREALLOC_METHOD = FIXField('PreallocMethod', 591)
    PREV_CLOSE_PX = FIXField('PrevClosePx', 140)
    PREVIOUSLY_REPORTED = FIXField('PreviouslyReported', 570)
    PRICE = FIXField('Price', 44)
    PRICE2 = FIXField('Price2', 640)
    PRICE_DELTA = FIXField('PriceDelta', 811)
    PRICE_IMPROVEMENT = FIXField('PriceImprovement', 639)
    PRICE_TYPE = FIXField('PriceType', 423)
    PRIOR_SETTL_PRICE = FIXField('PriorSettlPrice', 734)
    PRIOR_SPREAD_INDICATOR = FIXField('PriorSpreadIndicator', 720)
    PRIORITY_INDICATOR = FIXField('PriorityIndicator', 638)
    PROCESS_CODE = FIXField('ProcessCode', 81)
    PRODUCT = FIXField('Product', 460)
    PROG_PERIOD_INTERVAL = FIXField('ProgPeriodInterval', 415)
    PROG_RPT_REQS = FIXField('ProgRptReqs', 414)
    PUBLISH_TRD_INDICATOR = FIXField('PublishTrdIndicator', 852)
    PUT_OR_CALL = FIXField('PutOrCall', 201)
    QTY_TYPE = FIXField('QtyType', 854)
    QUANTITY = FIXField('Quantity', 53)
    QUOTE_CANCEL_TYPE = FIXField('QuoteCancelType', 298)
    QUOTE_CONDITION = FIXField('QuoteCondition', 276)
    QUOTE_ENTRY_ID = FIXField('QuoteEntryID', 299)
    QUOTE_ENTRY_REJECT_REASON = FIXField('QuoteEntryRejectReason', 368)
    QUOTE_ID = FIXField('QuoteID', 117)
    QUOTE_PRICE_TYPE = FIXField('QuotePriceType', 692)
    QUOTE_QUALIFIER = FIXField('QuoteQualifier', 695)
    QUOTE_REJECT_REASON = FIXField('QuoteRejectReason', 300)
    QUOTE_REQ_ID = FIXField('QuoteReqID', 131)
    QUOTE_REQUEST_REJECT_REASON = FIXField('QuoteRequestRejectReason', 658)
    QUOTE_REQUEST_TYPE = FIXField('QuoteRequestType', 303)
    QUOTE_RESP_ID = FIXField('QuoteRespID', 693)
    QUOTE_RESP_TYPE = FIXField('QuoteRespType', 694)
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
    REF_COMP_ID = FIXField('RefCompID', 930)
    REF_MSG_TYPE = FIXField('RefMsgType', 372)
    REF_SEQ_NUM = FIXField('RefSeqNum', 45)
    REF_SUB_ID = FIXField('RefSubID', 931)
    REF_TAG_ID = FIXField('RefTagID', 371)
    REGIST_ACCT_TYPE = FIXField('RegistAcctType', 493)
    REGIST_DTLS = FIXField('RegistDtls', 509)
    REGIST_EMAIL = FIXField('RegistEmail', 511)
    REGIST_ID = FIXField('RegistID', 513)
    REGIST_REF_ID = FIXField('RegistRefID', 508)
    REGIST_REJ_REASON_CODE = FIXField('RegistRejReasonCode', 507)
    REGIST_REJ_REASON_TEXT = FIXField('RegistRejReasonText', 496)
    REGIST_STATUS = FIXField('RegistStatus', 506)
    REGIST_TRANS_TYPE = FIXField('RegistTransType', 514)
    REPO_COLLATERAL_SECURITY_TYPE = FIXField('RepoCollateralSecurityType', 239)
    REPORT_TO_EXCH = FIXField('ReportToExch', 113)
    REPORTED_PX = FIXField('ReportedPx', 861)
    REPURCHASE_RATE = FIXField('RepurchaseRate', 227)
    REPURCHASE_TERM = FIXField('RepurchaseTerm', 226)
    RESET_SEQ_NUM_FLAG = FIXField('ResetSeqNumFlag', 141)
    RESPONSE_DESTINATION = FIXField('ResponseDestination', 726)
    RESPONSE_TRANSPORT_TYPE = FIXField('ResponseTransportType', 725)
    REVERSAL_INDICATOR = FIXField('ReversalIndicator', 700)
    ROUND_LOT = FIXField('RoundLot', 561)
    ROUNDING_DIRECTION = FIXField('RoundingDirection', 468)
    ROUNDING_MODULUS = FIXField('RoundingModulus', 469)
    ROUTING_ID = FIXField('RoutingID', 217)
    ROUTING_TYPE = FIXField('RoutingType', 216)
    RPT_SEQ = FIXField('RptSeq', 83)
    SCOPE = FIXField('Scope', 546)
    SECONDARY_ALLOC_ID = FIXField('SecondaryAllocID', 793)
    SECONDARY_CL_ORD_ID = FIXField('SecondaryClOrdID', 526)
    SECONDARY_EXEC_ID = FIXField('SecondaryExecID', 527)
    SECONDARY_ORDER_ID = FIXField('SecondaryOrderID', 198)
    SECONDARY_TRADE_REPORT_ID = FIXField('SecondaryTradeReportID', 818)
    SECONDARY_TRADE_REPORT_REF_ID = FIXField('SecondaryTradeReportRefID', 881)
    SECONDARY_TRD_TYPE = FIXField('SecondaryTrdType', 855)
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
    SECURITY_STATUS_REQ_ID = FIXField('SecurityStatusReqID', 324)
    SECURITY_SUB_TYPE = FIXField('SecuritySubType', 762)
    SECURITY_TRADING_STATUS = FIXField('SecurityTradingStatus', 326)
    SECURITY_TYPE = FIXField('SecurityType', 167)
    SELL_VOLUME = FIXField('SellVolume', 331)
    SELLER_DAYS = FIXField('SellerDays', 287)
    SENDER_COMP_ID = FIXField('SenderCompID', 49)
    SENDER_LOCATION_ID = FIXField('SenderLocationID', 142)
    SENDER_SUB_ID = FIXField('SenderSubID', 50)
    SENDING_TIME = FIXField('SendingTime', 52)
    SESSION_REJECT_REASON = FIXField('SessionRejectReason', 373)
    SETTL_CURR_AMT = FIXField('SettlCurrAmt', 119)
    SETTL_CURR_BID_FX_RATE = FIXField('SettlCurrBidFxRate', 656)
    SETTL_CURR_FX_RATE = FIXField('SettlCurrFxRate', 155)
    SETTL_CURR_FX_RATE_CALC = FIXField('SettlCurrFxRateCalc', 156)
    SETTL_CURR_OFFER_FX_RATE = FIXField('SettlCurrOfferFxRate', 657)
    SETTL_CURRENCY = FIXField('SettlCurrency', 120)
    SETTL_DATE = FIXField('SettlDate', 64)
    SETTL_DATE2 = FIXField('SettlDate2', 193)
    SETTL_DELIVERY_TYPE = FIXField('SettlDeliveryType', 172)
    SETTL_INST_ID = FIXField('SettlInstID', 162)
    SETTL_INST_MODE = FIXField('SettlInstMode', 160)
    SETTL_INST_MSG_ID = FIXField('SettlInstMsgID', 777)
    SETTL_INST_REF_ID = FIXField('SettlInstRefID', 214)
    SETTL_INST_REQ_ID = FIXField('SettlInstReqID', 791)
    SETTL_INST_REQ_REJ_CODE = FIXField('SettlInstReqRejCode', 792)
    SETTL_INST_SOURCE = FIXField('SettlInstSource', 165)
    SETTL_INST_TRANS_TYPE = FIXField('SettlInstTransType', 163)
    SETTL_PARTY_ID = FIXField('SettlPartyID', 782)
    SETTL_PARTY_ID_SOURCE = FIXField('SettlPartyIDSource', 783)
    SETTL_PARTY_ROLE = FIXField('SettlPartyRole', 784)
    SETTL_PARTY_SUB_ID = FIXField('SettlPartySubID', 785)
    SETTL_PARTY_SUB_ID_TYPE = FIXField('SettlPartySubIDType', 786)
    SETTL_PRICE = FIXField('SettlPrice', 730)
    SETTL_PRICE_TYPE = FIXField('SettlPriceType', 731)
    SETTL_SESS_ID = FIXField('SettlSessID', 716)
    SETTL_SESS_SUB_ID = FIXField('SettlSessSubID', 717)
    SETTL_TYPE = FIXField('SettlType', 63)
    SHARED_COMMISSION = FIXField('SharedCommission', 858)
    SHORT_QTY = FIXField('ShortQty', 705)
    SHORT_SALE_REASON = FIXField('ShortSaleReason', 853)
    SIDE = FIXField('Side', 54)
    SIDE_COMPLIANCE_ID = FIXField('SideComplianceID', 659)
    SIDE_MULTI_LEG_REPORTING_TYPE = FIXField('SideMultiLegReportingType', 752)
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
    START_CASH = FIXField('StartCash', 921)
    START_DATE = FIXField('StartDate', 916)
    STATE_OR_PROVINCE_OF_ISSUE = FIXField('StateOrProvinceOfIssue', 471)
    STATUS_TEXT = FIXField('StatusText', 929)
    STATUS_VALUE = FIXField('StatusValue', 928)
    STIPULATION_TYPE = FIXField('StipulationType', 233)
    STIPULATION_VALUE = FIXField('StipulationValue', 234)
    STOP_PX = FIXField('StopPx', 99)
    STRIKE_CURRENCY = FIXField('StrikeCurrency', 947)
    STRIKE_PRICE = FIXField('StrikePrice', 202)
    STRIKE_TIME = FIXField('StrikeTime', 443)
    SUBJECT = FIXField('Subject', 147)
    SUBSCRIPTION_REQUEST_TYPE = FIXField('SubscriptionRequestType', 263)
    SYMBOL = FIXField('Symbol', 55)
    SYMBOL_SFX = FIXField('SymbolSfx', 65)
    TARGET_COMP_ID = FIXField('TargetCompID', 56)
    TARGET_LOCATION_ID = FIXField('TargetLocationID', 143)
    TARGET_STRATEGY = FIXField('TargetStrategy', 847)
    TARGET_STRATEGY_PARAMETERS = FIXField('TargetStrategyParameters', 848)
    TARGET_STRATEGY_PERFORMANCE = FIXField('TargetStrategyPerformance', 850)
    TARGET_SUB_ID = FIXField('TargetSubID', 57)
    TAX_ADVANTAGE_TYPE = FIXField('TaxAdvantageType', 495)
    TERMINATION_TYPE = FIXField('TerminationType', 788)
    TEST_MESSAGE_INDICATOR = FIXField('TestMessageIndicator', 464)
    TEST_REQ_ID = FIXField('TestReqID', 112)
    TEXT = FIXField('Text', 58)
    THRESHOLD_AMOUNT = FIXField('ThresholdAmount', 834)
    TICK_DIRECTION = FIXField('TickDirection', 274)
    TIME_BRACKET = FIXField('TimeBracket', 943)
    TIME_IN_FORCE = FIXField('TimeInForce', 59)
    TOT_NO_ALLOCS = FIXField('TotNoAllocs', 892)
    TOT_NO_ORDERS = FIXField('TotNoOrders', 68)
    TOT_NO_QUOTE_ENTRIES = FIXField('TotNoQuoteEntries', 304)
    TOT_NO_RELATED_SYM = FIXField('TotNoRelatedSym', 393)
    TOT_NO_SECURITY_TYPES = FIXField('TotNoSecurityTypes', 557)
    TOT_NO_STRIKES = FIXField('TotNoStrikes', 422)
    TOT_NUM_ASSIGNMENT_REPORTS = FIXField('TotNumAssignmentReports', 832)
    TOT_NUM_REPORTS = FIXField('TotNumReports', 911)
    TOT_NUM_TRADE_REPORTS = FIXField('TotNumTradeReports', 748)
    TOTAL_ACCRUED_INTEREST_AMT = FIXField('TotalAccruedInterestAmt', 540)
    TOTAL_AFFECTED_ORDERS = FIXField('TotalAffectedOrders', 533)
    TOTAL_NET_VALUE = FIXField('TotalNetValue', 900)
    TOTAL_NUM_POS_REPORTS = FIXField('TotalNumPosReports', 727)
    TOTAL_TAKEDOWN = FIXField('TotalTakedown', 237)
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
    TRAD_SES_STATUS_REJ_REASON = FIXField('TradSesStatusRejReason', 567)
    TRADE_ALLOC_INDICATOR = FIXField('TradeAllocIndicator', 826)
    TRADE_CONDITION = FIXField('TradeCondition', 277)
    TRADE_DATE = FIXField('TradeDate', 75)
    TRADE_INPUT_DEVICE = FIXField('TradeInputDevice', 579)
    TRADE_INPUT_SOURCE = FIXField('TradeInputSource', 578)
    TRADE_LEG_REF_ID = FIXField('TradeLegRefID', 824)
    TRADE_LINK_ID = FIXField('TradeLinkID', 820)
    TRADE_ORIGINATION_DATE = FIXField('TradeOriginationDate', 229)
    TRADE_REPORT_ID = FIXField('TradeReportID', 571)
    TRADE_REPORT_REF_ID = FIXField('TradeReportRefID', 572)
    TRADE_REPORT_REJECT_REASON = FIXField('TradeReportRejectReason', 751)
    TRADE_REPORT_TRANS_TYPE = FIXField('TradeReportTransType', 487)
    TRADE_REPORT_TYPE = FIXField('TradeReportType', 856)
    TRADE_REQUEST_ID = FIXField('TradeRequestID', 568)
    TRADE_REQUEST_RESULT = FIXField('TradeRequestResult', 749)
    TRADE_REQUEST_STATUS = FIXField('TradeRequestStatus', 750)
    TRADE_REQUEST_TYPE = FIXField('TradeRequestType', 569)
    TRADED_FLAT_SWITCH = FIXField('TradedFlatSwitch', 258)
    TRADING_SESSION_ID = FIXField('TradingSessionID', 336)
    TRADING_SESSION_SUB_ID = FIXField('TradingSessionSubID', 625)
    TRANS_BKD_TIME = FIXField('TransBkdTime', 483)
    TRANSACT_TIME = FIXField('TransactTime', 60)
    TRANSFER_REASON = FIXField('TransferReason', 830)
    TRD_MATCH_ID = FIXField('TrdMatchID', 880)
    TRD_REG_TIMESTAMP = FIXField('TrdRegTimestamp', 769)
    TRD_REG_TIMESTAMP_ORIGIN = FIXField('TrdRegTimestampOrigin', 771)
    TRD_REG_TIMESTAMP_TYPE = FIXField('TrdRegTimestampType', 770)
    TRD_RPT_STATUS = FIXField('TrdRptStatus', 939)
    TRD_SUB_TYPE = FIXField('TrdSubType', 829)
    TRD_TYPE = FIXField('TrdType', 828)
    URL_LINK = FIXField('URLLink', 149)
    UNDERLYING_CFI_CODE = FIXField('UnderlyingCFICode', 463)
    UNDERLYING_CP_PROGRAM = FIXField('UnderlyingCPProgram', 877)
    UNDERLYING_CP_REG_TYPE = FIXField('UnderlyingCPRegType', 878)
    UNDERLYING_CONTRACT_MULTIPLIER = FIXField('UnderlyingContractMultiplier', 436)
    UNDERLYING_COUNTRY_OF_ISSUE = FIXField('UnderlyingCountryOfIssue', 592)
    UNDERLYING_COUPON_PAYMENT_DATE = FIXField('UnderlyingCouponPaymentDate', 241)
    UNDERLYING_COUPON_RATE = FIXField('UnderlyingCouponRate', 435)
    UNDERLYING_CREDIT_RATING = FIXField('UnderlyingCreditRating', 256)
    UNDERLYING_CURRENCY = FIXField('UnderlyingCurrency', 318)
    UNDERLYING_CURRENT_VALUE = FIXField('UnderlyingCurrentValue', 885)
    UNDERLYING_DIRTY_PRICE = FIXField('UnderlyingDirtyPrice', 882)
    UNDERLYING_END_PRICE = FIXField('UnderlyingEndPrice', 883)
    UNDERLYING_END_VALUE = FIXField('UnderlyingEndValue', 886)
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
    UNDERLYING_PX = FIXField('UnderlyingPx', 810)
    UNDERLYING_QTY = FIXField('UnderlyingQty', 879)
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
    UNDERLYING_SECURITY_SUB_TYPE = FIXField('UnderlyingSecuritySubType', 763)
    UNDERLYING_SECURITY_TYPE = FIXField('UnderlyingSecurityType', 310)
    UNDERLYING_SETTL_PRICE = FIXField('UnderlyingSettlPrice', 732)
    UNDERLYING_SETTL_PRICE_TYPE = FIXField('UnderlyingSettlPriceType', 733)
    UNDERLYING_START_VALUE = FIXField('UnderlyingStartValue', 884)
    UNDERLYING_STATE_OR_PROVINCE_OF_ISSUE = FIXField('UnderlyingStateOrProvinceOfIssue', 593)
    UNDERLYING_STIP_TYPE = FIXField('UnderlyingStipType', 888)
    UNDERLYING_STIP_VALUE = FIXField('UnderlyingStipValue', 889)
    UNDERLYING_STRIKE_CURRENCY = FIXField('UnderlyingStrikeCurrency', 941)
    UNDERLYING_STRIKE_PRICE = FIXField('UnderlyingStrikePrice', 316)
    UNDERLYING_SYMBOL = FIXField('UnderlyingSymbol', 311)
    UNDERLYING_SYMBOL_SFX = FIXField('UnderlyingSymbolSfx', 312)
    UNDERLYING_TRADING_SESSION_ID = FIXField('UnderlyingTradingSessionID', 822)
    UNDERLYING_TRADING_SESSION_SUB_ID = FIXField('UnderlyingTradingSessionSubID', 823)
    UNSOLICITED_INDICATOR = FIXField('UnsolicitedIndicator', 325)
    URGENCY = FIXField('Urgency', 61)
    USER_REQUEST_ID = FIXField('UserRequestID', 923)
    USER_REQUEST_TYPE = FIXField('UserRequestType', 924)
    USER_STATUS = FIXField('UserStatus', 926)
    USER_STATUS_TEXT = FIXField('UserStatusText', 927)
    USERNAME = FIXField('Username', 553)
    VALID_UNTIL_TIME = FIXField('ValidUntilTime', 62)
    VALUE_OF_FUTURES = FIXField('ValueOfFutures', 408)
    WORKING_INDICATOR = FIXField('WorkingIndicator', 636)
    WT_AVERAGE_LIQUIDITY = FIXField('WtAverageLiquidity', 410)
    XML_DATA = FIXField('XmlData', 213)
    XML_DATA_LEN = FIXField('XmlDataLen', 212)
    YIELD = FIXField('Yield', 236)
    YIELD_CALC_DATE = FIXField('YieldCalcDate', 701)
    YIELD_REDEMPTION_DATE = FIXField('YieldRedemptionDate', 696)
    YIELD_REDEMPTION_PRICE = FIXField('YieldRedemptionPrice', 697)
    YIELD_REDEMPTION_PRICE_TYPE = FIXField('YieldRedemptionPriceType', 698)
    YIELD_TYPE = FIXField('YieldType', 235)


class AccountType(Enum):
    ACCOUNT_IS_CARRIED_ON_CUSTOMER_SIDE_OF_BOOKS = '1'
    ACCOUNT_IS_CARRIED_ON_NON_CUSTOMER_SIDE_OF_BOOKS = '2'
    HOUSE_TRADER = '3'
    FLOOR_TRADER = '4'
    ACCOUNT_IS_CARRIED_ON_NON_CUSTOMER_SIDE_OF_BOOKS_AND_IS_CROSS_MARGINED = '6'
    ACCOUNT_IS_HOUSE_TRADER_AND_IS_CROSS_MARGINED = '7'
    JOINT_BACKOFFICE_ACCOUNT = '8'


class AcctIDSource(Enum):
    BIC = '1'
    SID_CODE = '2'
    TFM = '3'
    OMGEO = '4'
    DTCC_CODE = '5'
    OTHER = '99'


class Adjustment(Enum):
    CANCEL = '1'
    ERROR = '2'
    CORRECTION = '3'


class AdjustmentType(Enum):
    PROCESS_REQUEST_AS_MARGIN_DISPOSITION = '0'
    DELTA_PLUS = '1'
    DELTA_MINUS = '2'
    FINAL = '3'


class AdvSide(Enum):
    BUY = 'B'
    SELL = 'S'
    CROSS = 'X'
    TRADE = 'T'


class AdvTransType(Enum):
    NEW = 'N'
    CANCEL = 'C'
    REPLACE = 'R'


class AffirmStatus(Enum):
    RECEIVED = '1'
    CONFIRM_REJECTED_IE_NOT_AFFIRMED = '2'
    AFFIRMED = '3'


class AggregatedBook(Enum):
    YES = 'Y'
    NO = 'N'


class AllocAccountType(Enum):
    ACCOUNT_IS_CARRIED_ON_CUSTOMER_SIDE_OF_BOOKS = '1'
    ACCOUNT_IS_CARRIED_ON_NON_CUSTOMER_SIDE_OF_BOOKS = '2'
    HOUSE_TRADER = '3'
    FLOOR_TRADER = '4'
    ACCOUNT_IS_CARRIED_ON_NON_CUSTOMER_SIDE_OF_BOOKS_AND_IS_CROSS_MARGINED = '6'
    ACCOUNT_IS_HOUSE_TRADER_AND_IS_CROSS_MARGINED = '7'
    JOINT_BACKOFFICE_ACCOUNT = '8'


class AllocCancReplaceReason(Enum):
    ORIGINAL_DETAILS_INCOMPLETE_INCORRECT = '1'
    CHANGE_IN_UNDERLYING_ORDER_DETAILS = '2'
    OTHER = '99'


class AllocHandlInst(Enum):
    MATCH = '1'
    FORWARD = '2'
    FORWARD_AND_MATCH = '3'


class AllocIntermedReqType(Enum):
    PENDING_ACCEPT = '1'
    PENDING_RELEASE = '2'
    PENDING_REVERSAL = '3'
    ACCEPT = '4'
    BLOCK_LEVEL_REJECT = '5'
    ACCOUNT_LEVEL_REJECT = '6'


class AllocLinkType(Enum):
    F_X_NETTING = '0'
    F_X_SWAP = '1'


class AllocNoOrdersType(Enum):
    NOT_SPECIFIED = '0'
    EXPLICIT_LIST_PROVIDED = '1'


class AllocRejCode(Enum):
    UNKNOWN_ACCOUNT = '0'
    INCORRECT_QUANTITY = '1'
    INCORRECT_AVERAGE_PRICE = '2'
    UNKNOWN_EXECUTING_BROKER_MNEMONIC = '3'
    COMMISSION_DIFFERENCE = '4'
    UNKNOWN_ORDERID = '5'
    UNKNOWN_LISTID = '6'
    OTHER = '7'
    INCORRECT_ALLOCATED_QUANTITY = '8'
    CALCULATION_DIFFERENCE = '9'
    UNKNOWN_OR_STALE_EXECID = '10'
    MISMATCHED_DATA_VALUE = '11'
    UNKNOWN_CLORDID = '12'
    WAREHOUSE_REQUEST_REJECTED = '13'


class AllocReportType(Enum):
    SELLSIDE_CALCULATED_USING_PRELIMINARY = '3'
    SELLSIDE_CALCULATED_WITHOUT_PRELIMINARY = '4'
    WAREHOUSE_RECAP = '5'
    REQUEST_TO_INTERMEDIARY = '8'


class AllocSettlInstType(Enum):
    USE_DEFAULT_INSTRUCTIONS = '0'
    DERIVE_FROM_PARAMETERS_PROVIDED = '1'
    FULL_DETAILS_PROVIDED = '2'
    SSI_DB_IDS_PROVIDED = '3'
    PHONE_FOR_INSTRUCTIONS = '4'


class AllocStatus(Enum):
    ACCEPTED = '0'
    BLOCK_LEVEL_REJECT = '1'
    ACCOUNT_LEVEL_REJECT = '2'
    RECEIVED = '3'
    INCOMPLETE = '4'
    REJECTED_BY_INTERMEDIARY = '5'


class AllocTransType(Enum):
    NEW = '0'
    REPLACE = '1'
    CANCEL = '2'


class AllocType(Enum):
    CALCULATED = '1'
    PRELIMINARY = '2'
    READY_TO_BOOK = '5'
    WAREHOUSE_INSTRUCTION = '7'
    REQUEST_TO_INTERMEDIARY = '8'


class ApplQueueAction(Enum):
    NO_ACTION_TAKEN = '0'
    QUEUE_FLUSHED = '1'
    OVERLAY_LAST = '2'
    END_SESSION = '3'


class ApplQueueResolution(Enum):
    NO_ACTION_TAKEN = '0'
    QUEUE_FLUSHED = '1'
    OVERLAY_LAST = '2'
    END_SESSION = '3'


class AssignmentMethod(Enum):
    RANDOM = 'R'
    PRORATA = 'P'


class AvgPxIndicator(Enum):
    NO_AVERAGE_PRICING = '0'
    TRADE_IS_PART_OF_AN_AVERAGE_PRICE_GROUP_IDENTIFIED_BY_THE_TRADELINKID = '1'
    LAST_TRADE_IN_THE_AVERAGE_PRICE_GROUP_IDENTIFIED_BY_THE_TRADELINKID = '2'


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


class BidDescriptorType(Enum):
    SECTOR = '1'
    COUNTRY = '2'
    INDEX = '3'


class BidRequestTransType(Enum):
    NEW = 'N'
    CANCEL = 'C'


class BidTradeType(Enum):
    RISK_TRADE = 'R'
    VWAP_GUARANTEE = 'G'
    AGENCY = 'A'
    GUARANTEED_CLOSE = 'J'


class BidType(Enum):
    NON_DISCLOSED_STYLE = '1'
    DISCLOSED_STYLE = '2'
    NO_BIDDING_PROCESS = '3'


class BookingType(Enum):
    REGULAR_BOOKING = '0'
    CFD = '1'
    TOTAL_RETURN_SWAP = '2'


class BookingUnit(Enum):
    EACH_PARTIAL_EXECUTION_IS_A_BOOKABLE_UNIT = '0'
    AGGREGATE_PARTIAL_EXECUTIONS_ON_THIS_ORDER_AND_BOOK_ONE_TRADE_PER_ORDER = '1'
    AGGREGATE_EXECUTIONS_FOR_THIS_SYMBOL_SIDE_AND_SETTLEMENT_DATE = '2'


class BusinessRejectReason(Enum):
    OTHER = '0'
    UNKOWN_ID = '1'
    UNKNOWN_SECURITY = '2'
    UNSUPPORTED_MESSAGE_TYPE = '3'
    APPLICATION_NOT_AVAILABLE = '4'
    CONDITIONALLY_REQUIRED_FIELD_MISSING = '5'
    NOT_AUTHORIZED = '6'
    DELIVERTO_FIRM_NOT_AVAILABLE_AT_THIS_TIME = '7'


class CPProgram(Enum):
    THREE = '1'
    FOUR = '2'
    OTHER = '99'


class CancellationRights(Enum):
    YES = 'Y'
    NO_EXECUTION_ONLY = 'N'
    NO_WAIVER_AGREEMENT = 'M'
    NO_INSTITUTIONAL = 'O'


class CashMargin(Enum):
    CASH = '1'
    MARGIN_OPEN = '2'
    MARGIN_CLOSE = '3'


class ClearingFeeIndicator(Enum):
    CBOE_MEMBER = 'B'
    NON_MEMBER_AND_CUSTOMER = 'C'
    EQUITY_MEMBER_AND_CLEARING_MEMBER = 'E'
    FULL_AND_ASSOCIATE_MEMBER_TRADING_FOR_OWN_ACCOUNT_AND_AS_FLOOR_BROKERS = 'F'
    ONE_HUNDRED_AND_SIX_H_AND_106_J_FIRMS = 'H'
    GIM_IDEM_AND_COM_MEMBERSHIP_INTEREST_HOLDERS = 'I'
    LESSEE_AND_106_F_EMPLOYEES = 'L'
    ALL_OTHER_OWNERSHIP_TYPES = 'M'
    ONE_ST_YEAR_DELEGATE_TRADING_FOR_HIS_OWN_ACCOUNT = '1'
    TWO_ND_YEAR_DELEGATE_TRADING_FOR_HIS_OWN_ACCOUNT = '2'
    THREE_RD_YEAR_DELEGATE_TRADING_FOR_HIS_OWN_ACCOUNT = '3'
    FOUR_TH_YEAR_DELEGATE_TRADING_FOR_HIS_OWN_ACCOUNT = '4'
    FIVE_TH_YEAR_DELEGATE_TRADING_FOR_HIS_OWN_ACCOUNT = '5'
    SIX_TH_YEAR_AND_BEYOND_DELEGATE_TRADING_FOR_HIS_OWN_ACCOUNT = '9'


class ClearingInstruction(Enum):
    PROCESS_NORMALLY = '0'
    EXCLUDE_FROM_ALL_NETTING = '1'
    BILATERAL_NETTING_ONLY = '2'
    EX_CLEARING = '3'
    SPECIAL_TRADE = '4'
    MULTILATERAL_NETTING = '5'
    CLEAR_AGAINST_CENTRAL_COUNTERPARTY = '6'
    EXCLUDE_FROM_CENTRAL_COUNTERPARTY = '7'
    MANUAL_MODE = '8'
    AUTOMATIC_POSTING_MODE = '9'
    AUTOMATIC_GIVE_UP_MODE = '10'
    QUALIFIED_SERVICE_REPRESENTATIVE = '11'
    CUSTOMER_TRADE = '12'
    SELF_CLEARING = '13'


class CollAction(Enum):
    RETAIN = '0'
    ADD = '1'
    REMOVE = '2'


class CollAsgnReason(Enum):
    INITIAL = '0'
    SCHEDULED = '1'
    TIME_WARNING = '2'
    MARGIN_DEFICIENCY = '3'
    MARGIN_EXCESS = '4'
    FORWARD_COLLATERAL_DEMAND = '5'
    EVENT_OF_DEFAULT = '6'
    ADVERSE_TAX_EVENT = '7'


class CollAsgnRejectReason(Enum):
    UNKNOWN_DEAL = '0'
    UNKNOWN_OR_INVALID_INSTRUMENT = '1'
    UNAUTHORIZED_TRANSACTION = '2'
    INSUFFICIENT_COLLATERAL = '3'
    INVALID_TYPE_OF_COLLATERAL = '4'
    EXCESSIVE_SUBSTITUTION = '5'
    OTHER = '99'


class CollAsgnRespType(Enum):
    RECEIVED = '0'
    ACCEPTED = '1'
    DECLINED = '2'
    REJECTED = '3'


class CollAsgnTransType(Enum):
    NEW = '0'
    REPLACE = '1'
    CANCEL = '2'
    RELEASE = '3'
    REVERSE = '4'


class CollInquiryQualifier(Enum):
    TRADEDATE = '0'
    GC_INSTRUMENT = '1'
    COLLATERALINSTRUMENT = '2'
    SUBSTITUTION_ELIGIBLE = '3'
    NOT_ASSIGNED = '4'
    PARTIALLY_ASSIGNED = '5'
    FULLY_ASSIGNED = '6'
    OUTSTANDING_TRADES = '7'


class CollInquiryResult(Enum):
    SUCCESSFUL = '0'
    INVALID_OR_UNKNOWN_INSTRUMENT = '1'
    INVALID_OR_UNKNOWN_COLLATERAL_TYPE = '2'
    INVALID_PARTIES = '3'
    INVALID_TRANSPORT_TYPE_REQUESTED = '4'
    INVALID_DESTINATION_REQUESTED = '5'
    NO_COLLATERAL_FOUND_FOR_THE_TRADE_SPECIFIED = '6'
    NO_COLLATERAL_FOUND_FOR_THE_ORDER_SPECIFIED = '7'
    COLLATERAL_INQUIRY_TYPE_NOT_SUPPORTED = '8'
    UNAUTHORIZED_FOR_COLLATERAL_INQUIRY = '9'
    OTHER = '99'


class CollInquiryStatus(Enum):
    ACCEPTED = '0'
    ACCEPTED_WITH_WARNINGS = '1'
    COMPLETED = '2'
    COMPLETED_WITH_WARNINGS = '3'
    REJECTED = '4'


class CollStatus(Enum):
    UNASSIGNED = '0'
    PARTIALLY_ASSIGNED = '1'
    ASSIGNMENT_PROPOSED = '2'
    ASSIGNED = '3'
    CHALLENGED = '4'


class CommType(Enum):
    PER_UNIT = '1'
    PERCENTAGE = '2'
    ABSOLUTE = '3'
    FOUR = '4'
    FIVE = '5'
    POINTS_PER_BOND_OR_CONTRACT_SUPPLY_CONTRACTMULTIPLIER = '6'


class ConfirmRejReason(Enum):
    MISMATCHED_ACCOUNT = '1'
    MISSING_SETTLEMENT_INSTRUCTIONS = '2'
    OTHER = '99'


class ConfirmStatus(Enum):
    RECEIVED = '1'
    MISMATCHED_ACCOUNT = '2'
    MISSING_SETTLEMENT_INSTRUCTIONS = '3'
    CONFIRMED = '4'
    REQUEST_REJECTED = '5'


class ConfirmTransType(Enum):
    NEW = '0'
    REPLACE = '1'
    CANCEL = '2'


class ConfirmType(Enum):
    STATUS = '1'
    CONFIRMATION = '2'
    CONFIRMATION_REQUEST_REJECTED = '3'


class ContAmtType(Enum):
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
    FUND_BASED_RENEWAL_COMMISSION_AMOUNT_13 = '13'
    FUND_BASED_RENEWAL_COMMISSION_AMOUNT_14 = '14'
    NET_SETTLEMENT_AMOUNT = '15'


class CorporateAction(Enum):
    EX_DIVIDEND = 'A'
    EX_DISTRIBUTION = 'B'
    EX_RIGHTS = 'C'
    NEW = 'D'
    EX_INTEREST = 'E'


class CoveredOrUncovered(Enum):
    COVERED = '0'
    UNCOVERED = '1'


class CrossPrioritization(Enum):
    NONE = '0'
    BUY_SIDE_IS_PRIORITIZED = '1'
    SELL_SIDE_IS_PRIORITIZED = '2'


class CrossType(Enum):
    CROSS_TRADE_WHICH_IS_EXECUTED_COMPLETELY_OR_NOT_BOTH_SIDES_ARE_TREATED_IN_THE_SAME_MANNER_THIS_IS_EQUIVALENT_TO_AN_ALL_OR_NONE = '1'
    CROSS_TRADE_WHICH_IS_EXECUTED_PARTIALLY_AND_THE_REST_IS_CANCELLED_ONE_SIDE_IS_FULLY_EXECUTED_THE_OTHER_SIDE_IS_PARTIALLY_EXECUTED_WITH_THE_REMAINDER_BEING_CANCELLED_THIS_IS_EQUIVALENT_TO_AN_IMMEDIATE_OR_CANCEL_ON_THE_OTHER_SIDE_NOTE_THE_CROSSPRIORITZATION = '2'
    CROSS_TRADE_WHICH_IS_PARTIALLY_EXECUTED_WITH_THE_UNFILLED_PORTIONS_REMAINING_ACTIVE_ONE_SIDE_OF_THE_CROSS_IS_FULLY_EXECUTED = '3'
    CROSS_TRADE_IS_EXECUTED_WITH_EXISTING_ORDERS_WITH_THE_SAME_PRICE_IN_THE_CASE_OTHER_ORDERS_EXIST_WITH_THE_SAME_PRICE_THE_QUANTITY_OF_THE_CROSS_IS_EXECUTED_AGAINST_THE_EXISTING_ORDERS_AND_QUOTES_THE_REMAINDER_OF_THE_CROSS_IS_EXECUTED_AGAINST_THE_OTHER_SIDE_OF_THE_CROSS_THE_TWO_SIDES_POTENTIALLY_HAVE_DIFFERENT_QUANTITIES = '4'


class CustOrderCapacity(Enum):
    MEMBER_TRADING_FOR_THEIR_OWN_ACCOUNT = '1'
    CLEARING_FIRM_TRADING_FOR_ITS_PROPRIETARY_ACCOUNT = '2'
    MEMBER_TRADING_FOR_ANOTHER_MEMBER = '3'
    ALL_OTHER = '4'


class CxlRejReason(Enum):
    TOO_LATE_TO_CANCEL = '0'
    UNKNOWN_ORDER = '1'
    BROKER = '2'
    ORDER_ALREADY_IN_PENDING_CANCEL_OR_PENDING_REPLACE_STATUS = '3'
    UNABLE_TO_PROCESS_ORDER_MASS_CANCEL_REQUEST = '4'
    ORIGORDMODTIME = '5'
    DUPLICATE_CLORDID = '6'
    OTHER = '99'


class CxlRejResponseTo(Enum):
    ORDER_CANCEL_REQUEST = '1'
    ORDER_CANCEL_REPLACE_REQUEST = '2'


class DKReason(Enum):
    UNKNOWN_SYMBOL = 'A'
    WRONG_SIDE = 'B'
    QUANTITY_EXCEEDS_ORDER = 'C'
    NO_MATCHING_ORDER = 'D'
    PRICE_EXCEEDS_LIMIT = 'E'
    CALCULATION_DIFFERENCE = 'F'
    OTHER = 'Z'


class DayBookingInst(Enum):
    CAN_TRIGGER_BOOKING_WITHOUT_REFERENCE_TO_THE_ORDER_INITIATOR = '0'
    SPEAK_WITH_ORDER_INITIATOR_BEFORE_BOOKING = '1'
    ACCUMULATE = '2'


class DeleteReason(Enum):
    CANCELATION = '0'
    ERROR = '1'


class DeliveryForm(Enum):
    BOOKENTRY = '1'
    BEARER = '2'


class DeliveryType(Enum):
    VERSUS_PAYMENT_DELIVER = '0'
    FREE_DELIVER = '1'
    TRI_PARTY = '2'
    HOLD_IN_CUSTODY = '3'


class DiscretionInst(Enum):
    RELATED_TO_DISPLAYED_PRICE = '0'
    RELATED_TO_MARKET_PRICE = '1'
    RELATED_TO_PRIMARY_PRICE = '2'
    RELATED_TO_LOCAL_PRIMARY_PRICE = '3'
    RELATED_TO_MIDPOINT_PRICE = '4'
    RELATED_TO_LAST_TRADE_PRICE = '5'
    RELATED_TO_VWAP = '6'


class DiscretionLimitType(Enum):
    OR_BETTER = '0'
    STRICT_LIMIT_IS_A_STRICT_LIMIT = '1'
    OR_WORSE_FOR_A_BUY_THE_DISCRETION_PRICE_IS_A_MINIMUM_AND_FOR_A_SELL_THE_DISCRETION_PRICE_IS_A_MAXIMUM = '2'


class DiscretionMoveType(Enum):
    FLOATING = '0'
    FIXED = '1'


class DiscretionOffsetType(Enum):
    PRICE = '0'
    BASIS_POINTS = '1'
    TICKS = '2'
    PRICE_TIER = '3'


class DiscretionRoundDirection(Enum):
    MORE_AGGRESSIVE_ON_A_BUY_ORDER_ROUND_THE_PRICE_UP_ROUND_UP_TO_THE_NEAREST_TICK_ON_A_SELL_ROUND_DOWN_TO_THE_NEAREST_TICK = '1'
    MORE_PASSIVE_ON_A_BUY_ORDER_ROUND_DOWN_TO_NEAREST_TICK_ON_A_SELL_ORDER_ROUND_UP_TO_NEAREST_TICK = '2'


class DiscretionScope(Enum):
    LOCAL = '1'
    NATIONAL = '2'
    GLOBAL = '3'
    NATIONAL_EXCLUDING_LOCAL = '4'


class DistribPaymentMethod(Enum):
    CREST = '1'
    NSCC = '2'
    EUROCLEAR = '3'
    CLEARSTREAM = '4'
    CHEQUE = '5'
    TELEGRAPHIC_TRANSFER = '6'
    FEDWIRE = '7'
    DIRECT_CREDIT = '8'
    ACH_CREDIT = '9'
    BPAY = '10'
    HIGH_VALUE_CLEARING_SYSTEM = '11'
    REINVEST_IN_FUND = '12'


class DlvyInstType(Enum):
    SECURITIES = 'S'
    CASH = 'C'


class DueToRelated(Enum):
    YES = 'Y'
    NO = 'N'


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


class EventType(Enum):
    PUT = '1'
    CALL = '2'
    TENDER = '3'
    SINKING_FUND_CALL = '4'
    OTHER = '99'


class ExchangeForPhysical(Enum):
    YES = 'Y'
    NO = 'N'


class ExecInst(Enum):
    NOT_HELD = '1'
    WORK = '2'
    GO_ALONG = '3'
    OVER_THE_DAY = '4'
    HELD = '5'
    PARTICIPATE_DONT_INITIATE = '6'
    STRICT_SCALE = '7'
    TRY_TO_SCALE = '8'
    STAY_ON_BIDSIDE = '9'
    STAY_ON_OFFERSIDE = '0'
    NO_CROSS = 'A'
    OK_TO_CROSS = 'B'
    CALL_FIRST = 'C'
    PERCENT_OF_VOLUME = 'D'
    DO_NOT_INCREASE = 'E'
    DO_NOT_REDUCE = 'F'
    ALL_OR_NONE = 'G'
    REINSTATE_ON_SYSTEM_FAILURE = 'H'
    INSTITUTIONS_ONLY = 'I'
    REINSTATE_ON_TRADING_HALT = 'J'
    CANCEL_ON_TRADING_HALT = 'K'
    LAST_PEG = 'L'
    MID_PRICE_PEG = 'M'
    NON_NEGOTIABLE = 'N'
    OPENING_PEG = 'O'
    MARKET_PEG = 'P'
    CANCEL_ON_SYSTEM_FAILURE = 'Q'
    PRIMARY_PEG = 'R'
    SUSPEND = 'S'
    CUSTOMER_DISPLAY_INSTRUCTION = 'U'
    NETTING = 'V'
    PEG_TO_VWAP = 'W'
    TRADE_ALONG = 'X'
    TRY_TO_STOP = 'Y'
    CANCEL_IF_NOT_BEST = 'Z'
    TRAILING_STOP_PEG = 'a'
    STRICT_LIMIT = 'b'
    IGNORE_PRICE_VALIDITY_CHECKS = 'c'
    PEG_TO_LIMIT_PRICE = 'd'
    WORK_TO_TARGET_STRATEGY = 'e'


class ExecPriceType(Enum):
    BID_PRICE = 'B'
    CREATION_PRICE = 'C'
    CREATION_PRICE_PLUS_ADJUSTMENT = 'D'
    CREATION_PRICE_PLUS_ADJUSTMENT_AMOUNT = 'E'
    OFFER_PRICE = 'O'
    OFFER_PRICE_MINUS_ADJUSTMENT = 'P'
    OFFER_PRICE_MINUS_ADJUSTMENT_AMOUNT = 'Q'
    SINGLE_PRICE = 'S'


class ExecRestatementReason(Enum):
    GT_CORPORATE_ACTION = '0'
    GT_RENEWAL = '1'
    VERBAL_CHANGE = '2'
    REPRICING_OF_ORDER = '3'
    BROKER_OPTION = '4'
    PARTIAL_DECLINE_OF_ORDERQTY = '5'
    CANCEL_ON_TRADING_HALT = '6'
    CANCEL_ON_SYSTEM_FAILURE = '7'
    MARKET = '8'
    CANCELED_NOT_BEST = '9'
    WAREHOUSE_RECAP = '10'
    OTHER = '99'


class ExecType(Enum):
    NEW = '0'
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
    TRADE = 'F'
    TRADE_CORRECT = 'G'
    TRADE_CANCEL = 'H'
    ORDER_STATUS = 'I'


class ExerciseMethod(Enum):
    AUTOMATIC = 'A'
    MANUAL = 'M'


class ExpirationCycle(Enum):
    EXPIRE_ON_TRADING_SESSION_CLOSE = '0'
    EXPIRE_ON_TRADING_SESSION_OPEN = '1'


class FinancialStatus(Enum):
    BANKRUPT = '1'
    PENDING_DELISTING = '2'


class ForexReq(Enum):
    YES = 'Y'
    NO = 'N'


class FundRenewWaiv(Enum):
    YES = 'Y'
    NO = 'N'


class GTBookingInst(Enum):
    BOOK_OUT_ALL_TRADES_ON_DAY_OF_EXECUTION = '0'
    ACCUMULATE_EXECUTIONS_UNTIL_ORDER_IS_FILLED_OR_EXPIRES = '1'
    ACCUMULATE_UNTIL_VERBALLY_NOTIFIED_OTHERWISE = '2'


class GapFillFlag(Enum):
    YES = 'Y'
    NO = 'N'


class HaltReasonChar(Enum):
    ORDER_IMBALANCE = 'I'
    EQUIPMENT_CHANGEOVER = 'X'
    NEWS_PENDING = 'P'
    NEWS_DISSEMINATION = 'D'
    ORDER_INFLUX = 'E'
    ADDITIONAL_INFORMATION = 'M'


class HandlInst(Enum):
    AUTOMATED_EXECUTION_ORDER_PRIVATE_NO_BROKER_INTERVENTION = '1'
    AUTOMATED_EXECUTION_ORDER_PUBLIC_BROKER_INTERVENTION_OK = '2'
    MANUAL_ORDER_BEST_EXECUTION = '3'


class IOINaturalFlag(Enum):
    YES = 'Y'
    NO = 'N'


class IOIQltyInd(Enum):
    LOW = 'L'
    MEDIUM = 'M'
    HIGH = 'H'


class IOIQty(Enum):
    SMALL = 'S'
    MEDIUM = 'M'
    LARGE = 'L'


class IOIQualifier(Enum):
    ALL_OR_NONE = 'A'
    MARKET_ON_CLOSE = 'B'
    AT_THE_CLOSE = 'C'
    VWAP = 'D'
    IN_TOUCH_WITH = 'I'
    LIMIT = 'L'
    MORE_BEHIND = 'M'
    AT_THE_OPEN = 'O'
    TAKING_A_POSITION = 'P'
    AT_THE_MARKET = 'Q'
    READY_TO_TRADE = 'R'
    PORTFOLIO_SHOWN = 'S'
    THROUGH_THE_DAY = 'T'
    VERSUS = 'V'
    INDICATION = 'W'
    CROSSING_OPPORTUNITY = 'X'
    AT_THE_MIDPOINT = 'Y'
    PRE_OPEN = 'Z'


class IOITransType(Enum):
    NEW = 'N'
    CANCEL = 'C'
    REPLACE = 'R'


class InViewOfCommon(Enum):
    YES = 'Y'
    NO = 'N'


class IncTaxInd(Enum):
    NET = '1'
    GROSS = '2'


class InstrAttribType(Enum):
    FLAT = '1'
    ZERO_COUPON = '2'
    INTEREST_BEARING = '3'
    NO_PERIODIC_PAYMENTS = '4'
    VARIABLE_RATE = '5'
    LESS_FEE_FOR_PUT = '6'
    STEPPED_COUPON = '7'
    COUPON_PERIOD = '8'
    WHEN_AND_IF_ISSUED = '9'
    ORIGINAL_ISSUE_DISCOUNT = '10'
    CALLABLE_PUTTABLE = '11'
    ESCROWED_TO_MATURITY = '12'
    ESCROWED_TO_REDEMPTION_DATE_CALLABLE_SUPPLY_REDEMPTION_DATE_IN_THE_INSTRATTRIBVALUE = '13'
    PREREFUNDED = '14'
    IN_DEFAULT = '15'
    UNRATED = '16'
    TAXABLE = '17'
    INDEXED = '18'
    SUBJECT_TO_ALTERNATIVE_MINIMUM_TAX = '19'
    ORIGINAL_ISSUE_DISCOUNT_PRICE_SUPPLY_PRICE_IN_THE_INSTRATTRIBVALUE = '20'
    CALLABLE_BELOW_MATURITY_VALUE = '21'
    CALLABLE_WITHOUT_NOTICE_BY_MAIL_TO_HOLDER_UNLESS_REGISTERED = '22'
    TEXT_SUPPLY_THE_TEXT_OF_THE_ATTRIBUTE_OR_DISCLAIMER_IN_THE_INSTRATTRIBVALUE = '99'


class LastCapacity(Enum):
    AGENT = '1'
    CROSS_AS_AGENT = '2'
    CROSS_AS_PRINCIPAL = '3'
    PRINCIPAL = '4'


class LastFragment(Enum):
    YES = 'Y'
    NO = 'N'


class LastLiquidityInd(Enum):
    ADDED_LIQUIDITY = '1'
    REMOVED_LIQUIDITY = '2'
    LIQUIDITY_ROUTED_OUT = '3'


class LegSwapType(Enum):
    PAR_FOR_PAR = '1'
    MODIFIED_DURATION = '2'
    RISK = '4'
    PROCEEDS = '5'


class LegalConfirm(Enum):
    YES = 'Y'
    NO = 'N'


class LiquidityIndType(Enum):
    FIVE_DAY_MOVING_AVERAGE = '1'
    TWENTY_DAY_MOVING_AVERAGE = '2'
    NORMAL_MARKET_SIZE = '3'
    OTHER = '4'


class ListExecInstType(Enum):
    IMMEDIATE = '1'
    WAIT_FOR_EXECUTE_INSTRUCTION = '2'
    EXCHANGE_SWITCH_CIV_ORDER_SELL_DRIVEN = '3'
    EXCHANGE_SWITCH_CIV_ORDER_BUY_DRIVEN_CASH_TOP_UP = '4'
    EXCHANGE_SWITCH_CIV_ORDER_BUY_DRIVEN_CASH_WITHDRAW = '5'


class ListOrderStatus(Enum):
    INBIDDINGPROCESS = '1'
    RECEIVEDFOREXECUTION = '2'
    EXECUTING = '3'
    CANCELING = '4'
    ALERT = '5'
    ALL_DONE = '6'
    REJECT = '7'


class ListStatusType(Enum):
    ACK = '1'
    RESPONSE = '2'
    TIMED = '3'
    EXECSTARTED = '4'
    ALLDONE = '5'
    ALERT = '6'


class LocateReqd(Enum):
    YES = 'Y'
    NO = 'N'


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
    IMBALANCE = 'A'
    TRADE_VOLUME = 'B'
    OPEN_INTEREST = 'C'


class MDImplicitDelete(Enum):
    YES = 'Y'
    NO = 'N'


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
    UNSUPPORTED_TRADINGSESSIONID = '9'
    UNSUPPORTED_SCOPE = 'A'
    UNSUPPORTED_OPENCLOSESETTLEFLAG = 'B'
    UNSUPPORTED_MDIMPLICITDELETE = 'C'


class MDUpdateAction(Enum):
    NEW = '0'
    CHANGE = '1'
    DELETE = '2'


class MDUpdateType(Enum):
    FULL_REFRESH = '0'
    INCREMENTAL_REFRESH = '1'


class MassCancelRejectReason(Enum):
    MASS_CANCEL_NOT_SUPPORTED = '0'
    INVALID_OR_UNKNOWN_SECURITY = '1'
    INVALID_OR_UNKNOWN_UNDERLYING = '2'
    INVALID_OR_UNKNOWN_PRODUCT = '3'
    INVALID_OR_UNKNOWN_CFICODE = '4'
    INVALID_OR_UNKNOWN_SECURITY_TYPE = '5'
    INVALID_OR_UNKNOWN_TRADING_SESSION = '6'
    OTHER = '99'


class MassCancelRequestType(Enum):
    CANCEL_ORDERS_FOR_A_SECURITY = '1'
    CANCEL_ORDERS_FOR_AN_UNDERLYING_SECURITY = '2'
    CANCEL_ORDERS_FOR_A_PRODUCT = '3'
    CANCEL_ORDERS_FOR_A_CFICODE = '4'
    CANCEL_ORDERS_FOR_A_SECURITYTYPE = '5'
    CANCEL_ORDERS_FOR_A_TRADING_SESSION = '6'
    CANCEL_ALL_ORDERS = '7'


class MassCancelResponse(Enum):
    CANCEL_REQUEST_REJECTED = '0'
    CANCEL_ORDERS_FOR_A_SECURITY = '1'
    CANCEL_ORDERS_FOR_AN_UNDERLYING_SECURITY = '2'
    CANCEL_ORDERS_FOR_A_PRODUCT = '3'
    CANCEL_ORDERS_FOR_A_CFICODE = '4'
    CANCEL_ORDERS_FOR_A_SECURITYTYPE = '5'
    CANCEL_ORDERS_FOR_A_TRADING_SESSION = '6'
    CANCEL_ALL_ORDERS = '7'


class MassStatusReqType(Enum):
    STATUS_FOR_ORDERS_FOR_A_SECURITY = '1'
    STATUS_FOR_ORDERS_FOR_AN_UNDERLYING_SECURITY = '2'
    STATUS_FOR_ORDERS_FOR_A_PRODUCT = '3'
    STATUS_FOR_ORDERS_FOR_A_CFICODE = '4'
    STATUS_FOR_ORDERS_FOR_A_SECURITYTYPE = '5'
    STATUS_FOR_ORDERS_FOR_A_TRADING_SESSION = '6'
    STATUS_FOR_ALL_ORDERS = '7'
    STATUS_FOR_ORDERS_FOR_A_PARTYID = '8'


class MatchStatus(Enum):
    COMPARED_MATCHED_OR_AFFIRMED = '0'
    UNCOMPARED_UNMATCHED_OR_UNAFFIRMED = '1'
    ADVISORY_OR_ALERT = '2'


class MatchType(Enum):
    EXACT_MATCH_ON_TRADE_DATE_STOCK_SYMBOL_QUANTITY_PRICE_TRADE_TYPE_AND_SPECIAL_TRADE_INDICATOR_PLUS_FOUR_BADGES_AND_EXECUTION_TIME = 'A1'
    EXACT_MATCH_ON_TRADE_DATE_STOCK_SYMBOL_QUANTITY_PRICE_TRADE_TYPE_AND_SPECIAL_TRADE_INDICATOR_PLUS_FOUR_BADGES = 'A2'
    EXACT_MATCH_ON_TRADE_DATE_STOCK_SYMBOL_QUANTITY_PRICE_TRADE_TYPE_AND_SPECIAL_TRADE_INDICATOR_PLUS_TWO_BADGES_AND_EXECUTION_TIME = 'A3'
    EXACT_MATCH_ON_TRADE_DATE_STOCK_SYMBOL_QUANTITY_PRICE_TRADE_TYPE_AND_SPECIAL_TRADE_INDICATOR_PLUS_TWO_BADGES = 'A4'
    EXACT_MATCH_ON_TRADE_DATE_STOCK_SYMBOL_QUANTITY_PRICE_TRADE_TYPE_AND_SPECIAL_TRADE_INDICATOR_PLUS_EXECUTION_TIME = 'A5'
    COMPARED_RECORDS_RESULTING_FROM_STAMPED_ADVISORIES_OR_SPECIALIST_ACCEPTS_PAIR_OFFS = 'AQ'
    SUMMARIZED_MATCH_USING_A1_EXACT_MATCH_CRITERIA_EXCEPT_QUANTITY_IS_SUMMARIZED = 'S1'
    SUMMARIZED_MATCH_USING_A2_EXACT_MATCH_CRITERIA_EXCEPT_QUANTITY_IS_SUMMARIZED = 'S2'
    SUMMARIZED_MATCH_USING_A3_EXACT_MATCH_CRITERIA_EXCEPT_QUANTITY_IS_SUMMARIZED = 'S3'
    SUMMARIZED_MATCH_USING_A4_EXACT_MATCH_CRITERIA_EXCEPT_QUANTITY_IS_SUMMARIZED = 'S4'
    SUMMARIZED_MATCH_USING_A5_EXACT_MATCH_CRITERIA_EXCEPT_QUANTITY_IS_SUMMARIZED = 'S5'
    EXACT_MATCH_ON_TRADE_DATE_STOCK_SYMBOL_QUANTITY_PRICE_TRADE_TYPE_AND_SPECIAL_TRADE_INDICATOR_MINUS_BADGES_AND_TIMES_ACT_M1_MATCH = 'M1'
    SUMMARIZED_MATCH_MINUS_BADGES_AND_TIMES_ACT_M2_MATCH = 'M2'
    OCS_LOCKED_IN_NON_ACT = 'MT'
    ACT_ACCEPTED_TRADE = 'M3'
    ACT_DEFAULT_TRADE = 'M4'
    ACT_DEFAULT_AFTER_M2 = 'M5'
    ACT_M6_MATCH = 'M6'


class MessageEncoding(Enum):
    JIS = 'ISO-2022-JP'
    EUC = 'EUC-JP'
    FOR_USING_SJIS = 'Shift_JIS'
    UNICODE = 'UTF-8'


class MiscFeeBasis(Enum):
    ABSOLUTE = '0'
    PER_UNIT = '1'
    PERCENTAGE = '2'


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
    PER_TRANSACTION = '10'
    CONVERSION = '11'
    AGENT = '12'


class MoneyLaunderingStatus(Enum):
    PASSED = 'Y'
    NOT_CHECKED = 'N'
    EXEMPT_BELOW_THE_LIMIT = '1'
    EXEMPT_CLIENT_MONEY_TYPE_EXEMPTION = '2'
    EXEMPT_AUTHORISED_CREDIT_OR_FINANCIAL_INSTITUTION = '3'


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
    LOGON = 'A'
    NEWS = 'B'
    EMAIL = 'C'
    ORDER_SINGLE = 'D'
    ORDER_LIST = 'E'
    ORDER_CANCEL_REQUEST = 'F'
    ORDER_CANCEL_REPLACE_REQUEST = 'G'
    ORDER_STATUS_REQUEST = 'H'
    ALLOCATION_INSTRUCTION = 'J'
    LIST_CANCEL_REQUEST = 'K'
    LIST_EXECUTE = 'L'
    LIST_STATUS_REQUEST = 'M'
    LIST_STATUS = 'N'
    ALLOCATION_INSTRUCTION_ACK = 'P'
    DONT_KNOW_TRADE = 'Q'
    QUOTE_REQUEST = 'R'
    QUOTE = 'S'
    SETTLEMENT_INSTRUCTIONS = 'T'
    MARKET_DATA_REQUEST = 'V'
    MARKET_DATA_SNAPSHOT_FULL_REFRESH = 'W'
    MARKET_DATA_INCREMENTAL_REFRESH = 'X'
    MARKET_DATA_REQUEST_REJECT = 'Y'
    QUOTE_CANCEL = 'Z'
    QUOTE_STATUS_REQUEST = 'a'
    MASS_QUOTE_ACKNOWLEDGEMENT = 'b'
    SECURITY_DEFINITION_REQUEST = 'c'
    SECURITY_DEFINITION = 'd'
    SECURITY_STATUS_REQUEST = 'e'
    SECURITY_STATUS = 'f'
    TRADING_SESSION_STATUS_REQUEST = 'g'
    TRADING_SESSION_STATUS = 'h'
    MASS_QUOTE = 'i'
    BUSINESS_MESSAGE_REJECT = 'j'
    BID_REQUEST = 'k'
    BID_RESPONSE = 'l'
    LIST_STRIKE_PRICE = 'm'
    XML_MESSAGE = 'n'
    REGISTRATION_INSTRUCTIONS = 'o'
    REGISTRATION_INSTRUCTIONS_RESPONSE = 'p'
    ORDER_MASS_CANCEL_REQUEST = 'q'
    ORDER_MASS_CANCEL_REPORT = 'r'
    NEW_ORDER_S = 's'
    CROSS_ORDER_CANCEL_REPLACE_REQUEST = 't'
    CROSS_ORDER_CANCEL_REQUEST = 'u'
    SECURITY_TYPE_REQUEST = 'v'
    SECURITY_TYPES = 'w'
    SECURITY_LIST_REQUEST = 'x'
    SECURITY_LIST = 'y'
    DERIVATIVE_SECURITY_LIST_REQUEST = 'z'
    DERIVATIVE_SECURITY_LIST = 'AA'
    NEW_ORDER_AB = 'AB'
    MULTILEG_ORDER_CANCEL_REPLACE = 'AC'
    TRADE_CAPTURE_REPORT_REQUEST = 'AD'
    TRADE_CAPTURE_REPORT = 'AE'
    ORDER_MASS_STATUS_REQUEST = 'AF'
    QUOTE_REQUEST_REJECT = 'AG'
    RFQ_REQUEST = 'AH'
    QUOTE_STATUS_REPORT = 'AI'
    QUOTE_RESPONSE = 'AJ'
    CONFIRMATION = 'AK'
    POSITION_MAINTENANCE_REQUEST = 'AL'
    POSITION_MAINTENANCE_REPORT = 'AM'
    REQUEST_FOR_POSITIONS = 'AN'
    REQUEST_FOR_POSITIONS_ACK = 'AO'
    POSITION_REPORT = 'AP'
    TRADE_CAPTURE_REPORT_REQUEST_ACK = 'AQ'
    TRADE_CAPTURE_REPORT_ACK = 'AR'
    ALLOCATION_REPORT = 'AS'
    ALLOCATION_REPORT_ACK = 'AT'
    CONFIRMATION_ACK = 'AU'
    SETTLEMENT_INSTRUCTION_REQUEST = 'AV'
    ASSIGNMENT_REPORT = 'AW'
    COLLATERAL_REQUEST = 'AX'
    COLLATERAL_ASSIGNMENT = 'AY'
    COLLATERAL_RESPONSE = 'AZ'
    COLLATERAL_REPORT = 'BA'
    COLLATERAL_INQUIRY = 'BB'
    NETWORK_BC = 'BC'
    NETWORK_BD = 'BD'
    USER_REQUEST = 'BE'
    USER_RESPONSE = 'BF'
    COLLATERAL_INQUIRY_ACK = 'BG'
    CONFIRMATION_REQUEST = 'BH'


class MultiLegReportingType(Enum):
    SINGLE_SECURITY = '1'
    INDIVIDUAL_LEG_OF_A_MULTI_LEG_SECURITY = '2'
    MULTI_LEG_SECURITY = '3'


class MultiLegRptTypeReq(Enum):
    REPORT_BY_MULITLEG_SECURITY_ONLY = '0'
    REPORT_BY_MULTILEG_SECURITY_AND_BY_INSTRUMENT_LEGS_BELONGING_TO_THE_MULTILEG_SECURITY = '1'
    REPORT_BY_INSTRUMENT_LEGS_BELONGING_TO_THE_MULTILEG_SECURITY_ONLY = '2'


class NetGrossInd(Enum):
    NET = '1'
    GROSS = '2'


class NetworkRequestType(Enum):
    SNAPSHOT = '1'
    SUBSCRIBE = '2'
    STOP_SUBSCRIBING = '4'
    LEVEL_OF_DETAIL_THEN_NOCOMPIDS_BECOMES_REQUIRED = '8'


class NetworkStatusResponseType(Enum):
    FULL = '1'
    INCREMENTAL_UPDATE = '2'


class NoSides(Enum):
    ONE_SIDE = '1'
    BOTH_SIDES = '2'


class NotifyBrokerOfCredit(Enum):
    YES = 'Y'
    NO = 'N'


class OddLot(Enum):
    YES = 'Y'
    NO = 'N'


class OpenCloseSettlFlag(Enum):
    DAILY_OPEN = '0'
    SESSION_OPEN = '1'
    DELIVERY_SETTLEMENT_ENTRY = '2'
    EXPECTED_ENTRY = '3'
    ENTRY_FROM_PREVIOUS_BUSINESS_DAY = '4'
    THEORETICAL_PRICE_VALUE = '5'


class OrdRejReason(Enum):
    BROKER = '0'
    UNKNOWN_SYMBOL = '1'
    EXCHANGE_CLOSED = '2'
    ORDER_EXCEEDS_LIMIT = '3'
    TOO_LATE_TO_ENTER = '4'
    UNKNOWN_ORDER = '5'
    DUPLICATE_ORDER = '6'
    DUPLICATE_OF_A_VERBALLY_COMMUNICATED_ORDER = '7'
    STALE_ORDER = '8'
    TRADE_ALONG_REQUIRED = '9'
    INVALID_INVESTOR_ID = '10'
    UNSUPPORTED_ORDER_CHARACTERISTIC12_SURVEILLENCE_OPTION = '11'
    INCORRECT_QUANTITY = '13'
    INCORRECT_ALLOCATED_QUANTITY = '14'
    UNKNOWN_ACCOUNT = '15'
    OTHER = '99'


class OrdStatus(Enum):
    NEW = '0'
    PARTIALLY_FILLED = '1'
    FILLED = '2'
    DONE_FOR_DAY = '3'
    CANCELED = '4'
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
    WITH_OR_WITHOUT = '6'
    LIMIT_OR_BETTER = '7'
    LIMIT_WITH_OR_WITHOUT = '8'
    ON_BASIS = '9'
    PREVIOUSLY_QUOTED = 'D'
    PREVIOUSLY_INDICATED = 'E'
    FOREX = 'G'
    FUNARI = 'I'
    MARKET_IF_TOUCHED = 'J'
    MARKET_WITH_LEFTOVER_AS_LIMIT = 'K'
    PREVIOUS_FUND_VALUATION_POINT = 'L'
    NEXT_FUND_VALUATION_POINT = 'M'
    PEGGED = 'P'


class OrderCapacity(Enum):
    AGENCY = 'A'
    PROPRIETARY = 'G'
    INDIVIDUAL = 'I'
    PRINCIPAL = 'P'
    RISKLESS_PRINCIPAL = 'R'
    AGENT_FOR_OTHER_MEMBER = 'W'


class OrderRestrictions(Enum):
    PROGRAM_TRADE = '1'
    INDEX_ARBITRAGE = '2'
    NON_INDEX_ARBITRAGE = '3'
    COMPETING_MARKET_MAKER = '4'
    ACTING_AS_MARKET_MAKER_OR_SPECIALIST_IN_THE_SECURITY = '5'
    ACTING_AS_MARKET_MAKER_OR_SPECIALIST_IN_THE_UNDERLYING_SECURITY_OF_A_DERIVATIVE_SECURITY = '6'
    FOREIGN_ENTITY = '7'
    EXTERNAL_MARKET_PARTICIPANT = '8'
    EXTERNAL_INTER_CONNECTED_MARKET_LINKAGE = '9'
    RISKLESS_ARBITRAGE = 'A'


class OwnerType(Enum):
    INDIVIDUAL_INVESTOR = '1'
    PUBLIC_COMPANY = '2'
    PRIVATE_COMPANY = '3'
    INDIVIDUAL_TRUSTEE = '4'
    COMPANY_TRUSTEE = '5'
    PENSION_PLAN = '6'
    CUSTODIAN_UNDER_GIFTS_TO_MINORS_ACT = '7'
    TRUSTS = '8'
    FIDUCIARIES = '9'
    NETWORKING_SUB_ACCOUNT = '10'
    NON_PROFIT_ORGANIZATION = '11'
    CORPORATE_BODY = '12'
    NOMINEE = '13'


class OwnershipType(Enum):
    JOINT_INVESTORS = 'J'
    TENANTS_IN_COMMON = 'T'
    JOINT_TRUSTEES = '2'


class PartyIDSource(Enum):
    BIC = 'B'
    GENERALLY_ACCEPTED_MARKET_PARTICIPANT_IDENTIFIER = 'C'
    PROPRIETARY_CUSTOM_CODE = 'D'
    ISO_COUNTRY_CODE = 'E'
    SETTLEMENT_ENTITY_LOCATION = 'F'
    MIC = 'G'
    CSD_PARTICIPANT_MEMBER_CODE = 'H'
    KOREAN_INVESTOR_ID = '1'
    TAIWANESE_QUALIFIED_FOREIGN_INVESTOR_ID_QFII = '2'
    TAIWANESE_TRADING_ACCOUNT = '3'
    MALAYSIAN_CENTRAL_DEPOSITORY = '4'
    CHINESE_B_SHARE = '5'
    UK_NATIONAL_INSURANCE_OR_PENSION_NUMBER = '6'
    US_SOCIAL_SECURITY_NUMBER = '7'
    US_EMPLOYER_IDENTIFICATION_NUMBER = '8'
    AUSTRALIAN_BUSINESS_NUMBER = '9'
    AUSTRALIAN_TAX_FILE_NUMBER = 'A'
    DIRECTED_BROKER_THREE_CHARACTER_ACRONYM_AS_DEFINED_IN_ISITC_ETC_BEST_PRACTICE_GUIDELINES_DOCUMENT = 'I'


class PartyRole(Enum):
    EXECUTING_FIRM = '1'
    BROKER_OF_CREDIT = '2'
    CLIENT_ID = '3'
    CLEARING_FIRM = '4'
    INVESTOR_ID = '5'
    INTRODUCING_FIRM = '6'
    ENTERING_FIRM = '7'
    LOCATE_LENDING_FIRM = '8'
    FUND_MANAGER_CLIENT_ID = '9'
    SETTLEMENT_LOCATION = '10'
    ORDER_ORIGINATION_TRADER = '11'
    EXECUTING_TRADER = '12'
    ORDER_ORIGINATION_FIRM = '13'
    GIVEUP_CLEARING_FIRM = '14'
    CORRESPONDANT_CLEARING_FIRM = '15'
    EXECUTING_SYSTEM = '16'
    CONTRA_FIRM = '17'
    CONTRA_CLEARING_FIRM = '18'
    SPONSORING_FIRM = '19'
    UNDERLYING_CONTRA_FIRM = '20'
    CLEARING_ORGANIZATION = '21'
    EXCHANGE = '22'
    CUSTOMER_ACCOUNT = '24'
    CORRESPONDENT_CLEARING_ORGANIZATION = '25'
    CORRESPONDENT_BROKER = '26'
    BUYER_SELLER = '27'
    CUSTODIAN = '28'
    INTERMEDIARY = '29'
    AGENT = '30'
    SUB_CUSTODIAN = '31'
    BENEFICIARY = '32'
    INTERESTED_PARTY = '33'
    REGULATORY_BODY = '34'
    LIQUIDITY_PROVIDER = '35'
    ENTERING_TRADER = '36'
    CONTRA_TRADER = '37'
    POSITION_ACCOUNT = '38'


class PartySubIDType(Enum):
    FIRM = '1'
    PERSON = '2'
    SYSTEM = '3'
    APPLICATION = '4'
    FULL_LEGAL_NAME_OF_FIRM = '5'
    POSTAL_ADDRESS = '6'
    PHONE_NUMBER = '7'
    EMAIL_ADDRESS = '8'
    CONTACT_NAME = '9'
    SECURITIES_ACCOUNT_NUMBER = '10'
    REGISTRATION_NUMBER = '11'
    REGISTERED_ADDRESS_12 = '12'
    REGULATORY_STATUS = '13'
    REGISTRATION_NAME = '14'
    CASH_ACCOUNT_NUMBER = '15'
    BIC = '16'
    CSD_PARTICIPANT_MEMBER_CODE = '17'
    REGISTERED_ADDRESS_18 = '18'
    FUND_ACCOUNT_NAME = '19'
    TELEX_NUMBER = '20'
    FAX_NUMBER = '21'
    SECURITIES_ACCOUNT_NAME = '22'
    CASH_ACCOUNT_NAME = '23'
    DEPARTMENT = '24'
    LOCATION = '25'
    POSITION_ACCOUNT_TYPE = '26'


class PaymentMethod(Enum):
    CREST = '1'
    NSCC = '2'
    EUROCLEAR = '3'
    CLEARSTREAM = '4'
    CHEQUE = '5'
    TELEGRAPHIC_TRANSFER = '6'
    FEDWIRE = '7'
    DEBIT_CARD = '8'
    DIRECT_DEBIT = '9'
    DIRECT_CREDIT = '10'
    CREDIT_CARD = '11'
    ACH_DEBIT = '12'
    ACH_CREDIT = '13'
    BPAY = '14'
    HIGH_VALUE_CLEARING_SYSTEM = '15'


class PegLimitType(Enum):
    OR_BETTER = '0'
    STRICT_LIMIT_IS_A_STRICT_LIMIT = '1'
    OR_WORSE_FOR_A_BUY_THE_PEG_LIMIT_IS_A_MINIMUM_AND_FOR_A_SELL_THE_PEG_LIMIT_IS_A_MAXIMUM = '2'


class PegMoveType(Enum):
    FLOATING = '0'
    FIXED = '1'


class PegOffsetType(Enum):
    PRICE = '0'
    BASIS_POINTS = '1'
    TICKS = '2'
    PRICE_TIER = '3'


class PegRoundDirection(Enum):
    MORE_AGGRESSIVE_ON_A_BUY_ORDER_ROUND_THE_PRICE_UP_ROUND_UP_TO_THE_NEAREST_TICK_ON_A_SELL_ROUND_DOWN_TO_THE_NEAREST_TICK = '1'
    MORE_PASSIVE_ON_A_BUY_ORDER_ROUND_DOWN_TO_NEAREST_TICK_ON_A_SELL_ORDER_ROUND_UP_TO_NEAREST_TICK = '2'


class PegScope(Enum):
    LOCAL = '1'
    NATIONAL = '2'
    GLOBAL = '3'
    NATIONAL_EXCLUDING_LOCAL = '4'


class PosAmtType(Enum):
    FINAL_MARK_TO_MARKET_AMOUNT = 'FMTM'
    INCREMENTAL_MARK_TO_MARKET_AMOUNT = 'IMTM'
    TRADE_VARIATION_AMOUNT = 'TVAR'
    START_OF_DAY_MARK_TO_MARKET_AMOUNT = 'SMTM'
    PREMIUM_AMOUNT = 'PREM'
    CASH_RESIDUAL_AMOUNT = 'CRES'
    CASH_AMOUNT = 'CASH'
    VALUE_ADJUSTED_AMOUNT = 'VADJ'


class PosMaintAction(Enum):
    NEW_USED_TO_INCREMENT_THE_OVERALL_TRANSACTION_QUANTITY = '1'
    REPLACE_USED_TO_OVERRIDE_THE_OVERALL_TRANSACTION_QUANTITY_OR_SPECIFIC_ADD_MESSAGES_BASED_ON_THE_REFERENCE_ID = '2'
    CANCEL_USED_TO_REMOVE_THE_OVERALL_TRANSACTION_OR_SPECIFIC_ADD_MESSAGES_BASED_ON_REFERENCE_ID = '3'


class PosMaintResult(Enum):
    SUCCESSFUL_COMPLETION = '0'
    REJECTED = '1'
    OTHER = '99'


class PosMaintStatus(Enum):
    ACCEPTED = '0'
    ACCEPTED_WITH_WARNINGS = '1'
    REJECTED = '2'
    COMPLETED = '3'
    COMPLETED_WITH_WARNINGS = '4'


class PosQtyStatus(Enum):
    SUBMITTED = '0'
    ACCEPTED = '1'
    REJECTED = '2'


class PosReqResult(Enum):
    VALID_REQUEST = '0'
    INVALID_OR_UNSUPPORTED_REQUEST = '1'
    NO_POSITIONS_FOUND_THAT_MATCH_CRITERIA = '2'
    NOT_AUTHORIZED_TO_REQUEST_POSITIONS = '3'
    REQUEST_FOR_POSITION_NOT_SUPPORTED = '4'
    OTHER = '99'


class PosReqStatus(Enum):
    COMPLETED = '0'
    COMPLETED_WITH_WARNINGS = '1'
    REJECTED = '2'


class PosReqType(Enum):
    POSITIONS = '0'
    TRADES = '1'
    EXERCISES = '2'
    ASSIGNMENTS = '3'


class PosTransType(Enum):
    EXERCISE = '1'
    DO_NOT_EXERCISE = '2'
    POSITION_ADJUSTMENT = '3'
    POSITION_CHANGE_SUBMISSION_MARGIN_DISPOSITION = '4'
    PLEDGE = '5'


class PosType(Enum):
    TRANSACTION_QUANTITY = 'TQ'
    INTRA_SPREAD_QTY = 'IAS'
    INTER_SPREAD_QTY = 'IES'
    END_OF_DAY_QTY = 'FIN'
    START_OF_DAY_QTY = 'SOD'
    OPTION_EXERCISE_QTY = 'EX'
    OPTION_ASSIGNMENT = 'AS'
    TRANSACTION_FROM_EXERCISE = 'TX'
    TRANSACTION_FROM_ASSIGNMENT = 'TA'
    PIT_TRADE_QTY = 'PIT'
    TRANSFER_TRADE_QTY = 'TRF'
    ELECTRONIC_TRADE_QTY = 'ETR'
    ALLOCATION_TRADE_QTY = 'ALC'
    ADJUSTMENT_QTY = 'PA'
    AS_OF_TRADE_QTY = 'ASF'
    DELIVERY_QTY = 'DLV'
    TOTAL_TRANSACTION_QTY = 'TOT'
    CROSS_MARGIN_QTY = 'XM'
    INTEGRAL_SPLIT = 'SPL'


class PositionEffect(Enum):
    OPEN = 'O'
    CLOSE = 'C'
    ROLLED = 'R'
    FIFO = 'F'


class PossDupFlag(Enum):
    YES = 'Y'
    NO = 'N'


class PossResend(Enum):
    YES = 'Y'
    NO = 'N'


class PreallocMethod(Enum):
    PRO_RATA = '0'
    DO_NOT_PRO_RATA_DISCUSS_FIRST = '1'


class PreviouslyReported(Enum):
    YES = 'Y'
    NO = 'N'


class PriceType(Enum):
    PERCENTAGE = '1'
    PER_UNIT = '2'
    FIXED_AMOUNT = '3'
    DISCOUNT_PERCENTAGE_POINTS_BELOW_PAR = '4'
    PREMIUM_PERCENTAGE_POINTS_OVER_PAR = '5'
    SPREAD = '6'
    TED_PRICE = '7'
    TED_YIELD = '8'
    YIELD = '9'
    FIXED_CABINET_TRADE_PRICE = '10'
    VARIABLE_CABINET_TRADE_PRICE = '11'


class PriorityIndicator(Enum):
    PRIORITY_UNCHANGED = '0'
    LOST_PRIORITY_AS_RESULT_OF_ORDER_CHANGE = '1'


class ProcessCode(Enum):
    REGULAR = '0'
    SOFT_DOLLAR = '1'
    STEP_IN = '2'
    STEP_OUT = '3'
    SOFT_DOLLAR_STEP_IN = '4'
    SOFT_DOLLAR_STEP_OUT = '5'
    PLAN_SPONSOR = '6'


class Product(Enum):
    AGENCY = '1'
    COMMODITY = '2'
    CORPORATE = '3'
    CURRENCY = '4'
    EQUITY = '5'
    GOVERNMENT = '6'
    INDEX = '7'
    LOAN = '8'
    MONEYMARKET = '9'
    MORTGAGE = '10'
    MUNICIPAL = '11'
    OTHER = '12'
    FINANCING = '13'


class ProgRptReqs(Enum):
    BUYSIDE_EXPLICITLY_REQUESTS_STATUS_USING_STATUSREQUEST = '1'
    SELLSIDE_PERIODICALLY_SENDS_STATUS_USING_LISTSTATUS_PERIOD_OPTIONALLY_SPECIFIED_IN_PROGRESSPERIOD = '2'
    REAL_TIME_EXECUTION_REPORTS = '3'


class PublishTrdIndicator(Enum):
    YES = 'Y'
    NO = 'N'


class PutOrCall(Enum):
    PUT = '0'
    CALL = '1'


class QtyType(Enum):
    UNITS = '0'
    CONTRACTS = '1'


class QuoteCancelType(Enum):
    CANCEL_FOR_SYMBOL = '1'
    CANCEL_FOR_SECURITY_TYPE = '2'
    CANCEL_FOR_UNDERLYING_SYMBOL = '3'
    CANCEL_ALL_QUOTES = '4'


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


class QuotePriceType(Enum):
    PERCENT = '1'
    PER_SHARE = '2'
    FIXED_AMOUNT = '3'
    DISCOUNT_PERCENTAGE_POINTS_BELOW_PAR = '4'
    PREMIUM_PERCENTAGE_POINTS_OVER_PAR = '5'
    BASIS_POINTS_RELATIVE_TO_BENCHMARK = '6'
    TED_PRICE = '7'
    TED_YIELD = '8'
    YIELD_SPREAD = '9'
    YIELD = '10'


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
    OTHER = '99'


class QuoteRequestRejectReason(Enum):
    UNKNOWN_SYMBOL = '1'
    EXCHANGE = '2'
    QUOTE_REQUEST_EXCEEDS_LIMIT = '3'
    TOO_LATE_TO_ENTER = '4'
    INVALID_PRICE = '5'
    NOT_AUTHORIZED_TO_REQUEST_QUOTE = '6'
    NO_MATCH_FOR_INQUIRY = '7'
    NO_MARKET_FOR_INSTRUMENT = '8'
    NO_INVENTORY = '9'
    PASS = '10'
    OTHER = '99'


class QuoteRequestType(Enum):
    MANUAL = '1'
    AUTOMATIC = '2'


class QuoteRespType(Enum):
    HIT_LIFT = '1'
    COUNTER = '2'
    EXPIRED = '3'
    COVER = '4'
    DONE_AWAY = '5'
    PASS = '6'


class QuoteResponseLevel(Enum):
    NO_ACKNOWLEDGEMENT = '0'
    ACKNOWLEDGE_ONLY_NEGATIVE_OR_ERRONEOUS_QUOTES = '1'
    ACKNOWLEDGE_EACH_QUOTE_MESSAGES = '2'


class QuoteStatus(Enum):
    ACCEPTED = '0'
    CANCELED_FOR_SYMBOL = '1'
    CANCELED_FOR_SECURITY_TYPE = '2'
    CANCELED_FOR_UNDERLYING = '3'
    CANCELED_ALL = '4'
    REJECTED = '5'
    REMOVED_FROM_MARKET = '6'
    EXPIRED = '7'
    QUERY = '8'
    QUOTE_NOT_FOUND = '9'
    PENDING = '10'
    PASS = '11'
    LOCKED_MARKET_WARNING = '12'
    CROSS_MARKET_WARNING = '13'
    CANCELED_DUE_TO_LOCK_MARKET = '14'
    CANCELED_DUE_TO_CROSS_MARKET = '15'


class QuoteType(Enum):
    INDICATIVE = '0'
    TRADEABLE = '1'
    RESTRICTED_TRADEABLE = '2'
    COUNTER = '3'


class RegistRejReasonCode(Enum):
    INVALID_UNACCEPTABLE_ACCOUNT_TYPE = '1'
    INVALID_UNACCEPTABLE_TAX_EXEMPT_TYPE = '2'
    INVALID_UNACCEPTABLE_OWNERSHIP_TYPE = '3'
    INVALID_UNACCEPTABLE_NO_REG_DETLS = '4'
    INVALID_UNACCEPTABLE_REG_SEQ_NO = '5'
    INVALID_UNACCEPTABLE_REG_DTLS = '6'
    INVALID_UNACCEPTABLE_MAILING_DTLS = '7'
    INVALID_UNACCEPTABLE_MAILING_INST = '8'
    INVALID_UNACCEPTABLE_INVESTOR_ID = '9'
    INVALID_UNACCEPTABLE_INVESTOR_ID_SOURCE = '10'
    INVALID_UNACCEPTABLE_DATE_OF_BIRTH = '11'
    INVALID_UNACCEPTABLE_INVESTOR_COUNTRY_OF_RESIDENCE = '12'
    INVALID_UNACCEPTABLE_NODISTRIBINSTNS = '13'
    INVALID_UNACCEPTABLE_DISTRIB_PERCENTAGE = '14'
    INVALID_UNACCEPTABLE_DISTRIB_PAYMENT_METHOD = '15'
    INVALID_UNACCEPTABLE_CASH_DISTRIB_AGENT_ACCT_NAME = '16'
    INVALID_UNACCEPTABLE_CASH_DISTRIB_AGENT_CODE = '17'
    INVALID_UNACCEPTABLE_CASH_DISTRIB_AGENT_ACCT_NUM = '18'
    OTHER = '99'


class RegistStatus(Enum):
    ACCEPTED = 'A'
    REJECTED = 'R'
    HELD = 'H'
    REMINDER_IE_REGISTRATION_INSTRUCTIONS_ARE_STILL_OUTSTANDING = 'N'


class RegistTransType(Enum):
    NEW = '0'
    REPLACE = '1'
    CANCEL = '2'


class ReportToExch(Enum):
    YES = 'Y'
    NO = 'N'


class ResetSeqNumFlag(Enum):
    YES = 'Y'
    NO = 'N'


class ResponseTransportType(Enum):
    INBAND_TRANSPORT_THE_REQUEST_WAS_SENT_OVER = '0'
    OUT_OF_BAND_PRE_ARRANGED_OUT_OF_BAND_DELIVERY_MECHANISM = '1'


class RoundingDirection(Enum):
    ROUND_TO_NEAREST = '0'
    ROUND_DOWN = '1'
    ROUND_UP = '2'


class RoutingType(Enum):
    TARGET_FIRM = '1'
    TARGET_LIST = '2'
    BLOCK_FIRM = '3'
    BLOCK_LIST = '4'


class Scope(Enum):
    LOCAL = '1'
    NATIONAL = '2'
    GLOBAL = '3'


class SecurityIDSource(Enum):
    CUSIP = '1'
    SEDOL = '2'
    QUIK = '3'
    ISIN_NUMBER = '4'
    RIC_CODE = '5'
    ISO_CURRENCY_CODE = '6'
    ISO_COUNTRY_CODE = '7'
    EXCHANGE_SYMBOL = '8'
    CONSOLIDATED_TAPE_ASSOCIATION = '9'
    BLOOMBERG_SYMBOL = 'A'
    WERTPAPIER = 'B'
    DUTCH = 'C'
    VALOREN = 'D'
    SICOVAM = 'E'
    BELGIAN = 'F'
    COMMON = 'G'
    CLEARING_HOUSE = 'H'
    ISDA_FPML_PRODUCT_SPECIFICATION = 'I'
    OPTIONS_PRICE_REPORTING_AUTHORITY = 'J'


class SecurityListRequestType(Enum):
    SYMBOL = '0'
    SECURITYTYPE_AND_OR_CFICODE = '1'
    PRODUCT = '2'
    TRADINGSESSIONID = '3'
    ALL_SECURITIES = '4'


class SecurityRequestResult(Enum):
    VALID_REQUEST = '0'
    INVALID_OR_UNSUPPORTED_REQUEST = '1'
    NO_INSTRUMENTS_FOUND_THAT_MATCH_SELECTION_CRITERIA = '2'
    NOT_AUTHORIZED_TO_RETRIEVE_INSTRUMENT_DATA = '3'
    INSTRUMENT_DATA_TEMPORARILY_UNAVAILABLE = '4'
    REQUEST_FOR_INSTRUMENT_DATA_NOT_SUPPORTED = '5'


class SecurityRequestType(Enum):
    REQUEST_SECURITY_IDENTITY_AND_SPECIFICATIONS = '0'
    REQUEST_SECURITY_IDENTITY_FOR_THE_SPECIFICATIONS_PROVIDED = '1'
    REQUEST_LIST_SECURITY_TYPES = '2'
    REQUEST_LIST_SECURITIES = '3'


class SecurityResponseType(Enum):
    ACCEPT_SECURITY_PROPOSAL_AS_IS = '1'
    ACCEPT_SECURITY_PROPOSAL_WITH_REVISIONS_AS_INDICATED_IN_THE_MESSAGE = '2'
    REJECT_SECURITY_PROPOSAL = '5'
    CAN_NOT_MATCH_SELECTION_CRITERIA = '6'


class SecurityTradingStatus(Enum):
    OPENING_DELAY = '1'
    TRADING_HALT = '2'
    RESUME = '3'
    NO_OPEN_NO_RESUME = '4'
    PRICE_INDICATION = '5'
    TRADING_RANGE_INDICATION = '6'
    MARKET_IMBALANCE_BUY = '7'
    MARKET_IMBALANCE_SELL = '8'
    MARKET_ON_CLOSE_IMBALANCE_BUY = '9'
    MARKET_ON_CLOSE_IMBALANCE_SELL = '10'
    NO_MARKET_IMBALANCE = '12'
    NO_MARKET_ON_CLOSE_IMBALANCE = '13'
    ITS_PRE_OPENING = '14'
    NEW_PRICE_INDICATION = '15'
    TRADE_DISSEMINATION_TIME = '16'
    READY_TO_TRADE = '17'
    NOT_AVAILABLE_FOR_TRADING = '18'
    NOT_TRADED_ON_THIS_MARKET = '19'
    UNKNOWN_OR_INVALID = '20'
    PRE_OPEN = '21'
    OPENING_ROTATION = '22'
    FAST_MARKET = '23'


class SecurityType(Enum):
    FUTURE = 'FUT'
    OPTION = 'OPT'
    EURO_SUPRANATIONAL_COUPONS = 'EUSUPRA'
    FEDERAL_AGENCY_COUPON = 'FAC'
    FEDERAL_AGENCY_DISCOUNT_NOTE = 'FADN'
    PRIVATE_EXPORT_FUNDING = 'PEF'
    USD_SUPRANATIONAL_COUPONS = 'SUPRA'
    CORPORATE_BOND = 'CORP'
    CORPORATE_PRIVATE_PLACEMENT = 'CPP'
    CONVERTIBLE_BOND = 'CB'
    DUAL_CURRENCY = 'DUAL'
    EURO_CORPORATE_BOND = 'EUCORP'
    INDEXED_LINKED = 'XLINKD'
    STRUCTURED_NOTES = 'STRUCT'
    YANKEE_CORPORATE_BOND = 'YANK'
    FOREIGN_EXCHANGE_CONTRACT = 'FOR'
    COMMON_STOCK = 'CS'
    PREFERRED_STOCK = 'PS'
    BRADY_BOND = 'BRADY'
    EURO_SOVEREIGNS = 'EUSOV'
    US_TREASURY_BOND = 'TBOND'
    INTEREST_STRIP_FROM_ANY_BOND_OR_NOTE = 'TINT'
    TREASURY_INFLATION_PROTECTED_SECURITIES = 'TIPS'
    PRINCIPAL_STRIP_OF_A_CALLABLE_BOND_OR_NOTE = 'TCAL'
    PRINCIPAL_STRIP_FROM_A_NON_CALLABLE_BOND_OR_NOTE = 'TPRN'
    US_TREASURY_NOTE_UST = 'UST'
    US_TREASURY_BILL_USTB = 'USTB'
    US_TREASURY_NOTE_TNOTE = 'TNOTE'
    US_TREASURY_BILL_TBILL = 'TBILL'
    REPURCHASE = 'REPO'
    FORWARD = 'FORWARD'
    BUY_SELLBACK = 'BUYSELL'
    SECURITIES_LOAN = 'SECLOAN'
    SECURITIES_PLEDGE = 'SECPLEDGE'
    TERM_LOAN = 'TERM'
    REVOLVER_LOAN = 'RVLV'
    REVOLVER_TERM_LOAN = 'RVLVTRM'
    BRIDGE_LOAN = 'BRIDGE'
    LETTER_OF_CREDIT = 'LOFC'
    SWING_LINE_FACILITY = 'SWING'
    DEBTOR_IN_POSSESSION = 'DINP'
    DEFAULTED = 'DEFLTED'
    WITHDRAWN = 'WITHDRN'
    REPLACED = 'REPLACD'
    MATURED = 'MATURED'
    AMENDED_RESTATED = 'AMENDED'
    RETIRED = 'RETIRED'
    BANKERS_ACCEPTANCE = 'BA'
    BANK_NOTES = 'BN'
    BILL_OF_EXCHANGES = 'BOX'
    CERTIFICATE_OF_DEPOSIT = 'CD'
    CALL_LOANS = 'CL'
    COMMERCIAL_PAPER = 'CP'
    DEPOSIT_NOTES = 'DN'
    EURO_CERTIFICATE_OF_DEPOSIT = 'EUCD'
    EURO_COMMERCIAL_PAPER = 'EUCP'
    LIQUIDITY_NOTE = 'LQN'
    MEDIUM_TERM_NOTES = 'MTN'
    OVERNIGHT = 'ONITE'
    PROMISSORY_NOTE = 'PN'
    PLAZOS_FIJOS = 'PZFJ'
    SHORT_TERM_LOAN_NOTE = 'STN'
    TIME_DEPOSIT = 'TD'
    EXTENDED_COMM_NOTE = 'XCN'
    YANKEE_CERTIFICATE_OF_DEPOSIT = 'YCD'
    ASSET_BACKED_SECURITIES = 'ABS'
    CORP_MORTGAGE_BACKED_SECURITIES = 'CMBS'
    COLLATERALIZED_MORTGAGE_OBLIGATION = 'CMO'
    IOETTE_MORTGAGE = 'IET'
    MORTGAGE_BACKED_SECURITIES = 'MBS'
    MORTGAGE_INTEREST_ONLY = 'MIO'
    MORTGAGE_PRINCIPAL_ONLY = 'MPO'
    MORTGAGE_PRIVATE_PLACEMENT = 'MPP'
    MISCELLANEOUS_PASS_THROUGH = 'MPT'
    PFANDBRIEFE = 'PFAND'
    TO_BE_ANNOUNCED = 'TBA'
    OTHER_ANTICIPATION_NOTES_BAN_GAN_ETC = 'AN'
    CERTIFICATE_OF_OBLIGATION = 'COFO'
    CERTIFICATE_OF_PARTICIPATION = 'COFP'
    GENERAL_OBLIGATION_BONDS = 'GO'
    MANDATORY_TENDER = 'MT'
    REVENUE_ANTICIPATION_NOTE = 'RAN'
    REVENUE_BONDS = 'REV'
    SPECIAL_ASSESSMENT = 'SPCLA'
    SPECIAL_OBLIGATION = 'SPCLO'
    SPECIAL_TAX = 'SPCLT'
    TAX_ANTICIPATION_NOTE = 'TAN'
    TAX_ALLOCATION = 'TAXA'
    TAX_EXEMPT_COMMERCIAL_PAPER = 'TECP'
    TAX_REVENUE_ANTICIPATION_NOTE = 'TRAN'
    VARIABLE_RATE_DEMAND_NOTE = 'VRDN'
    WARRANT = 'WAR'
    MUTUAL_FUND = 'MF'
    MULTI_LEG_INSTRUMENT = 'MLEG'
    NO_SECURITY_TYPE = 'NONE'


class SessionRejectReason(Enum):
    INVALID_TAG_NUMBER = '0'
    REQUIRED_TAG_MISSING = '1'
    TAG_NOT_DEFINED_FOR_THIS_MESSAGE_TYPE = '2'
    UNDEFINED_TAG = '3'
    TAG_SPECIFIED_WITHOUT_A_VALUE = '4'
    VALUE_IS_INCORRECT = '5'
    INCORRECT_DATA_FORMAT_FOR_VALUE = '6'
    DECRYPTION_PROBLEM = '7'
    SIGNATURE_PROBLEM = '8'
    COMPID_PROBLEM = '9'
    SENDINGTIME_ACCURACY_PROBLEM = '10'
    INVALID_MSGTYPE = '11'
    XML_VALIDATION_ERROR = '12'
    TAG_APPEARS_MORE_THAN_ONCE = '13'
    TAG_SPECIFIED_OUT_OF_REQUIRED_ORDER = '14'
    REPEATING_GROUP_FIELDS_OUT_OF_ORDER = '15'
    INCORRECT_NUMINGROUP_COUNT_FOR_REPEATING_GROUP = '16'
    NON_DATA_VALUE_INCLUDES_FIELD_DELIMITER = '17'
    OTHER = '99'


class SettlCurrFxRateCalc(Enum):
    MULTIPLY = 'M'
    DIVIDE = 'D'


class SettlDeliveryType(Enum):
    VERSUS_PAYMENT_DELIVER = '0'
    FREE_DELIVER = '1'
    TRI_PARTY = '2'
    HOLD_IN_CUSTODY = '3'


class SettlInstMode(Enum):
    STANDING_INSTRUCTIONS_PROVIDED = '1'
    SPECIFIC_ORDER_FOR_A_SINGLE_ACCOUNT = '4'
    REQUEST_REJECT = '5'


class SettlInstReqRejCode(Enum):
    UNABLE_TO_PROCESS_REQUEST = '0'
    UNKNOWN_ACCOUNT = '1'
    NO_MATCHING_SETTLEMENT_INSTRUCTIONS_FOUND = '2'
    OTHER = '99'


class SettlInstSource(Enum):
    BROKERS_INSTRUCTIONS = '1'
    INSTITUTIONS_INSTRUCTIONS = '2'
    INVESTOR = '3'


class SettlInstTransType(Enum):
    NEW = 'N'
    CANCEL = 'C'
    REPLACE = 'R'
    RESTATE = 'T'


class SettlPriceType(Enum):
    FINAL = '1'
    THEORETICAL = '2'


class SettlSessID(Enum):
    INTRADAY = 'ITD'
    REGULAR_TRADING_HOURS = 'RTH'
    ELECTRONIC_TRADING_HOURS = 'ETH'


class SettlType(Enum):
    REGULAR = '0'
    CASH = '1'
    NEXT_DAY = '2'
    T_PLUS_2 = '3'
    T_PLUS_3 = '4'
    T_PLUS_4 = '5'
    FUTURE = '6'
    WHEN_AND_IF_ISSUED = '7'
    SELLERS_OPTION = '8'
    T_PLUS_5 = '9'


class ShortSaleReason(Enum):
    DEALER_SOLD_SHORT = '0'
    DEALER_SOLD_SHORT_EXEMPT = '1'
    SELLING_CUSTOMER_SOLD_SHORT = '2'
    SELLING_CUSTOMER_SOLD_SHORT_EXEMPT = '3'
    QUALIFED_SERVICE_REPRESENTATIVE = '4'
    QSR_OR_AGU_CONTRA_SIDE_SOLD_SHORT_EXEMPT = '5'


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
    CROSS_SHORT_EXEMPT = 'A'
    AS_DEFINED = 'B'
    OPPOSITE = 'C'
    SUBSCRIBE = 'D'
    REDEEM = 'E'
    LEND = 'F'
    BORROW = 'G'


class SideMultiLegReportingType(Enum):
    SINGLE_SECURITY = '1'
    INDIVIDUAL_LEG_OF_A_MULTI_LEG_SECURITY = '2'
    MULTI_LEG_SECURITY = '3'


class SideValueInd(Enum):
    SIDEVALUE1 = '1'
    SIDEVALUE_2 = '2'


class SolicitedFlag(Enum):
    YES = 'Y'
    NO = 'N'


class StandInstDbType(Enum):
    OTHER = '0'
    DTC_SID = '1'
    THOMSON_ALERT = '2'
    A_GLOBAL_CUSTODIAN = '3'
    ACCOUNTNET = '4'


class StatusValue(Enum):
    CONNECTED = '1'
    NOT_CONNECTED_DOWN_EXPECTED_UP = '2'
    NOT_CONNECTED_DOWN_EXPECTED_DOWN = '3'
    IN_PROCESS = '4'


class StipulationType(Enum):
    AMT = 'AMT'
    AUTO_REINVESTMENT_AT_RATE_OR_BETTER = 'AUTOREINV'
    BANK_QUALIFIED = 'BANKQUAL'
    BARGAIN_CONDITIONS_SEE = 'BGNCON'
    COUPON_RANGE = 'COUPON'
    ISO_CURRENCY_CODE = 'CURRENCY'
    CUSTOM_START_END_DATE = 'CUSTOMDATE'
    GEOGRAPHICS_AND_RANGE = 'GEOG'
    VALUATION_DISCOUNT = 'HAIRCUT'
    INSURED = 'INSURED'
    YEAR_OR_YEAR_MONTH_OF_ISSUE = 'ISSUE'
    ISSUERS_TICKER = 'ISSUER'
    ISSUE_SIZE_RANGE = 'ISSUESIZE'
    LOOKBACK_DAYS = 'LOOKBACK'
    EXPLICIT_LOT_IDENTIFIER = 'LOT'
    LOT_VARIANCE = 'LOTVAR'
    MATURITY_YEAR_AND_MONTH = 'MAT'
    MATURITY_RANGE = 'MATURITY'
    MAXIMUM_SUBSTITUTIONS = 'MAXSUBS'
    MINIMUM_QUANTITY = 'MINQTY'
    MINIMUM_INCREMENT = 'MININCR'
    MINIMUM_DENOMINATION = 'MINDNOM'
    PAYMENT_FREQUENCY_CALENDAR = 'PAYFREQ'
    NUMBER_OF_PIECES = 'PIECES'
    POOLS_MAXIMUM = 'PMAX'
    POOLS_PER_MILLION = 'PPM'
    POOLS_PER_LOT = 'PPL'
    POOLS_PER_TRADE = 'PPT'
    PRICE_RANGE = 'PRICE'
    PRICING_FREQUENCY = 'PRICEFREQ'
    PRODUCTION_YEAR = 'PROD'
    CALL_PROTECTION = 'PROTECT'
    PURPOSE = 'PURPOSE'
    BENCHMARK_PRICE_SOURCE = 'PXSOURCE'
    RATING_SOURCE_AND_RANGE = 'RATING'
    TYPE_OF_REDEMPTION_VALUES_ARE_NONCALLABLE_CALLABLE_PREFUNDED_ESCROWEDTOMATURITY_PUTABLE_CONVERTIBLE = 'REDEMPTION'
    RESTRICTED = 'RESTRICTED'
    MARKET_SECTOR = 'SECTOR'
    SECURITYTYPE_INCLUDED_OR_EXCLUDED = 'SECTYPE'
    STRUCTURE = 'STRUCT'
    SUBSTITUTIONS_FREQUENCY = 'SUBSFREQ'
    SUBSTITUTIONS_LEFT = 'SUBSLEFT'
    FREEFORM_TEXT = 'TEXT'
    TRADE_VARIANCE = 'TRDVAR'
    WEIGHTED_AVERAGE_COUPONVALUE_IN_PERCENT = 'WAC'
    WEIGHTED_AVERAGE_LIFE_COUPON_VALUE_IN_PERCENT = 'WAL'
    WEIGHTED_AVERAGE_LOAN_AGE_VALUE_IN_MONTHS = 'WALA'
    WEIGHTED_AVERAGE_MATURITY_VALUE_IN_MONTHS = 'WAM'
    WHOLE_POOL = 'WHOLE'
    YIELD_RANGE = 'YIELD'


class SubscriptionRequestType(Enum):
    SNAPSHOT = '0'
    SNAPSHOT_PLUS_UPDATES = '1'
    DISABLE_PREVIOUS_SNAPSHOT_PLUS_UPDATE_REQUEST = '2'


class TargetStrategy(Enum):
    VWAP = '1'
    PARTICIPATE = '2'
    MININIZE_MARKET_IMPACT = '3'


class TaxAdvantageType(Enum):
    NONE_NOT_APPLICABLE = '0'
    MAXI_ISA = '1'
    TESSA = '2'
    MINI_CASH_ISA = '3'
    MINI_STOCKS_AND_SHARES_ISA = '4'
    MINI_INSURANCE_ISA = '5'
    CURRENT_YEAR_PAYMENT = '6'
    PRIOR_YEAR_PAYMENT = '7'
    ASSET_TRANSFER = '8'
    EMPLOYEE = '9'
    EMPLOYEE_CURRENT_YEAR = '10'
    EMPLOYER = '11'
    EMPLOYER_CURRENT_YEAR = '12'
    NON_FUND_PROTOTYPE_IRA = '13'
    NON_FUND_QUALIFIED_PLAN = '14'
    DEFINED_CONTRIBUTION_PLAN = '15'
    INDIVIDUAL_RETIREMENT_ACCOUNT = '16'
    INDIVIDUAL_RETIREMENT_ACCOUNT_ROLLOVER = '17'
    KEOGH = '18'
    PROFIT_SHARING_PLAN = '19'
    FOUR_HUNDRED_AND_ONE_K = '20'
    SELF_DIRECTED_IRA = '21'
    FOUR_HUNDRED_AND_THREE = '22'
    FOUR_HUNDRED_AND_FIFTY_SEVEN = '23'
    ROTH_IRA_24 = '24'
    ROTH_IRA_25 = '25'
    ROTH_CONVERSION_IRA_26 = '26'
    ROTH_CONVERSION_IRA_27 = '27'
    EDUCATION_IRA_28 = '28'
    EDUCATION_IRA_29 = '29'


class TerminationType(Enum):
    OVERNIGHT = '1'
    TERM = '2'
    FLEXIBLE = '3'
    OPEN = '4'


class TestMessageIndicator(Enum):
    YES = 'Y'
    NO = 'N'


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
    AT_THE_CLOSE = '7'


class TradSesMethod(Enum):
    ELECTRONIC = '1'
    OPEN_OUTCRY = '2'
    TWO_PARTY = '3'


class TradSesMode(Enum):
    TESTING = '1'
    SIMULATED = '2'
    PRODUCTION = '3'


class TradSesStatus(Enum):
    UNKNOWN = '0'
    HALTED = '1'
    OPEN = '2'
    CLOSED = '3'
    PRE_OPEN = '4'
    PRE_CLOSE = '5'
    REQUEST_REJECTED = '6'


class TradSesStatusRejReason(Enum):
    UNKNOWN_OR_INVALID_TRADINGSESSIONID = '1'
    OTHER = '99'


class TradeAllocIndicator(Enum):
    ALLOCATION_NOT_REQUIRED = '0'
    ALLOCATION_REQUIRED = '1'
    USE_ALLOCATION_PROVIDED_WITH_THE_TRADE = '2'


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
    IMBALANCE_MORE_BUYERS = 'P'
    IMBALANCE_MORE_SELLERS = 'Q'
    OPENING_PRICE = 'R'


class TradeReportRejectReason(Enum):
    SUCCESSFUL = '0'
    INVALID_PARTY_INFORMATION = '1'
    UNKNOWN_INSTRUMENT = '2'
    UNAUTHORIZED_TO_REPORT_TRADES = '3'
    INVALID_TRADE_TYPE = '4'
    OTHER = '99'


class TradeReportType(Enum):
    SUBMIT = '0'
    ALLEGED = '1'
    ACCEPT = '2'
    DECLINE = '3'
    ADDENDUM = '4'
    NO_WAS = '5'
    TRADE_REPORT_CANCEL = '6'
    LOCKED_IN_TRADE_BREAK = '7'


class TradeRequestResult(Enum):
    SUCCESSFUL = '0'
    INVALID_OR_UNKNOWN_INSTRUMENT = '1'
    INVALID_TYPE_OF_TRADE_REQUESTED = '2'
    INVALID_PARTIES = '3'
    INVALID_TRANSPORT_TYPE_REQUESTED = '4'
    INVALID_DESTINATION_REQUESTED = '5'
    TRADEREQUESTTYPE_NOT_SUPPORTED = '8'
    UNAUTHORIZED_FOR_TRADE_CAPTURE_REPORT_REQUEST = '9'
    OTHER = '99'


class TradeRequestStatus(Enum):
    ACCEPTED = '0'
    COMPLETED = '1'
    REJECTED = '2'


class TradeRequestType(Enum):
    ALL_TRADES = '0'
    MATCHED_TRADES_MATCHING_CRITERIA_PROVIDED_ON_REQUEST = '1'
    UNMATCHED_TRADES_THAT_MATCH_CRITERIA = '2'
    UNREPORTED_TRADES_THAT_MATCH_CRITERIA = '3'
    ADVISORIES_THAT_MATCH_CRITERIA = '4'


class TradedFlatSwitch(Enum):
    YES = 'Y'
    NO = 'N'


class TrdRegTimestampType(Enum):
    EXECUTION_TIME = '1'
    TIME_IN = '2'
    TIME_OUT = '3'
    BROKER_RECEIPT = '4'
    BROKER_EXECUTION = '5'


class TrdRptStatus(Enum):
    ACCEPTED = '0'
    REJECTED = '1'


class TrdType(Enum):
    REGULAR_TRADE = '0'
    BLOCK_TRADE = '1'
    EFP = '2'
    TRANSFER = '3'
    LATE_TRADE = '4'
    T_TRADE = '5'
    WEIGHTED_AVERAGE_PRICE_TRADE = '6'
    BUNCHED_TRADE = '7'
    LATE_BUNCHED_TRADE = '8'
    PRIOR_REFERENCE_PRICE_TRADE = '9'
    AFTER_HOURS_TRADE = '10'


class UnsolicitedIndicator(Enum):
    YES = 'Y'
    NO = 'N'


class Urgency(Enum):
    NORMAL = '0'
    FLASH = '1'
    BACKGROUND = '2'


class UserRequestType(Enum):
    LOGONUSER = '1'
    LOGOFFUSER = '2'
    CHANGEPASSWORDFORUSER = '3'
    REQUEST_INDIVIDUAL_USER_STATUS = '4'


class UserStatus(Enum):
    LOGGED_IN = '1'
    NOT_LOGGED_IN = '2'
    USER_NOT_RECOGNISED = '3'
    PASSWORD_INCORRECT = '4'
    PASSWORD_CHANGED = '5'
    OTHER = '6'


class WorkingIndicator(Enum):
    YES = 'Y'
    NO = 'N'


class YieldType(Enum):
    AFTER_TAX_YIELD = 'AFTERTAX'
    ANNUAL_YIELD = 'ANNUAL'
    YIELD_AT_ISSUE = 'ATISSUE'
    YIELD_TO_AVERAGE_MATURITY = 'AVGMATURITY'
    BOOK_YIELD = 'BOOK'
    YIELD_TO_NEXT_CALL = 'CALL'
    YIELD_CHANGE_SINCE_CLOSE = 'CHANGE'
    CLOSING_YIELD = 'CLOSE'
    COMPOUND_YIELD = 'COMPOUND'
    CURRENT_YIELD = 'CURRENT'
    TRUE_GROSS_YIELD = 'GROSS'
    GOVERNMENT_EQUIVALENT_YIELD = 'GOVTEQUIV'
    YIELD_WITH_INFLATION_ASSUMPTION = 'INFLATION'
    INVERSE_FLOATER_BOND_YIELD = 'INVERSEFLOATER'
    MOST_RECENT_CLOSING_YIELD = 'LASTCLOSE'
    CLOSING_YIELD_MOST_RECENT_MONTH = 'LASTMONTH'
    CLOSING_YIELD_MOST_RECENT_QUARTER = 'LASTQUARTER'
    CLOSING_YIELD_MOST_RECENT_YEAR = 'LASTYEAR'
    YIELD_TO_LONGEST_AVERAGE_LIFE = 'LONGAVGLIFE'
    MARK_TO_MARKET_YIELD = 'MARK'
    YIELD_TO_MATURITY = 'MATURITY'
    YIELD_TO_NEXT_REFUND = 'NEXTREFUND'
    OPEN_AVERAGE_YIELD = 'OPENAVG'
    YIELD_TO_NEXT_PUT = 'PUT'
    PREVIOUS_CLOSE_YIELD = 'PREVCLOSE'
    PROCEEDS_YIELD = 'PROCEEDS'
    SEMI_ANNUAL_YIELD = 'SEMIANNUAL'
    YIELD_TO_SHORTEST_AVERAGE_LIFE = 'SHORTAVGLIFE'
    SIMPLE_YIELD = 'SIMPLE'
    TAX_EQUIVALENT_YIELD = 'TAXEQUIV'
    YIELD_TO_TENDER_DATE = 'TENDER'
    TRUE_YIELD = 'TRUE'
    YIELD_VALUE_OF_1_32 = 'VALUE1/32'
    YIELD_TO_WORST = 'WORST'
