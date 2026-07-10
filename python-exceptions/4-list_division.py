#!/usr/bin/python3
"""
Module for dividing elements of two lists with comprehensive error handling
"""


def list_division(my_list_1, my_list_2, list_length):
    """
    Divides elements of two lists up to list_length.
    Handles type, division, and index range exceptions gracefully.
    """
    new_list = []
    for i in range(list_length):
        div_result = 0
        try:
            val_1 = my_list_1[i]
            val_2 = my_list_2[i]
            div_result = val_1 / val_2
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(div_result)
    return new_list
