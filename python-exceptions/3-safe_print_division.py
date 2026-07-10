#!/usr/bin/python3
"""
Module for safely dividing two integers with detailed block reporting
"""


def safe_print_division(a, b):
    """
    Divides two integers and prints the outcome in the finally clause.
    Returns the division value if successful, otherwise None.
    """
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        pass
    finally:
        print("Inside result: {}".format(result))
    return result
