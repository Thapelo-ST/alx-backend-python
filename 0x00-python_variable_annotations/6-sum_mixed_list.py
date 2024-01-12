#!/usr/bin/env python3
"""
    Function that adds up a list of numbers (ints and floats).
"""
from typing import List, Union


def sum_mixed_list(input_list: List[Union[int, float]]) -> float:
    """
        Takes a list of numbers (ints and floats) as
        an argument and returns their sum as a float.
    """
    result: float = 0.0

    for num in input_list:
        result += num

    return result
