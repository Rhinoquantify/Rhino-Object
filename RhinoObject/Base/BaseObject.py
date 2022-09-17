from dataclasses import dataclass


@dataclass
class BaseConfig:
    host: str = "127.0.0.1"
    port: int = 0  # 无论是 redis 还是 mysql 必须要修改端口号，因为黑客会用相关的服务挖矿
    db_name: str = ""
    password: str = ""  # 必须是强密码


@dataclass
class RedisConfig(BaseConfig):
    pass
