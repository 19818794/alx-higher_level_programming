#!/usr/bin/python3
"""
3-to_json_string module function container.
"""
import json


def to_json_string(my_obj):
    """
    returns the JSON representation of an object (string).
    args:
        my_obj (str): an object.
    """
    return json.dumps(my_obj)
