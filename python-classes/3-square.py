#!/usr/bin/python3
"""
This module defines a class Square.
"""


class Square:
    """Defines a square with size and area computation."""

    def __init__(self, size=0):
        """
        Initializes a Square instance with optional size.

        Args:
            size (int): The size of the square (default 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculates and returns the current square area.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size ** 2
