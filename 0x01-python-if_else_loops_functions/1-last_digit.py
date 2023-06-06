#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    digit = -1 * number
    sign = True
else:
    digit = number
    sign = False
while digit > 9:
    digit %= 10
if digit > 5 and sign is False:
    str = "and is greater than 5"
elif digit == 0:
    str = "and is 0"
else:
    str = "and is less than 6 and not 0"
    if sign is True:
        digit *= -1
print(f"Last digit of {number} is {digit} {str}")
