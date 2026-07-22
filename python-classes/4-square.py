#!/usr/bin/python3
"""
This module defines a class Square.
"""


class Square:
    """Defines a square with private size, getter, setter, and area."""

    def __init__(self, size=0):
        """
        Initializes a Square instance with optional size.

        Args:
            size (int): The size of the square (default 0).
        """
        self.size = size

    @property
    def size(self):
        """
        Getter property for private attribute __size.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter property for private attribute __size with validation.

        Args:
            value (int): The new size value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates and returns the current square area.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size ** 2
