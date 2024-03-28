#!/usr/bin/python3

""" Finds the peak in a list of unsorted integers"""

def find_peak(list_of_integers):

    """finds a peak in a list of unsorted integers"""

    li_st = list_of_integers
    ln = len(li_st)
    if ln == 0:
        return
    i = ln // 2
    if (i == ln - 1 or li_st[i] >= li_st[i + 1]) and (i == 0 or li_st[i] >= li_st[i - 1]):
        return li_st[i]
    if i != ln - 1 and li_st[i + 1] > li_st[i]:
        return find_peak(li_st[i + 1:])
    return find_peak(li_st[:i])
