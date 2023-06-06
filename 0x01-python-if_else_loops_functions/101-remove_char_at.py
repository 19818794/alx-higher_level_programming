#!/usr/bin/python3
def remove_char_at(str, n):
    """creates a copy of the string, removing the character at the position n
    (not the Python way, the “C array index”).
    """
    i = 0
    str_copy = ""
    for c in str:
        if i != n:
            str_copy += c
        i += 1
    return str_copy
