#!/usr/bin/python3
"""
1-write_file module function container.
"""


def write_file(filename="", text=""):
    """
    writes a string to a text file (UTF8).
    args:
        filename: the name of the file to be read.
        text: the text to be added to the file.
    Return: the number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as file:
        written_bytes = file.write(text)
        return written_bytes
