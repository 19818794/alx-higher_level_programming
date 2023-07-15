#!/usr/bin/python3
"""
base module is a class container.
"""


class Base:
    """
    this class will be the "base" of all other classes in this project.
    the goal of it is to manage id attribute in all your future classes,
    and to avoid duplicating the same code (by extension, same bugs).
    args:
        nb_objects: a private class attribute indicating the number of
        objects created.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        initializes a public instance attribute.
        args:
            id (int): object indentifier.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
