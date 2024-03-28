#!/usr/bin/python3

"""contains the function find_peak"""


def find_peak(list_of_integers):

    """finds a peak in a list of unsorted integers"""
    li_st = list_of_integers
    lent = len(li_st)
    if lent == 0:
        return
    i = lent // 2
    if (i == lent - 1 or li_st[m] >= li_st[i + 1]) and (i == 0 or li_st[i] >= li_st[i - 1]):
        return li_st[i]
    if i != lent - 1 and li_st[i + 1] > li_st[i]:
        return find_peak(li_st[i + 1:])
    return find_peak(li_st[:i])
