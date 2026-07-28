#!/usr/bin/python3
"""
Module containing say_my_name function.
Prints 'My name is <first name> <last name>'.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints full name formatted as 'My name is <first_name> <last_name>'.

    Args:
        first_name: First name string
        last_name: Last name string (defaults to "")

    Raises:
        TypeError: If either parameter is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
