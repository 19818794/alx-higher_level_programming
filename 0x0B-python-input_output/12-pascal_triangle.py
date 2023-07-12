#!/usr/bin/python3
"""
12-pascal_triangle module function container.
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascal's triangle of n
    args:
        n (int): an integer.
    Return: an empty list if n <= 0.
    """
    rows = [[1 for j in range(i + 1)] for i in range(n)]
    for i in range(n):
        for j in range(i - 1):
            rows[i][j + 1] = sum(rows[i - 1][j: j + 2])
    return rows
