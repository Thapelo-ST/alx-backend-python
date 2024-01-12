#!/usr/bin/env python3
"""
    function that accepts one argument multiply the argment with a function
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
        Accepts a float multiplier as an argument and returns a function.
        The returned function multiplies a float by the specified multiplier.
    """
    def mult_function(a: float) -> float:
        """
            Multiplieer function to be returned
        """
        return a * multiplier
    return mult_function
