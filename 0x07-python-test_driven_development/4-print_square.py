#!/usr/bin/python3
"""
4-print_square module
prints a square with character # of given size.
"""


def print_square(size):
    """
    prints a square with the character #.
    args:
        size (int): length of the square.
    return: square with the character #.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    for row in range(size):
        for column in range(size):
            print("#", end="")
        print()
