#!/usr/bin/python3
"""
100-append_after module function container.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    inserts a line of text to a file, after each line
    containing a specific string.
    args:
        filename: the name of the file.
        search_string: the string to be repleaced.
        new_string: the strinf to be inserted.
    """
    lines = []
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()
        i = 0
        while i < len(lines):
            if search_string in lines[i]:
                lines[i: i + 1] = [lines[i], new_string]
                i += 1
            i += 1
    with open(filename, "w", encoding="utf-8") as file:
        file.writelines(lines)
