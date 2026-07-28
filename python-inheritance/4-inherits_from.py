#!/usr/bin/python3
"""
This module defines a function that checks if an object is an instance of
a class that inherited (directly or indirectly) from a specified class.
"""


def inherits_from(obj, a_class):
    """Returns True if obj inherited from a_class, otherwise False."""
    return type(obj) is not a_class and isinstance(obj, a_class)
