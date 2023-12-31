#!/usr/bin/python3
"""Defines a function for checking inheritance."""


def is_same_class(obj, a_class):
    """Checks if an object is an instance of a given class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to check the obj to.
    Returns:
        If obj exactly an instance of a_class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
