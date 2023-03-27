from dataclasses import dataclass
from typing import Union

from RhinoObject.Base.BaseEnum import ExchangeSub, Exchange


@dataclass
class BaseStrategy:
    key: str = ""
    secret: str = ""
    symbol: str = ""
    base: str = ""
    real_pair: str = ""
    exchange: Union[Exchange] = Exchange.BINANCE.value
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
    max_diff: float = 0  # 回调


@dataclass
class LBHS(BaseStrategy):
    leverage: int = 5
    depth_limit: int = 5
    open_depth: int = 3
    profit: float = 1
    loss: float = 1
    # 每笔使用多少 usdt 下单
    order_usdt: float = 5
    max_diff: float = 0  # 回调


@dataclass
class PINGRID(BaseStrategy):
    grid_limit: int = 5  # 网格次数
    order_usdt: float = 5
    profit: float = 1
    max_diff: float = 0


@dataclass
class MeshMoveBottomShort(BaseStrategy):
    leverage: int = 5  # USWAP 做空杠杆
    mesh_limit: int = 5  # 网格大小
    origin_price: float = 0.5  # 初始价格
    up_mesh_percentage: float = 0.2  # 上区间百分比
    bottom_mesh_percentage: float = 0.2  # 下区间百分比
    # 假设 origin_price = 0.5 则区间为 0.5 - 0.5 * 0.2 = 0.4 --- 0.5 + 0.5 * 0.2 = 0.6
    # 网格大小为 5 ，则每一格为 (0.6 - 0.4) / 5 = 0.04
