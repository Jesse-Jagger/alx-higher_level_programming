#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0

    num = 0
    den = 0

    for tupp in my_list:
        num += tupp[0] * tupp[1]
        den += tupp[1]

    return (num / den)
