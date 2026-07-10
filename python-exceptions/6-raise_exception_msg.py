#!/usr/bin/python3
"""
Module for raising a NameError exception with a custom message
"""


def raise_exception_msg(message=""):
    """
    Raises a NameError exception along with a descriptive message.
    """
    raise NameError(message)
