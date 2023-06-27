#!/usr/bin/python3
"""
we are not allowed to import any module.
"""


class Square:
    """
    a class Square that defines a square by private instance attribute: size.
    """
    def __init__(self, size=0) -> None:
        """
        initializes class attributes.
        args:
            size (int): integer indicateing the size of square,
                    otherwise if it is less than 0, raise the value error.
        """
        self.__size = size

    @property
    def size(self):
        """
        retrieves the size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        sets a value to the size.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise TypeError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        returns the current square area.
        """
        return self.__size ** 2
