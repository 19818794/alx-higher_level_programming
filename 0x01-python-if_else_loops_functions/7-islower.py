#!/usr/bin/python3
def islower(c):
    """checks for lowercase character.
    Returns True if c is lowercase, False otherwise.
    """
    if ord(c) in range(97, 123):
        return True
    else:
        return False
