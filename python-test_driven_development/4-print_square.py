#!/usr/bin/python3
"""
Module containing print_square function.
Prints a square with the character #.
"""


def print_square(size):
    """
    Prints a square with the '#' character of a given size.

    Args:
        size: Int size length of the square

    Raises:
        TypeError: If size is not an integer, or if size is a float < 0
        ValueError: If size is < 0
    """
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
