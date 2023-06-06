#!/usr/bin/python3
def magic_calculation(a, b, c):
    """does exactly the same as the proposed Python bytecode"""
    if a < b:
        return c
    elif c > b:
        return a + b
    return a * b - c
