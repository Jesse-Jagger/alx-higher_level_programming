#!/usr/bin/python3

""" Finds the peak in a list of unsorted integers"""


def find_peak(list_of_integers):

    if not list_of_integers:
        return None

    less, more = 0, len(list_of_integers) - 1

    while less < more:
        moderate = (less + more) // 2

        if list_of_integers[moderate] > list_of_integers[moderate + 1]:
            more = moderate
        else:
            less = moderate + 1

    return list_of_integers[less]
