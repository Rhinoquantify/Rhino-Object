from enum import Enum, unique


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


@unique
class PositionDirection(Enum):
    LONG = "LONG"
    SHORT = "SHORT"


@unique
class KLineType(Enum):
    K_1M = "K_1M"


@unique
class CexOrderForceType(Enum):
    # 有效方法
    GTC = "GTC"  # Good Till Cancel 成交为止
    IOC = "IOC"  # Immediate or Cancel 无法立即成交(吃单)的部分就撤销
    FOK = "FOK"  # Fill or Kill 无法全部立即成交就撤销
    GTX = "GTX"  # Good Till Crossing 无法成为挂单方就撤销，即不主动吃单


@unique
class CexOrderType(Enum):
    SUCCESS = "SUCCESS"
    SUCCESSPART = "SUCCESSPART"
    CANCEL = "CANCEL"
    CANCELPART = "CANCELPART"
    FAIL = "FAIL"


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
