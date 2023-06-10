#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    my_max = my_list[0]
    for n in my_list:
        if my_max < n:
            my_max = n
    return my_max
