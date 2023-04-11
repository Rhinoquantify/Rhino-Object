from enum import Enum, unique


@unique
class OfferType(Enum):
    FirmOffer = "FirmOffer"  # 实盘
    TestOffer = "TestOffer"  # 包含假数据、模拟盘、实盘数据、回测数据


@unique
class Chain(Enum):
    ETH = "ETH"
    BSC = "BSC"
    POLYGON = "POLYGON"


@unique
class Exchange(Enum):
    BINANCE = "BINANCE"
    OKEX = "OKEX"
    HUOBI = "HUOBI"
    MEXC = "MEXC"
    GATE = "GATE"
    FTX = "FTX"
    BSC = "BSC"


@unique
class ExchangeSub(Enum):
    BINANCESPOT = "BINANCESPOT"
    BINANCEUSWAP = "BINANCEUSWAP"
    OKEXSPOT = "OKEXSPOT"
    OKEXUSWAP = "OKEXUSWAP"
    HUOBISPOT = "HUOBISPOT"
    HUOBIUSWAP = "HUOBIUSWAP"
    MEXCSPOT = "MEXCSPOT"
    MEXCUSWAP = "MEXCUSWAP"
    BSCSPOT = "BSCSPOT"

    # 这个是 BSC 的 BASE
    BSCSPOTBASE = "BSCSPOTBASE"


@unique
class ExchangeBSC(Enum):
    BSC = "BSC"
    PANCAKESWAP = "PANCAKESWAP"
    BISWAP = "BISWAP"
    BABYSWAP = "BABYSWAP"
    APESWAP = "APESWAP"
    JULSWAP = "JULSWAP"
    FSTSWAP = "FSTSWAP"


@unique
class ExchangeBSCRoute(Enum):
    PANCAKESWAP = "0x10ed43c718714eb63d5aa57b78b54704e256024e"
    BISWAP = "0x3a6d8cA21D1CF76F653A67577FA0D27453350dD8"
    BABYSWAP = "0x325e343f1de602396e256b67efd1f61c3a6b38bd"
    APESWAP = "0xcF0feBd3f17CEf5b47b0cD257aCf6025c5BFf3b7"
    JULSWAP = "0xbd67d157502A23309Db761c41965600c2Ec788b2"


@unique
class ExchangeETH(Enum):
    ETH = "ETH"


@unique
class SymbolType(Enum):
    SPOT = "SPOT"
    USWAP = "USWAP"


@unique
class OrderDirection(Enum):
    BUY = "BUY"
    SELL = "SELL"
    BOTH = "BOTH"


@unique
class PositionDirection(Enum):
    LONG = "LONG"
    SHORT = "SHORT"
    BOTH = "BOTH"


@unique
class KLineType(Enum):
    K_1M = "K_1M"
    K_3M = "K_3M"
    K_5M = "K_5M"
    K_15M = "K_15M"
    K_30M = "K_30M"
    K_1H = "K_1H"
    K_2H = "K_2H"
    K_4H = "K_4H"
    K_6H = "K_6H"
    K_8H = "K_8H"
    K_12H = "K_12H"
    K_1D = "K_1D"
    K_3D = "K_3D"
    K_1W = "K_1W"
    K_1Mouth = "K_1Mouth"


@unique
class OrderType(Enum):
    LIMIT = "LIMIT"
    MARKET = "MARKET"
    STOP = "STOP"
    TAKE_PROFIT = "TAKE_PROFIT"
    STOP_MARKET = "STOP_MARKET"
    TAKE_PROFIT_MARKET = "TAKE_PROFIT_MARKET"
    TRAILING_STOP_MARKET = "TRAILING_STOP_MARKET"


@unique
class CexOrderForceType(Enum):
    # 有效方法
    GTC = "GTC"  # Good Till Cancel 成交为止
    IOC = "IOC"  # Immediate or Cancel 无法立即成交(吃单)的部分就撤销
    FOK = "FOK"  # Fill or Kill 无法全部立即成交就撤销
    GTX = "GTX"  # Good Till Crossing 无法成为挂单方就撤销，即不主动吃单


@unique
class CexOrderType(Enum):
    NEW = "NEW"  # 订单被交易引擎接受
    PARTIALLY_FILLED = "PARTIALLY_FILLED"  # 部分订单被成交
    FILLED = "FILLED"  # 订单完全成交
    CANCELED = "CANCELED"  # 用户撤销了订单
    PENDING_CANCEL = "PENDING_CANCEL"  # 撤销中
    REJECTED = "REJECTED"  # 订单没有被交易引擎接受
    EXPIRED = "EXPIRED"  # 订单被交易引擎取消
    CALCULATED = "CALCULATED"  # 订单ADL或爆仓
    TRADE = "TRADE"  # 交易


@unique
class DealDataType(Enum):
    REDIS = "REDIS"
    KAFKA = "KAFKA"
    RABBITMQ = "RABBITMQ"
    RPC = "RPC"
    MYSQL = "MYSQL"


@unique
class DataGetType(Enum):
    RESTFUL = "RESTFUL"
    WEBSOCKET = "WEBSOCKET"


@unique
class RedisDataType(Enum):
    SET = "SET"
    GET = "GET"


@unique
class TickerType(Enum):
    ALL = "ALL"
    SINGLE = "SINGLE"


@unique
class DepthType(Enum):
    SYMBOL = "SYMBOL"  # 正常单个 symbol 的 depth
    SYMBOLBEST = "SYMBOLBEST"  # 单个 symbol 最优挂单 最好不用，而是用 SYMBOL 获得，目前没办法区分 SYMBOLBEST 和 BESTALL
    BESTALL = "BESTALL"  # 全市场最有挂单
