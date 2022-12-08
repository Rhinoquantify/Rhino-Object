from dataclasses import dataclass

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
class SignCondition:
    # QD
    is_base: bool = True
    amount: float = 30_000
