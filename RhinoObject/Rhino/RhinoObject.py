from typing import Union, List, Any, Dict, Callable

from RhinoObject.Base.BaseEnum import *
from RhinoObject.Base.BaseObject import *
from RhinoObject.Rhino.RhinoEnum import *


@dataclass
class BaseInfo:
    symbol: str = ""  # 只能是 BTC 不能是 BTCUSDT
    symbol_contract: str = ""  # 在 chain 链上的 symbol 合约地址
    base: str = ""  # 如果 pair 是 BTC_USDT 形式，那么 base 是 USDT
    base_contract: str = ""  # 在 chain 链上的 base 合约地址
    base_price_precision: int = 0
    base_amount_precision: int = 0
    symbol_price_precision: int = 0
    symbol_amount_precision: int = 0
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
    data_get_type: Union[DataGetType] = DataGetType.RESTFUL.value
    ip: str = ""
    code: int = 0
    data: dict = None
    is_dex: bool = False

    data_calcu_time: int = 0  # 数据计算时间，比如币安 trade 数据中的 T
    gateway_send_time: int = 0  # 从交易所发出该数据的时间，比如币安 trade 数据中的 E
    rhino_get_time: int = 0  # 程序接收到交易所的时间
    pipe_start_time: int = 0  # 存放在传输介质的时间

    sign_key: str = ""
    sign_secret: str = ""
    time_out: int = 3
    proxy: Union[Any, None] = None
    headers: Any = None

    rest_url: str = ""
    wss_url: str = ""

    price_percent: int = 5  # 价格精度
    chains: List = None
    chains_contracts: List = None
    deposit_enables: List[bool] = None  # 是否可充值
    withdraw_enables: List[bool] = None  # 是否可提币
    withdraw_amounts: List[float] = None  # 提币手续费
    transfer_feess: List[float] = None  # 转账手续费
    nonce: int = 0
    gas: int = 3
    address: str = ""  # 钱包地址

    def __post_init__(self):
        self.key = "_".join([self.cex_exchange_sub, self.data_type, self.real_pair])

    def __str__(self):
        return f"{self.chain}_{self.cex_exchange_sub}_{self.dex_exchange}_{self.real_pair}_{self.data_type}"


@dataclass
class MixInfo(BaseInfo):
    # 其他配置
    symbol_method: Any = None  # 这个是 Rhino-collect 包中的 MethodEnum
    # cex 配置
    depth_limit: int = 5
    # ticker_symbol: str = ""  # 如果传入 all 则查询所有的 symbol 否则只查询 ticker_symbol
    # ticker_symbols: list = None  # 如果上述传递 all 则会返回海量的数据，通过 ticker_symbols 里面的 real_pair 进行过滤
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
class DEXInfo(BaseInfo):
    platform: Union[ExchangeBSC] = ExchangeBSC.PANCAKESWAP.value
    route: Union[ExchangeBSCRoute] = ExchangeBSCRoute.PANCAKESWAP.value
    pair: str = ""  # 在 chain 链上工厂中存的 pair token
    pair_contract: str = ""  # pair 的合约地址
    token_symbol: str = ""
    token_amount: float = 0
    token_contract: str = ""
    token_decimal: int = 0
    to_symbol: str = ""
    to_amount: float = 0
    to_contract: str = ""
    to_decimal: int = 0
    token_index: int = 0  # 只能是 0 或者 1
    pool_reverse0: int = 0
    pool_reverse1: int = 0
    # 用户信息相关
    cex_address: str = ""
    dex_address: str = ""
    address: str = ""
    private: str = ""


@dataclass
class RhinoExchangeInfo(BaseInfo):
    pass


@dataclass
class RhinoDepth(BaseInfo):
    depth_type: Union[DepthType] = DepthType.SYMBOL.value

    depth_limit: int = 5
    interval: int = 100

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
    pool11_reverse0: int = 0
    pool11_reverse1: int = 0
    pool12_reverse0: int = 0
    pool12_reverse1: int = 0
    pool13_reverse0: int = 0
    pool13_reverse1: int = 0
    pool14_reverse0: int = 0
    pool14_reverse1: int = 0
    pool15_reverse0: int = 0
    pool15_reverse1: int = 0
    pool16_reverse0: int = 0
    pool16_reverse1: int = 0
    pool17_reverse0: int = 0
    pool17_reverse1: int = 0
    pool18_reverse0: int = 0
    pool18_reverse1: int = 0
    pool19_reverse0: int = 0
    pool19_reverse1: int = 0
    pool20_reverse0: int = 0
    pool20_reverse1: int = 0
    pool21_reverse0: int = 0
    pool21_reverse1: int = 0
    pool22_reverse0: int = 0
    pool22_reverse1: int = 0
    pool23_reverse0: int = 0
    pool23_reverse1: int = 0
    pool24_reverse0: int = 0
    pool24_reverse1: int = 0
    pool25_reverse0: int = 0
    pool25_reverse1: int = 0
    pool26_reverse0: int = 0
    pool26_reverse1: int = 0
    pool27_reverse0: int = 0
    pool27_reverse1: int = 0
    pool28_reverse0: int = 0
    pool28_reverse1: int = 0
    pool29_reverse0: int = 0
    pool29_reverse1: int = 0

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
    buy_price11: float = 0
    buy_amount11: float = 0
    buy_price12: float = 0
    buy_amount12: float = 0
    buy_price13: float = 0
    buy_amount13: float = 0
    buy_price14: float = 0
    buy_amount14: float = 0
    buy_price15: float = 0
    buy_amount15: float = 0

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
    sell_price11: float = 0
    sell_amount11: float = 0
    sell_price12: float = 0
    sell_amount12: float = 0
    sell_price13: float = 0
    sell_amount13: float = 0
    sell_price14: float = 0
    sell_amount14: float = 0
    sell_price15: float = 0
    sell_amount15: float = 0

    def __str__(self):
        return f"depths: {self.chain}_{self.cex_exchange_sub}_{self.dex_exchange}_{self.real_pair}"


