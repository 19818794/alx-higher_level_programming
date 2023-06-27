#!/usr/bin/python3
"""
we are not allowed to import any module.
"""


class Square:
    """
    a class Square that defines a square by private instance attribute: size.
    """
    def __init__(self, size=0):
        """
        initializes class attributes.
        args:
            size (int): integer indicateing the size of square,
                    otherwise if it is less than 0, raise the value error.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise TypeError("size must be >= 0")
        else:
            self.__size = size
