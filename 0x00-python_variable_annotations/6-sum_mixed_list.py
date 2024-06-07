#!/usr/bin/env python3
""" 6. complex types - mixed list """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    sum_mixed_list - takes a list mxd_lst of integers and floats
                        and returns their sum as a float.
    mxd_lst: list[int | float]
    Return : float
    """
    return sum(mxd_lst)
