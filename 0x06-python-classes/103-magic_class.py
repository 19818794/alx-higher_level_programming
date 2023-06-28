#!/usr/bin/python3
"""
allowed to import any module.
"""
import math


class MagicClass:
    """
    defines a Python class MagicClass that does exactly the same as
    the provided Python bytecode.
    """
    def __init__(self, radius=0):
        """
        initializes class attributes.
        args:
            radius (int or float): radius for a new MagicClass.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """
        returns the area of the MagicClass.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        returns the circumference of the MagicClass.
        """
        return self.__radius * 2 * math.pi
