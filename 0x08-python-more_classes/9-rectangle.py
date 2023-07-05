#!/usr/bin/python3
"""
9-rectangle module for Rectangle class.
"""


class Rectangle:
    """
    class Rectangle defines a rectangle
    with two private instance attribute,
    their propoerties, and setters.
    Also with public instance methods,
    print(), str(), repr(), del().
    It also defines public class attributes,
    a static method, and a class method.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        initializes private instance attribute.
        It also increments a public class attribute
        during each new instance instantiation.
        args:
            width (int): width of rectangle.
            height (int): height of rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """
        makes printing a Rectangle instance with producing it
        in a string representation.
        """
        string_representation = ""
        if self.__width != 0 and self.__height != 0:
            string_representation += "\n".join(str(self.print_symbol) *
                                               self.__width
                                               for i in range(self.__height))
        return string_representation

    def __repr__(self):
        """
        returns a string representation of the rectangle to be able to
        recreate a new instance by using eval().
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """
        prints a message when an instance of Rectangle is deleted.
        It also decrements a public class attribute
        during each instance deletion.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        returns the biggest rectangle based on the area.
        """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """
        returns a new Rectangle instance with width == height == size.
        """
        return cls(size, size)
