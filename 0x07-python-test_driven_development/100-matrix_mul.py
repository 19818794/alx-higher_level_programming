#!/usr/bin/python3
"""
100-matrix_mul module
has only one function that multiplies 2 matrices.
"""


def matrix_mul(m_a, m_b):
    """
    multiplies 2 matrices.
    args:
        m_a: the first list of lists of integers or floats.
        m_b: the second list of lists of integers or floats.
    return: a new matrix.
    """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    len_prev_row_m_a = 0
    for row in m_a:
        if type(row) is not list:
            raise TypeError("m_a must be a list of lists")
        if row == []:
            raise ValueError("m_a can't be empty")
        for column in row:
            if type(column) is not int and type(column) is not float:
                raise TypeError("m_a should contain only integers or floats")
        if len(row) != len_prev_row_m_a and len_prev_row_m_a != 0:
            raise TypeError("each row of m_a must be of the same size")
        len_prev_row_m_a = len(row)

    len_prev_row_m_b = 0
    for row in m_b:
        if type(row) is not list:
            raise TypeError("m_b must be a list of lists")
        if row == []:
            raise ValueError("m_b can't be empty")
        for column in row:
            if type(column) is not int and type(column) is not float:
                raise TypeError("m_b should contain only integers or floats")
        if len(row) != len_prev_row_m_b and len_prev_row_m_b != 0:
            raise TypeError("each row of m_b must be of the same size")
        len_prev_row_m_b = len(row)

    len_row_m_a = len(m_a)
    len_column_m_a = len(m_a[0])
    len_row_m_b = len(m_b)
    len_column_m_b = len(m_b[0])
    if len_column_m_a != len_row_m_b:
        raise ValueError("m_a and m_b can't be multiplied")

    m_c = [[0 for _ in range(len_column_m_b)] for _ in range(len_row_m_a)]
    for i in range(len_row_m_a):
        for j in range(len_column_m_b):
            for k in range(len_column_m_a):
                m_c[i][j] += m_a[i][k] * m_b[k][j]

    return m_c
