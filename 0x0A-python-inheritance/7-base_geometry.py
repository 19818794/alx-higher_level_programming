#!/usr/bin/python3
"""
7-base_geometry module based on 6-base_geometry
to create two public instance method.
"""


class BaseGeometry:
    """
    a class for two public instance method.
    """

    def area(self):
        """
        raises an Exception.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates value.
        args:
            name: the name of the variable.
            value: the value of the variable.
        Return: Exceptions.
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
