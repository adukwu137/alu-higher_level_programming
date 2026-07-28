#!/usr/bin/python3
"""
Module containing matrix_divided function.
Divides all elements of a matrix by a divisor.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div, rounded to 2 decimal places.

    Args:
        matrix: List of lists of integers or floats
        div: Number (integer or float) to divide matrix elements by

    Returns:
        A new matrix containing the division results

    Raises:
        TypeError: If matrix is invalid or rows differ in size,
                   or div is not a number
        ZeroDivisionError: If div is equal to 0
    """
    msg_type = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(msg_type)

    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(msg_type)
        for elem in row:
            if type(elem) not in [int, float]:
                raise TypeError(msg_type)

    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(elem / div, 2) for elem in row] for row in matrix]
