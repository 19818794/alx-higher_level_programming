#!/usr/bin/python3
"""
8-rectangle module for creating a class Rectangle that inherits
frOOm BaseGeometry.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    a class Rectangle that inherits frOOm BaseGeometry to validat
    width and height inetegers.
    """

    def __init__(self, width, height):
        """
        initializes private instance attributes.
        argd:
            width: positive integer to be validated by integer_validator.
            height: positive integer to be validated by integer_validator.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
