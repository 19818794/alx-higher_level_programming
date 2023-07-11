#!/usr/bin/python3
"""
3-is_kind_of_class function container.
"""


def is_kind_of_class(obj, a_class):
    """
    checks if the object is an instance of, or if the object is
    an instance of a class that inherited from, the specified class.

    args:
        obj: object to be checked.
        a_class: class to confirm with the object.

    Return: True if the object is an instance of, or if the object is
    an instance of a class that inherited from, the specified class,
    otherwise False.
    """
    return isinstance(obj, a_class)
