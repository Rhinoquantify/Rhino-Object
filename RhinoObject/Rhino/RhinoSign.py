from dataclasses import dataclass


@dataclass
class BaseSign:
    symbol: str = ""
    base: str = ""


@dataclass
class TradeSign(BaseSign):
    price: float = 0
    amount: float = 0


@dataclass
class BarSign(BaseSign):
    amount: float = 0
    open_price: float = 0
    close_price: float = 0
    high_price: float = 0
    low_price: float = 0
    start: int = 0
    end: int = 0
