#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) in range(97, 123):
            c = chr(ord(c) - 32)
        print("{}".format(c), end="")
    print()
