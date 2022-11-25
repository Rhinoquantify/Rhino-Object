from enum import Enum


# 值不是唯一 不能进行 unique 注解
class BinanceUswapAmountPrecision(Enum):
    DOGEUSDT = 0
    DOGEBUSD = 0


class BinanceSpotAmountPrecision(Enum):
    BTCUSDT = 5
    BTCBUSD = 5
