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
        super().__init__(size, size, x, y, id)
        self.validation("width", size)
        self.size = size

    def __str__(self):
        """
        returns a string representatiob of a Square instance.
        """
        output = "[Square] ({}) {}/{} - {}".format(
                 self.id, self.x, self.y, self.width)
        return output

    @property
    def size(self):
        """
        retrieves the size.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        sets a value to the size.
        """
        self.validation("width", value)
        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        """
        assigns attributes.
        args:
            *args: is the list of arguments - no-keyworded arguments.
                    id: 1st argument should be the id attribute.
                    size: 2nd argument should be the size attribute.
                    x: 3rd argument should be the x attribute.
                    y: 4th argument should be the y attribute.
            **kwargs: must be skipped if *args exists and is not empty. Each
                key in this dictionary represents an attribute to the instance.
        """
        if args is not None and len(args) != 0:
            if len(args) >= 1:
                if type(args[0]) != int and args[0] is not None:
                    raise TypeError("id must be an integer")
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    if type(value) != int and value is not None:
                        raise TypeError("id must be an integer")
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
