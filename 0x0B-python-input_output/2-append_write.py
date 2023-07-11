#!/usr/bin/python3
"""
2-append_write module function container.
"""


def append_write(filename="", text=""):
    """
    appends a string at the end of a text file (UTF8).
    args:
        filename: name of the file.
        text: the text to be added at the end of a text file.
    Return: the number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as file:
        written_bytes = file.write(text)
        return written_bytes
