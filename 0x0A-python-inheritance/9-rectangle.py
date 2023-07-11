#!/usr/bin/python3
"""
9-rectangle module based on 8-rectangle.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    a class Rectangle that inherits from BaseGeometry to validat
    width and height inetegers, and get the area and
    string representation of a rectangle.
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

    def area(self):
        """
        returns the area of a rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        prints a string representation of a rectangle.
        """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
