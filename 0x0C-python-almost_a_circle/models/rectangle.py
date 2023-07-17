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
        self.validation("width", width)
        self.__width = width
        self.validation("height", height)
        self.__height = height
        self.validation("x", x)
        self.__x = x
        self.validation("y", y)
        self.__y = y

    def validation(self, name, value):
        """
        validates private instance attributes for all setter methods
        and instantiation.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if (name == "width" or name == "height") and value <= 0:
            raise ValueError("{} must be > 0".format(name))
        if (name == "x" or name == "y") and value < 0:
            raise ValueError("{} must be >= 0".format(name))

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
        self.validation("width", value)
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
        self.validation("height", value)
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
        self.validation("x", value)
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
        self.validation("y", value)
        self.__y = value

    def area(self):
        """
        returns the area value of the Rectangle instance.
        """
        return self.__width * self.__height

    def display(self):
        """
        prints in stdout the Rectangle instance with the character #.
        """
        for y in range(self.__y):
            print()
        for i in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """
        returns a string representatiob of a Rectangle instance.
        """
        output = "[Rectangle] ({}) {}/{} - {}/{}".format(
                 self.id, self.__x, self.__y, self.__width, self.__height)
        return output
