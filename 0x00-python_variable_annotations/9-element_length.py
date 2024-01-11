#!/usr/bin/env python3from typing import List, Tuple
from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """
        accpets a list of strings as input and returns a list of tuples.
        Each tuple contains an element from the input list and its length.
    """
    return [(i, len(i)) for i in lst]
