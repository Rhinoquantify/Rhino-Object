from dataclasses import dataclass


@dataclass
class BaseConfig:
    host: str = "127.0.0.1"
    port: int = 0


@dataclass
class RedisConfig(BaseConfig):
    pass
