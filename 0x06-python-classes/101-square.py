#!/usr/bin/python3
"""
we are not allowed to import any module.
"""


class Square:
    """
    a class Square that defines a square.
    """
    def __init__(self, size=0, position=(0, 0)) -> None:
        """
        initializes class attributes.
        args:
            size (int): integer indicateing the size of square,
                        otherwise if it is less than 0, raise the value error.
            position (int, int): position of the new square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        retrieves the size.
        """
        return self.__size

    @property
    def position(self):
        """
        retrieves the position.
        """
        return self.__position

    @size.setter
    def size(self, value):
        """
        sets a value to the size.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise TypeError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        """
        sets a value to the position.
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        returns the current square area.
        """
        return self.__size ** 2

    def my_print(self):
        """
        prints in stdout the square with the character #,
        otherwise if size is equal to 0, print an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()

    def __str__(self):
        """
        makes printing a Square instance should have the same behavior
        as my_print().
        """
        if self.__size != 0:
            for i in range(self.__position[1]):
                print()
        for i in range(self.__size):
            [print(" ", end="") for j in range(self.__position[0])]
            [print("#", end="") for j in range(self.__size)]
            if i != self.__size - 1:
                print()
        return ""
