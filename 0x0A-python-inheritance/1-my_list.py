#!/usr/bin/python3
"""Defines a class to inherit list."""


class MyList(list):
    """Implements print_sort."""

    def print_sorted(self):
        """Prints a list in sorted ascending order."""
        print(sorted(self))
