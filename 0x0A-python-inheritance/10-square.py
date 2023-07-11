#!/usr/bin/python3
"""
10-square module inherits frOOm Rectangle frOOm 9-rectangle.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    a class Square that inherits frOOm Rectangle
    to validate size by integer_validator and get the area of the square.
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
