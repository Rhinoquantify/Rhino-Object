from dataclasses import dataclass
from typing import Union, List, Any

from RhinoObject.Base.BaseEnum import *
from RhinoObject.Rhino.RhinoEnum import *


@dataclass
class BaseInfo:
    symbol: str = ""  # 只能是 BTC 不能是 BTCUSDT
    symbol_contract: str = ""  # 在 chain 链上的 symbol 合约地址
    base: str = ""  # 如果 pair 是 BTC_USDT 形式，那么 base 是 USDT
    base_contract: str = ""  # 在 chain 链上的 base 合约地址
    chain: Union[Chain] = Chain.BSC.value
    key: str = ""  # 作为 dict 的 key
    pair: str = ""  # 只能以 token_base 形式书写
    real_pair: str = ""  # cex 中真实的交易对地址 dex 也要写，可以按照某些规则自定义，长度不能超过 10
    cex_exchange: Union[Exchange] = Exchange.BINANCE.value
    cex_exchange_sub: Union[ExchangeSub] = ExchangeSub.BINANCESPOT.value
    dex_exchange: Union[ExchangeBSC, ExchangeETH] = ExchangeBSC.BSC.value
    dex_type: Union[SymbolType] = SymbolType.SPOT.value
    cex_type: Union[SymbolType] = SymbolType.SPOT.value
    data_type: Union[RhinoDataType] = RhinoDataType.RHINODEPTH.value  # 存储数据的类型
    rhino_update_time: int = 0  # 该系统接收到的时间 毫秒级别
    data_update_time: int = 0  # 该数据返回自带的时间 毫秒级别
    ip: str = ""
    code: int = 0
    data: dict = None
    is_dex: bool = False
    start_time: int = 0  # 毫秒级别 start_time 和 end_time 是为了统计所消耗的时间
    end_time: int = 0  # 毫秒级别 可以是存储时间、网络接收数据时间等

    def __post_init__(self):
        self.key = "_".join([self.data_type, self.cex_exchange_sub, self.chain, self.dex_exchange, self.pair])

    def __str__(self):
        return f"{self.chain}_{self.cex_exchange_sub}_{self.dex_exchange}_{self.real_pair}"


@dataclass
class MixInfo(BaseInfo):
    # 其他配置
    symbol_method: Any = None  # 这个是 Rhino-collect 包中的 MethodEnum
    time_out: int = 3
    proxy: Union[Any, None] = None
    headers: Any = None
    # cex 配置
    depth_limit: int = 5
    ticker_symbol: str = ""  # 如果传入 all 则查询所有的 symbol 否则只查询 ticker_symbol
    ticker_symbols: list = None  # 如果上述传递 all 则会返回海量的数据，通过 ticker_symbols 里面的 real_pair 进行过滤
    # dex 配置
    route: str = ""  # dex 的路由地址
    pair_addresses: [] = None  # dex 通过传入的 pair 来获取池子的深度 长度不能超过 10 个
    from_index: int = 0
    from_contract: str = ""
    from_amount: float = 0
    from_decimal: int = 0
    to_contract: str = ""
    to_amount: float = 0
    to_decimal: int = 0


@dataclass
class RhinoDepth(BaseInfo):
    # dex 特有的
    pool1_reverse0: int = 0
    pool1_reverse1: int = 0
    pool2_reverse0: int = 0
    pool2_reverse1: int = 0
    pool3_reverse0: int = 0
    pool3_reverse1: int = 0
    pool4_reverse0: int = 0
    pool4_reverse1: int = 0
    pool5_reverse0: int = 0
    pool5_reverse1: int = 0
    pool6_reverse0: int = 0
    pool6_reverse1: int = 0
    pool7_reverse0: int = 0
    pool7_reverse1: int = 0
    pool8_reverse0: int = 0
    pool8_reverse1: int = 0
    pool9_reverse0: int = 0
    pool9_reverse1: int = 0
    pool10_reverse0: int = 0
    pool10_reverse1: int = 0

    buy_price1: float = 0
    buy_amount1: float = 0
    buy_price2: float = 0
    buy_amount2: float = 0
    buy_price3: float = 0
    buy_amount3: float = 0
    buy_price4: float = 0
    buy_amount4: float = 0
    buy_price5: float = 0
    buy_amount5: float = 0
    buy_price6: float = 0
    buy_amount6: float = 0
    buy_price7: float = 0
    buy_amount7: float = 0
    buy_price8: float = 0
    buy_amount8: float = 0
    buy_price9: float = 0
    buy_amount9: float = 0
    buy_price10: float = 0
    buy_amount10: float = 0

    sell_price1: float = 0  # 第一深度价格
    sell_amount1: float = 0
    sell_price2: float = 0  # 第二深度价格
    sell_amount2: float = 0  # 第一深度加上第二深度
    sell_price3: float = 0  # 第一深度价格
    sell_amount3: float = 0
    sell_price4: float = 0
    sell_amount4: float = 0
    sell_price5: float = 0
    sell_amount5: float = 0
    sell_price6: float = 0
    sell_amount6: float = 0
    sell_price7: float = 0
    sell_amount7: float = 0
    sell_price8: float = 0
    sell_amount8: float = 0
    sell_price9: float = 0
    sell_amount9: float = 0
    sell_price10: float = 0
    sell_amount10: float = 0

    def __str__(self):
        return f"depths: {self.chain}_{self.cex_exchange_sub}_{self.dex_exchange}_{self.real_pair}"


