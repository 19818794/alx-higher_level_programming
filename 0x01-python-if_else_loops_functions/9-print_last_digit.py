#!/usr/bin/python3
def print_last_digit(number):
    """prints the last digit of a number.
    Returns the value of the last digit
    """
    if number < 0:
        digit = -1 * number
    else:
        digit = number
    while digit > 9:
        digit %= 10
    print(f"{digit:d}", end="")
    return digit
