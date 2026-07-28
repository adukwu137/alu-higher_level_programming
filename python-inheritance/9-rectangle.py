#!/usr/bin/python3
"""
This module defines a full Rectangle class that inherits from BaseGeometry.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A Rectangle class inherited from BaseGeometry."""

    def __init__(self, width, height):
        """Initializes a Rectangle instance with width and height."""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Returns string representation of the rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
