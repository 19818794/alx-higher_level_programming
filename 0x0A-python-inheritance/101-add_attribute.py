#!/usr/bin/python3
"""
101-add_attribute is a function container.
"""


def add_attribute(obj, objname, value):
    """
    adds a new attribute to an object if it's possible.
    args:
        obj: a class object.
        objname: an object name.
        value: the value of attribute objname.
    """
    if hasattr(obj, "__dict__") is False:
        raise TypeError("can't add new attribute")
    setattr(obj, objname, value)
