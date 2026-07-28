#!/usr/bin/python3
"""
Module containing the Square class.
Inherits from Rectangle.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class representation inheriting from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor for Square class."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size, updating both width and height."""
        self.width = value
        self.height = value

    def __str__(self):
        """Returns string representation of Square."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )

    def update(self, *args, **kwargs):
        """Updates attributes using positional (*args) or keyword (**kwargs) arguments."""
        attrs = ["id", "size", "x", "y"]
        if args and len(args) != 0:
            for i, arg in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                if key in attrs:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns dictionary representation of Square."""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
