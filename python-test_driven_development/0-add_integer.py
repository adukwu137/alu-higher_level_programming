#!/usr/bin/python3
"""
Module containing the add_integer function.
Adds two integers or floats cast to integers.
"""


def add_integer(a, b=98):
    """
    Adds two numbers after casting floats to integers.

    Args:
        a: First number (int or float)
        b: Second number (int or float, defaults to 98)

    Returns:
        Integer sum of a and b

    Raises:
        TypeError: If a or b is not an int or float
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
