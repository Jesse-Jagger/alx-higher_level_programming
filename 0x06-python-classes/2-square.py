#!/usr/bin/python3

"""This module creates square class"""


class Square:
    """Class Square that defines a square.
    """
    def __init__(self, size=0):

        if type(size).__name__ != "int":
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        
