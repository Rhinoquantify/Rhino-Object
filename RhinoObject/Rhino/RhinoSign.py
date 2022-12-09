from dataclasses import dataclass
from typing import Union, Callable

from RhinoObject.Rhino.RhinoEnum import BarDirectionEnum
from RhinoObject.Rhino.RhinoEnum import RhinoSign
from RhinoObject.Rhino.RhinoObject import BaseInfo


@dataclass
class QD(BaseInfo):
    """
    量价指标
    在特定的 trade 数量中，多空/买卖占据的比例
    """
    high_price: float = 0
    low_price: float = 0
    open_price: float = 0
    close_price: float = 0
    amount: float = 0
    real_amount: float = 0
    buy_amount: float = 0
    sell_amount: float = 0

    def __post_init__(self):
        self.key = self.cex_exchange_sub + self.real_pair.upper() + "_" + RhinoSign.QD.value


@dataclass
class KlineTrend(BaseInfo):
    bar_amounts: int = 3  # 检测多少根 bar

    # 下面都是百分比 开盘价和收盘价之间的百分比 (开盘价 - 收盘价) / 开盘价
    single_bar_price_diff_up: float = 0
    single_bar_amount_diff_up: float = 0
    all_bar_price_diff_up: float = 0
    all_bar_amount_diff_up: float = 0

    single_bar_price_diff_down: float = 0
    single_bar_amount_diff_down: float = 0
    all_bar_price_diff_down: float = 0
    all_bar_amount_diff_down: float = 0

    trend_direction: Union[BarDirectionEnum] = BarDirectionEnum.DOWN.value

    on_transfer: Callable = None

    def __post_init__(self):
        self.key = self.cex_exchange_sub + self.real_pair.upper() + "_" + RhinoSign.KLINETREND.value


@dataclass
class MA(BaseInfo):
    MA_period: int = 9
    every_update: bool = True
    on_transfer: Callable = None

    def __post_init__(self):
        self.key = self.cex_exchange_sub + self.real_pair.upper() + "_" + RhinoSign.MA.value


@dataclass
class ATR(BaseInfo):
    ATR_period: int = 9
    every_update: bool = True
    on_transfer: Callable = None

    def __post_init__(self):
        self.key = self.cex_exchange_sub + self.real_pair.upper() + "_" + RhinoSign.ATR.value


@dataclass
class SignCondition:
    # QD
    is_base: bool = True
    amount: float = 30_000
    kline_trend: KlineTrend = None
    MA: MA = None
    ATR: ATR = None
