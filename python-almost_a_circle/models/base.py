#!/usr/bin/python3
"""
Module containing the Base class.
Serves as the foundation for future geometry classes.
"""


class Base:
    """
    Base class to manage id attribute in all future classes.

    Attributes:
        __nb_objects (int): Private class attribute tracking instances.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor for Base class.

        Args:
            id (int, optional): ID value for instance. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
