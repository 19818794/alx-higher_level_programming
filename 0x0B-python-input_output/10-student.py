#!/usr/bin/python3
"""
10-student module based on 9-student.
"""


class Student:
    """
    defines a student.
    """

    def __init__(self, first_name, last_name, age):
        """
        initialize public instance attributes.
        args:
            first_name: the student's first name.
            last_name: the student's last name.
            age: the student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation of a Student instance
        (same as 8-class_to_json.py).
        args:
            attrs (list): attribute names.
        """
        if attrs is not None:
            dic = {i: self.__dict__[i] for i in self.__dict__.keys() & attrs}
            return dic
        return self.__dict__