@dataclass
class RhinoIncreaseDepth:
    price: float = 0
    amount: float = 0
    real_pair: str = ""
    direction: Union[OrderDirection, PositionDirection] = OrderDirection.BUY.value
    gateway_send_time: int = 0
    rhino_get_time: int = 0


@dataclass
class RhinoTrade(BaseInfo):
    price: float = 0
    amount: float = 0
    time: int = 0
    direction: Union[OrderDirection, PositionDirection] = OrderDirection.BUY.value

    limit: int = 1000

    trade_start_time: int = 0  # 开始时间 查询订单的时候的开始时间
    trade_end_time: int = 0  # 结束时间 查询订单的时候的结束时间

    def __str__(self):
        return f"trades: {self.chain}_{self.cex_exchange_sub}_{self.dex_exchange}_{self.real_pair}"


@dataclass
class RhinoTrades:
    trade_list: List[RhinoTrade] = None


@dataclass
class RhinoTickers:
    key: str = ""
    ticker_type: Union[TickerType] = TickerType.SINGLE.value
    ticker_list: list = None


@dataclass
class RhinoTicker(BaseInfo):
    ticker_type: Union[TickerType] = TickerType.SINGLE.value

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
class RhinoKlines:
    base_info: BaseInfo = None
    k_line_type: Union[KLineType] = KLineType.K_1M.value
    kline_list: [] = None


@dataclass
class RhinoKline(BaseInfo):
    k_line_type: Union[KLineType] = KLineType.K_1M.value  # 更新频率
    is_end: bool = False  # 这跟K是否结束
    line_limit: int = 10

    open_price: float = 0
    close_price: float = 0
    low_price: float = 0
    high_price: float = 0
    up_multi: float = 0  # 上影线相对于实体的倍数
    down_multi: float = 0  # 下影线相对于实体的倍数
    direction: int = 0  # 涨跌，主要是看开盘和收盘的对比
    trade_count: int = 0  # 成交次数
    trade_amount: float = 0  # token 成交量
    trade_sell_amount: float = 0
    trade_buy_amount: float = 0
    trade_usdt: float = 0  # 成交额
    trade_buy_usdt: float = 0  # 主动买入
    trade_sell_usdt: float = 0  # 主动卖出
    open_time: int = 0
    close_time: int = 0

    # def __post_init__(self):
    # if self.open_price > self.close_price:
    #     self.direction = -1  # 跌
    #     self.up_multi = float((self.high_price - self.open_price) / (self.open_price - self.close_price))
    #     self.down_multi = float((self.close_price - self.low_price) / (self.open_price - self.close_price))
    # elif self.open_price < self.close_price:
    #     self.direction = 1  # 涨
    #     self.up_multi = float((self.high_price - self.close_price) / (self.close_price - self.open_price))
    #     self.down_multi = float((self.open_price - self.low_price) / (self.close_price - self.open_price))
    # else:
    #     self.direction = 0  # 不涨不跌
    #     self.up_multi = float((self.high_price - self.open_price) / self.open_price)
    #     self.down_multi = float((self.open_price - self.low_price) / self.open_price)
    # pass


@dataclass
class RhinoBalance:
    symbol: str = ""
    balance: float = 0
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
    withdraw_state: Union[WithdrawStatus] = WithdrawStatus.SUBMIT.value
    withdraw_id: str = ""
    tx: str = ""  # 交易 hash
    apply_time: int = 0  # 申请提现时间


