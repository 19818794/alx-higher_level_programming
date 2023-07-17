#!/usr/bin/python3
"""
rectangle module is a class container.
"""
from models.base import Base


class Rectangle(Base):
    """
    class Rectangle is a subclass that inherits from Base.
    it uses private attributes with getter/setter and not directly public
    attribute, because we want to protect attributes of our class.
    with a setter, we are able to validate what a developer is trying
    to assign to a variable. So after, in our class we can "trust" these
    attributes.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        initializes private instance attributes.
        args:
            width: width of rectangle.
            height: height of rectangle.
            x: integer.
            y: integer.
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        retrieves the width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        sets a value to the width.
        """
        self.__width = value

    @property
    def height(self):
        """
        retrieves the height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        sets a value to the height.
        """
        self.__height = value

    @property
    def x(self):
        """
        retrieves the x.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        sets a value to the x.
        """
        self.__x = value

    @property
    def y(self):
        """
        retrieves the y.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        sets a value to the y.
        """
        self.__y = value
