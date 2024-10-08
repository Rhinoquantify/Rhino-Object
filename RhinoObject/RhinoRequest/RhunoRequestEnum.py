from enum import Enum, unique


@unique
class Method(Enum):
    GET = "GET"
    POST = "POST"
    DELETE = "DELETE"
