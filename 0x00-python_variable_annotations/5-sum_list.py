#!/usr/bin/env python3
"""
    function that adds up a list of inputs that are floats
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
        function that adds up a list of inputs that are floats
    """
    result: float = 0
    for num in input_list:
        result += num
    return result
