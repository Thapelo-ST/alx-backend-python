#!/usr/bin/env python3
""" accepts a string and an int or float then returns a turple """
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
        accepts a string and an int or float then returns a turple
    """
    return k, float(v ** 2)