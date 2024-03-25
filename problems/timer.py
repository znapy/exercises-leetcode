# -*- coding: utf-8 -*-
"""Timer decorator."""

from time import time
from typing import Callable, Any, Optional


def timer(func: Callable) -> Any:
    """Timer decorator."""
    def wrapper(*args: Optional[Any], **kwargs: Optional[Any]) -> Any:
        tic = time()
        result = func(*args, **kwargs)
        toc = time()
        print(f"timer: {toc - tic:0.8f} seconds ({func.__name__})")
        return result
    return wrapper
