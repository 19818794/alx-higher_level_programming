#!/usr/bin/python3
def fizzbuzz():
    """prints the numbers from 1 to 100 separated by a space.
    For multiples of three print Fizz instead of the number,
    and for multiples of five print Buzz.
    For numbers which are multiples of both three and five print FizzBuzz.
    """
    for n in range(1, 101):
        if (n % 3 == 0) and (n % 5 == 0):
            print(f"FizzBuzz", end=" ")
        elif (n % 5 == 0) and not (n % 3 == 0):
            print(f"Buzz", end=" ")
        elif not (n % 5 == 0) and (n % 3 == 0):
            print(f"Fizz", end=" ")
        else:
            print(f"{n}", end=" ")
