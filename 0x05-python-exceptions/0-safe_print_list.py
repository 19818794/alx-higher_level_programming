#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    len_list = 0
    counter = 0
    for item in my_list:
        len_list += 1
    try:
        if x == 0:
            print()
            return counter
        if x >= len_list:
            for item in my_list:
                print("{}".format(item), end="")
            print()
            return len_list
        else:
            for item in my_list:
                counter += 1
                print("{}".format(item), end="")
                if x == counter:
                    break
            print()
            return counter
    except BaseException:
        pass
