#!/usr/bin/python3
"""
This module defines a class Square.
"""


class Square:
    """Defines a square by size, position, area, and print capabilities."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square (default 0).
            position (tuple): A tuple of 2 positive integers (default (0, 0)).
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Getter property for private attribute __position.

        Returns:
            tuple: The position tuple of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter property for private attribute __position with validation.

        Args:
            value (tuple): A tuple of 2 positive integers.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (type(value) is not tuple or
                len(value) != 2 or
                type(value[0]) is not int or
                type(value[1]) is not int or
                value[0] < 0 or
                value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates and returns the current square area.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints in stdout the square with the character #, offsetting by position.
        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print("")
            return

        for _ in range(self.__position[1]):
            print("")

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