@dataclass
class RhinoOrder(BaseInfo):
    price: float = 0
    stop_price: float = 0
    amount: float = 0  # 下单 coin 的数量
    execute_price: float = 0  # 成交价格
    execute_amount: float = 0  # 成交数量
    usdt: float = 0  # 价值多少 usdt
    direction: Union[OrderDirection] = OrderDirection.BUY.value
    position_direction: Union[PositionDirection, None] = None
    order_id: str = ""
    client_order_id: str = ""
    is_taker: bool = True
    order_type: Union[OrderType] = OrderType.LIMIT.value
    OrderForceType: Union[CexOrderForceType] = None
    state: Union[CexOrderType] = CexOrderType.NEW.value

    # 待删除，以后不用该属性
    pre_price: float = 0  # 等于 price 防止，市价单卖出时没有成功
    pre_order_id: str = ""
    pre_client_order_id: str = ""

    # 记录
    buy_price: float = 0
    sell_price: float = 0
    sell_order_id: str = ""
    sell_client_order_id: str = ""
    buy_order_id: str = ""
    buy_client_order_id: str = ""

    # 取消 order
    cancel: bool = False
    executed_amount: float = 0  # 成交 coin 数量
    executed_usdt: float = 0  # 成交usdt

    is_close: bool = True
    is_check: Union[bool] = False  # 这参数是为了出现这种情况，当查询完订单状态后，恰好成交，此时又取消订单，然后下订单，就会导致上次订单完全丢失
    max_profit: float = 0

    # 链上
    routers: list = None
    token_contracts: list = None
    receive_address: str = ""
    amount_in: int = 0
    amount_out: int = 0
    eth_tx: str = ""
    token_burn: bool = False
    logs: Union[list, str] = None
    code: int = 0
    error_info: str = ""
    from_contract: str = ""
    to_contract: str = ""
    gas_price: int = ""


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
    Liquidation_Price: float = 0  # 强平价格
    real_profit: float = 0  # 自己根据最新合约价格计算的盈亏
    estimate_profit: float = 0  # 标记价格的未实现盈亏 不是最终的盈亏
    state: Union[CexOrderType] = CexOrderType.NEW.value
    usdt: float = 0  # 价值多少 usdt
    is_taker: bool = True
    mark_price: float = 0  # 标记价格
    order_id: str = ""
    client_order_id: str = ""
    pre_price: float = 0
    pre_order_id: str = ""
    pre_client_order_id: str = ""

    # 平仓
    end_profit: float = 0
    close_time: int = 0
    is_close: bool = False
    max_profit: float = 0  # 最大真实利润


@dataclass
class RhinoToken(BaseInfo):
    token_decimal: int = 0
    token_contract: str = ""


@dataclass
class RhinoProfit(BaseInfo):
    order_direction: Union[OrderDirection] = OrderDirection.BUY.value
    strategy: Union[Strategy.MULTICEXDEXBSCMEXCTAKER.value] = Strategy.MULTICEXDEXBSCMEXCTAKER.value
    profit: float = 0
    price: float = 0
    depth_number: int = 1  # 需要吃多少深度的 depth


@dataclass
class RhinoFundingRate(BaseInfo):
    funding_rate: float = 0
    next_funding_rate: float = 0


@dataclass
class RedisConfig(BaseConfig):
    DataType: Union[RedisDataType] = RedisDataType.SET.value
    is_subscribe: bool = False
    is_async: bool = False


@dataclass
class RhinoConfig:
    ip: str = ""
    heartbeat: int = 0.1
    collect_type: Union[DealDataType] = DealDataType.REDIS.value
    redis_config: RedisConfig = None
    zh: str = ""


@dataclass
class SymbolInfo(MixInfo):
    symbol_methods: List[Union[MethodEnum, Any]] = None  # 调用该 exchange_sub 的什么方法
    rhino_depth: RhinoDepth = None
    rhino_trade: RhinoTrade = None
    rhino_kline: RhinoKline = None
    rhino_ticker: RhinoTicker = None

    dex: Dict[int, DEXInfo] = None  # int 从 1 开始

    def __str__(self):
        return f"SymbolInfo: {self.chain}_{self.cex_exchange_sub}_{self.dex_exchange}_{self.real_pair}"


@dataclass
class SymbolInfos:
    """
    和下面的 exchangeSub 一一对应，表示该 exchangeSub 使用 wb 还是 rest 收集数据
    """
    subscribes: Dict[Union[ExchangeSub], bool] = None
    """
    每一个 ExchangeSub 下面 list 长度不能超过 20 个
    超过 20 个之后，无论是 python 的 wb 处理还是 rest 请求，都变得有压力
    """
    symbols: Dict[Union[ExchangeSub], List[SymbolInfo]] = None


@dataclass
class WebsocketListen:
    time: int = 0
    gateway: str = ""
    key: str = ""


@dataclass
class WebsocketData:
    key: Union[ExchangeSub] = ExchangeSub.BINANCESPOT.value
    data_type: Union[RhinoDataType] = RhinoDataType.WEBSOCKETSTART.value
    exchange_sub: Union[ExchangeSub] = ExchangeSub.BINANCESPOT.value


@dataclass
class CallableMethods:
    on_transfer: Callable = None
    on_failed: Callable = None
    on_error: Callable = None
    on_timeout: Callable = None
    on_heart: Callable = None

    # 一般用于 on_transfer 的回调函数中，携带的值
    extra_data: Any = None
    on_transfers: Dict[str, Callable] = None
