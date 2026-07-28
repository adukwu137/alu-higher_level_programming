#!/usr/bin/python3
"""
Module containing the Base class.
This class serves as the foundation for all future classes in the project.
"""


class Base:
    """
    Base class to manage the id attribute across all project instances.

    Attributes:
        __nb_objects (int): Private class attribute tracking instance count.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor for the Base class.

        Args:
            id (int, optional): Custom ID value. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
