#!/usr/bin/python3
"""
4-inherits_from function container.
"""


def inherits_from(obj, a_class):
    """
    checks if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class.

    args:
        obj: object to be checked.
        a_class: class to confirm with the object.

    Return: True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class, otherwise False.
    """
    if type(obj) is not a_class and isinstance(obj, a_class):
        return True
    return False
