#!/usr/bin/python3
"""
Module for safely printing an integer using standard formatting
"""


def safe_print_integer(value):
    """
    Prints an integer with "{:d}".format().
    Returns True if successfully printed, otherwise False.
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
