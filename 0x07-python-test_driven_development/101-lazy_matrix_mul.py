#!/usr/bin/python3
"""
101-lazy_matrix_mul module
has only a function that multiplies 2 matrices
by using the module NumPy.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    multiplies 2 matrices by using the module NumPy.
    args:
        m_a: the first list of lists of integers or floats.
        m_b: the second list of lists of integers or floats.
    return: a new matrix.
    """
    return np.matmul(m_a, m_b).tolist()
