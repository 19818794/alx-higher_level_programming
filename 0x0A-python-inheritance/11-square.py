#!/usr/bin/python3
"""
11-square module based on 10-square.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    a class Square that inherits frOOm Rectangle
    to validate size by integer_validator,
    get the area and the string representation of the square.
    """

    def __init__(self, size):
        """
        initializes private instance attribute.
        args:
            size: positive integer to be validated by integer_validator.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        returns the area of the square.
        """
        return self.__size ** 2

    def __str__(self):
        """
        prints a string representation of a square.
        """
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
