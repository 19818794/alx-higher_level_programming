#!/usr/bin/python3
"""
0-lookup function container.
"""


def lookup(obj):
    """
    gests the list of available attributes and methods of an object.
    args:
        obj: an object.
    Return: the list of available attributes and methods of an object.
    """
    return dir(obj)
