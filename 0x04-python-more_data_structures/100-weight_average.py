#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    result = sum(list(map(lambda n: n[0] * n[1], my_list)))
    sum_weight = sum(list(map(lambda n: n[1], my_list)))
    return result / sum_weight