@dataclass
class RhinoTrades(BaseInfo):
    ticker_list: [] = None


@dataclass
class RhinoTrade:
    price: float = 0
    amount: float = 0
    time: int = 0
    direction: Union[OrderDirection, PositionDirection] = OrderDirection.BUY.value


@dataclass
class RhinoTickers(BaseInfo):
    ticker_list: [] = None


@dataclass
class RhinoTicker:
    rate: float = 0  # 本阶段变化 一般指 24 小时
    price_change: float = 0  # 本阶段价格变化 一般指 24 小时
    sell_price: float = 0  # 最低卖价
    sell_amount: float = 0  # 最低卖价数量
    buy_price: float = 0  # 最高买价
    buy_amount: float = 0  # 最高买价数量
    open_price: float = 0  # 本阶段开盘价格
    trade_price: float = 0  # 最新成交价
    high_price: float = 0  # 本阶段成交最高卖价
    low_price: float = 0  # 本阶段成交最低价
    data: list = None


@dataclass
class RhinoKlines(BaseInfo):
    interval: Union[KLineType] = KLineType.K_1M.value
    kline_list: [] = None


@dataclass
class RhinoKline:
    open_price: float = 0
    close_price: float = 0
    min_price: float = 0
    max_price: float = 0
    up_multi: float = 0  # 上影线相对于实体的倍数
    down_multi: float = 0  # 下影线相对于实体的倍数
    direction: int = 0  # 涨跌，主要是看开盘和收盘的对比
    trade_count: int = 0  # 成交次数
    trade_usdt: float = 0  # 成交额
    trade_buy_usdt: float = 0  # 主动买入
    trade_sell_usdt: float = 0  # 主动卖出
    open_time: int = 0
    close_time: int = 0

    def __post_init__(self):
        if self.open_price > self.close_price:
            self.direction = -1  # 跌
            self.up_multi = float((self.max_price - self.open_price) / (self.open_price - self.close_price))
            self.down_multi = float((self.close_price - self.min_price) / (self.open_price - self.close_price))
        elif self.open_price < self.close_price:
            self.direction = 1  # 涨
            self.up_multi = float((self.max_price - self.close_price) / (self.close_price - self.open_price))
            self.down_multi = float((self.open_price - self.min_price) / (self.close_price - self.open_price))
        else:
            self.direction = 0  # 不涨不跌
            self.up_multi = float((self.max_price - self.open_price) / self.open_price)
            self.down_multi = float((self.open_price - self.min_price) / self.open_price)


@dataclass
class RhinoBalance:
    symbol: str = ""
    frozen: float = 0
    available: float = 0


@dataclass
class RhinoAccount(BaseInfo):
    balance_list: Union[List[RhinoBalance], None] = None


@dataclass
class RhinoCexConfig(BaseInfo):
    key: str = ""
    secret: str = ""
    cex_address: str = ""
    dex_address: str = ""  # dex_address 接收地址


@dataclass
class RhinoDexConfig:
    dex_from_decimal: int = 0
    dex_to_decimal: int = 0
    dex_sell_path: [] = None  # coin -> usdt
    dex_buy_path: [] = None  # usdt -> coin
    cex_address: str = ""
    dex_address: str = ""
    route1: str = ""  # dex swap 路由地址 1
    route2: str = ""  # dex swap 路由地址 2
    tx: str = ""
    nonce: int = 0


@dataclass
class RhinoWithdraw(BaseInfo):
    amount: float = 0  # 提现的数量
    fee: float = 0  # 手续费
    is_success: bool = False
    withdraw_state: str = ""
    withdraw_id: str = ""
    tx: str = ""  # 交易 hash


@dataclass
class RhinoOrder(BaseInfo):
    price: float = 0
    amount: float = 0  # 下单 coin 的数量
    usdt: float = 0  # 价值多少 usdt
    direction: str = ""
    order_id: str = ""
    is_taker: bool = True
    order_type: Union[CexOrderForceType] = CexOrderForceType.IOC.value
    state: Union[CexOrderType] = CexOrderType.SUCCESS.value

    # 取消 order
    cancel: bool = False
    executed_amount: float = 0  # 成交 coin 数量
    executed_usdt: float = 0  # 成交usdt


@dataclass
class RhinoLeverage(BaseInfo):
    leverage: int = 0


@dataclass
class RhinoPosition(BaseInfo):
    price: float = 0  # 开仓均价
    amount: float = 0  # 下单 coin 的数量
    fee_token: float = 0  # 手续费 token
    fee_usdt: float = 0  # 手续费 usdt
    position_id: str = ""
    position_type: Union[CexOrderForceType] = CexOrderForceType.IOC.value
    direction: Union[PositionDirection] = PositionDirection.LONG.value
    real_profit: float = 0  # 自己根据最新合约价格计算的盈亏
    estimate_profit: float = 0  # 标记价格的未实现盈亏 不是最终的盈亏
    state: Union[CexOrderType] = CexOrderType.SUCCESS.value
    usdt: float = 0  # 价值多少 usdt
    is_taker: bool = True
    # 平仓
    end_profit: float = 0
    close_time: int = 0


@dataclass
class RhinoToken(BaseInfo):
    token_decimal: int = 0
    token_contract: str = ""
