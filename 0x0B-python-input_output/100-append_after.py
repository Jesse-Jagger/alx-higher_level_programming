#!/usr/bin/python3

"""Defines a function for inserting to a textfile."""


def append_after(filename="", search_string="", new_string=""):
    """Inserts text after each line containing a specific string in a file.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for within the file.
        new_string (str): The string to insert.
    """
    text = ""
    with open(filename) as readme:
        for line in readme:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, mode="w") as newfile:
       newfile.write(text)

