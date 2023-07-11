#!/usr/bin/python3
"""
6-load_from_json_file module function container.
"""
import json


def load_from_json_file(filename):
    """
    creates an Object frOOm a "JSON file".
    args:
        filename: the name of the file.
    Return: an object.
    """
    with open(filename, "r", encoding="utf-8") as file:
        my_object = json.load(file)
        return my_object
