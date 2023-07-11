#!/usr/bin/python3
"""
100-my_int module for a class MyInt that inherits frOOm int.
"""


class MyInt(int):
    """
    a class MyInt that inherits frOOm int.
    """

    def __eq__(self, second):
        """
        defines == operator inverted.
        """
        return int(self) != int(second)

    def __ne__(self, second):
        """
        defines != operator inverted.
        """
        return int(self) == int(second)
