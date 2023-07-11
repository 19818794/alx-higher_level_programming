#!/usr/bin/python3
"""
5-save_to_json_file module function container.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    writes an Object to a text file, using a JSON representation.
    args:
        my_obj: an object.
        filename: the name of the file.
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
