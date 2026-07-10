#!/usr/bin/python3
"""
Module for safely printing elements of a list
"""


def safe_print_list(my_list=[], x=0):
    """
    Prints x elements of a list on the same line.
    Returns the actual number of elements printed.
    """
    count = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            count += 1
        except IndexError:
            break
    print("")
    return count
