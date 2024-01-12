#!/usr/bin/env python3
""" function fixed for mypy and pycodestyle """
from typing import List, Any


def zoom_array(lst: List[Any], factor: int = 2) -> List[Any]:
    """ function fixed for mypy and pycodestyle """
    zoomed_in: List[Any] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in
