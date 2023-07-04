#!/usr/bin/python3
"""
3-say_my_name module
takes two strings and prints a sentance.
"""


def say_my_name(first_name, last_name=""):
    """
    prints My name is <first name> <last name>.
    args:
        first_name (string): first string.
        last_name (string): second string.
    return: full sentence.
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
