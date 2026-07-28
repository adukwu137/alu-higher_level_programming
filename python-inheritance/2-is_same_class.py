#!/usr/bin/python3
"""
This module defines a function that checks exact class instance matching.
"""


def is_same_class(obj, a_class):
    """Returns True if obj is exactly an instance of a_class; otherwise False.

    Args:
        obj: The object to check.
        a_class: The class to match against.

    Returns:
        bool: True if type(obj) is a_class, False otherwise.
    """
    return type(obj) is a_class
