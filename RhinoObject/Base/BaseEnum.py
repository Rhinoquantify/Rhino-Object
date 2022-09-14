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
