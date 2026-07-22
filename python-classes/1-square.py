#!/usr/bin/python3
"""
This module defines a class Square with a private instance attribute size.
"""


class Square:
    """Defines a square by size."""

    def __init__(self, size):
        """
        Initializes a Square instance.

        Args:
            size: The size of the square.
        """
        self.__size = size
