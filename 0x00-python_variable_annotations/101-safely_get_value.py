#!/usr/bin/env python3
"""
   Safely gets the value from a dictionary by key.
"""
from typing import TypeVar, Mapping, Any, Union, Optional
T = TypeVar('T')


def safely_get_value(dct: Mapping, key:
                     Any, default:
                     Optional[T] = None) -> Union[Any, T]:
    """
        Safely gets the value from a dictionary by key.
    """
    if key in dct:
        return dct[key]
    else:
        return default
