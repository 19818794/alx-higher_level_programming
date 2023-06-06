#!/usr/bin/python3
for alpha in range(122, 96, -1):
    flag = True
    if alpha % 2 != 0:
        alpha -= 32
        flag = False
    print("{}".format(chr(alpha)), end="")
    if flag is False:
        alpha += 32
