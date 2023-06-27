#!/usr/bin/python3
"""
we are not allowed to import any module.
"""


class Square:
    """
    a class Square that defines a square by private instance attribute: size.
    """
    def __init__(self, size):
        """
        initializes class attributes.
        args:
            size: size of square, with no type/value verification.
        """
        self.__size = size
