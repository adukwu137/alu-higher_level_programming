#!/usr/bin/python3
"""
Module for safely printing only the integers from a mixed list
"""


def safe_print_list_integers(my_list=[], x=0):
    """
    Prints the first x elements of a list, filtering for integers only.
    Raises IndexError intentionally if x exceeds list capacity.
    """
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            continue
    print("")
    return count
