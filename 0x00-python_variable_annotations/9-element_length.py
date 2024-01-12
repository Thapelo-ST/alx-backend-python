#!/usr/bin/env python3
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
        accpets a list of strings as input and returns a list of tuples.
        Each tuple contains an element from the input list and its length.
    """
    return [(i, len(i)) for i in lst]
