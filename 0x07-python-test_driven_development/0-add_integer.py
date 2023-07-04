#!/usr/bin/python3

"""
0-add_integer module
for integers addition.
it contains only one function.
"""


def add_integer(a, b=98):
    """
    adds 2 integers.
    args:
        a (int or float): first number.
        b (int or float): second number.
    return:
        an integer indicating the addition of a and b.
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
