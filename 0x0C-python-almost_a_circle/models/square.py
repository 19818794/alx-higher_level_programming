#!/usr/bin/python3
"""
square module is a class container.
"""
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class Square is a subclass that inherits from Rectangle.
    As you know, a Square is a special Rectangle,
    so it makes sense this class Square inherits from Rectangle.
    Now you have a Square class who has the same attributes and same methods.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        initializes private instance attributes.
        args:
            size: width and the heigh of a square.
            x: integer.
            y: integer.
            id: identifier
        """
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        returns a string representatiob of a Square instance.
        """
        output = "[Square] ({}) {}/{} - {}".format(
                 self.id, self.x, self.y, self.width)
        return output
