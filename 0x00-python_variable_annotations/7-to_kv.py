#!/usr/bin/env python3
""" 7. Complex types - string and int/float to tuple """
from typing import Tuple, Union


def to_kv(k: str, v: int | float) -> Tuple[str, float]:
    """
    to_kv -  takes a string k and an int OR float v
                    as arguments and returns a tuple.
    k: str
    v: int | float
    Return: Tuple
    """
    return (k, float(v**2))
