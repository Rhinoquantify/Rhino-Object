from enum import Enum, unique


@unique
class RhinoDataType(Enum):
    RHINODEPTH = "RHINODEPTH"
    RHINOTRADE = "RHINOTRADE"


@unique
class Strategy(Enum):
    FLASHSWAPBSC = "FLASHSWAPBSC"
    MULTICEXDEXBSCMEXCTAKER = "MULTICEXDEXBSCMEXCTAKER"


@unique
class Project(Enum):
    MEXCSPOTWSDATASERVICE = "MEXCSPOTWSDATASERVICE"


@unique
class RestEnum(Enum):
    BINANCESPOTSYNCH = "BINANCESPOTSYNCH"
    BINANCESPOTASYNCH = "BINANCESPOTASYNCH"
    BINANCESWAPUSDTSYNCH = "BINANCESWAPUSDTSYNCH"
    BINANCESWAPUSDTASYNCH = "BINANCESWAPUSDTASYNCH"

    MEXCSPOTSYNCH = "MEXCSPOTSYNCH"
    MEXCSPOTASYNCH = "MEXCSPOTASYNCH"

    BSCDEXPOOL = "BSCDEXPOOL"
    BSCDEXPOOLASYNCH = "BSCDEXPOOLASYNCH"
    BSCDEXPOOLSYNCH = "BSCDEXPOOLSYNCH"


@unique
class MethodEnum(Enum):
    """
    和 BaseGateway 里面的函数相对应
    """
    # RhinoCollect 里面的
    GETDEPTHS = "GETDEPTHS"
    GETTRADES = "GETTRADES"
