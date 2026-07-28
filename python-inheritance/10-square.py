#!/usr/bin/python3
"""
This module defines a Square class that inherits from Rectangle.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A Square class inherited from Rectangle."""

    def __init__(self, size):
        """Initializes a Square instance with size."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Returns the area of the square."""
        return self.__size ** 2
