from typing import Any, Callable, Union

from RhinoObject.RhinoRequest.RhunoRequestEnum import Method


class RhinoRequest:
    def __init__(
            self,
            url: str,
            method: Union[Method] = Method.GET.value,
            params: Union[None, dict] = None,  # GET,DELETE
            data: Union[dict, str, bytes, None] = None,  # POST
            headers: Union[dict, None] = None,
            callback: Callable = None,
            on_failed: Callable = None,
            on_error: Callable = None,
            on_transfer: Callable = None,
            on_heart: Callable = None,
            extra: Any = None,
            on_transfer_extra_data: Any = None,
            timeout: int = 3,
            proxy: Union[None, Any] = None,
            is_sign: bool = True,
            special_sign: str = "data"
    ):
        """"""
        self.method = method
        self.url = url
        self.callback = callback
        self.params = params
        self.data = data
        self.headers = headers

        self.on_failed = on_failed
        self.on_error = on_error
        self.on_transfer = on_transfer
        self.on_heart = on_heart
        self.extra = extra
        self.on_transfer_extra_data = on_transfer_extra_data

        self.response = None
        self.timeout = timeout
        self.is_sign = is_sign
        self.proxy = proxy
        self.special_sign = special_sign
