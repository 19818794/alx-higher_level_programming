#!/usr/bin/python3
"""
2-rectangle module for Rectangle class.
"""


class Rectangle:
    """
    class Rectangle defines a rectangle
    with two private instance attribute,
    their propoerties, and setters.
    Also with public instance methods.
    """
    def __init__(self, width=0, height=0):
        """
        initializes private instance attribute.
        args:
            width (int): width of rectangle.
            height (int): height of rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        retrieves the width
        """
        return self.__width

    @property
    def height(self):
        """
        retrieves the height
        """
        return self.__height

    @width.setter
    def width(self, value):
        """
        sets a value for width.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
        sets a value for height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        returns the rectangle area.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        returns the rectangle perimeter.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
