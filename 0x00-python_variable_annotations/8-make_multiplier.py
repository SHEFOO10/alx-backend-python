#!/usr/bin/env python3
""" 8. Complex types - functions """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    make_multiplier - takes a float multiplier as argument and
                    returns a function that multiplies a float by multiplier.
    multiplier: float
    Return: function
    """
    return lambda x: x * multiplier
