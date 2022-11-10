from typing import Any, Callable, Union


class RhinoWebsocket:
    def __init__(
            self,
            url: str,
            data: Union[dict, str, bytes, None] = None,  # POST
            on_connected: Callable = None,
            on_reconnected: Callable = None,
            on_receive: Callable = None,
            on_ping: Callable = None,
            on_pong: Callable = None,
            on_fail: Callable = None,
            on_error: Callable = None,
            on_transfer: Callable = None,
            extra: Any = None,
            on_transfer_extra_data: Any = None,
            proxy: Union[None, Any] = None,
            heart: int = 10  # 保活机制，ping/pong
    ):
        self.url = url
        self.data = data
        self.on_connected = on_connected
        self.on_reconnected = on_reconnected
        self.on_receive = on_receive
        self.on_ping = on_ping
        self.on_pong = on_pong
        self.on_fail = on_fail
        self.on_transfer = on_transfer
        self.on_transfer_extra_data = on_transfer_extra_data
        self.on_error = on_error
        self.extra = extra
        self.proxy = proxy
        self.heart = heart
