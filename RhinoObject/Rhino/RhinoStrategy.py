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
class MeshMoveBottomShortConfig(BaseStrategy):
    amount_precision: int = 1  # 数量精度
    price_precision: int = 5  # 价格精度
    leverage: int = 5  # USWAP 做空杠杆
    mesh_limit: int = 3  # 半边网格大小
    origin_price: float = 0.5  # 初始价格
    mesh_percentage: float = 0.005  # 每格的百分比
    mesh_price: list[float] = None  # 价格区间 list
    top_mesh_price: float = 0  # 上区间价格
    bottom_mesh_price: float = 0  # 下区间价格

    spot_usdt: float = 50  # 每一次挂单的价值
    spot_mix_usdt: float = 5  # 最小卖出价值，交易所最小单量
    spot_max_usdt: float = 40  # 策略运行时最大下单量
