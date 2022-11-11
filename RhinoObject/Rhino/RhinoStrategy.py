from dataclasses import dataclass
from typing import Union

from RhinoObject.Base.BaseEnum import ExchangeSub


@dataclass
class BaseStrategy:
    key: str = ""
    secret: str = ""
    symbol: str = ""
    real_pair: str = ""
    exchange_sub: Union[ExchangeSub] = ExchangeSub.BINANCEUSWAP.value
    proxy: str = ""


@dataclass
class USWAPLSHL(BaseStrategy):
    """
    小资金高倍数
    low source high leverage
    """
    leverage: int = 5
    depth_limit: int = 5
    open_depth: int = 3
    profit: float = 1
    loss: float = 1
    # 每笔使用多少 usdt 下单
    order_usdt: float = 5
