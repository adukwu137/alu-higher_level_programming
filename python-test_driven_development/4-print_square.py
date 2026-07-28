#!/usr/bin/python3
"""
Module containing print_square function.
Prints a square using # characters.
"""


def print_square(size):
    """
    Prints a square with character '#' of given size length.

    Args:
        size: Side length of square (integer)

    Raises:
        TypeError: If size is not an integer
        ValueError: If size is less than 0
    """
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
