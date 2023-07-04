#!/usr/bin/python3
"""
2-matrix_divided module
for dividing all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    divides all elements of a matrix.
    args:
        matrix (int or float): a list of lists of integers or floats.
        div (int or float): a number (integer or float).
    return: a new matrix.
    """
    error_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list:
        raise TypeError(error_msg)

    len_prev_row = 0
    for row in matrix:
        if type(row) is not list:
            raise TypeError(error_msg)
        for column in row:
            if type(column) is not int and type(column) is not float:
                raise TypeError(error_msg)
        if len(row) != len_prev_row and len_prev_row != 0:
            raise TypeError("Each row of the matrix must have the same size")
        len_prev_row = len(row)

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(column / div, 2) for column in row] for row in matrix]
