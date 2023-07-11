#!/usr/bin/python3
"""
0-read_file module function container.
"""


def read_file(filename=""):
    """
    reads a text file (UTF8) and prints it to stdout.
    args:
        filename: a file name.
    """
    with open(filename, "r", encoding="utf-8") as file:
        read_bytes = file.read()
        print(read_bytes, end="")
