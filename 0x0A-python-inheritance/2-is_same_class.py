#!/usr/bin/python3
"""
2-is_same_class function container
"""


def is_same_class(obj, a_class):
    """
    checks if the object is exactly an instance of the specified class.
    args:
        obj: object to be checked.
        a_class: class to confirm with the object.
    Return: True if the object is exactly an instance of the specified class,
    otherwise False.
    """
    if type(obj) is a_class:
        return True
    return False
