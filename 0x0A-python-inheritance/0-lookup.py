#!/usr/bin/python3
"""Module 0-lookup
Find list of available attributes & methods of object
"""


def lookup(obj):
    """Returns that list of attributes and methods

    Args:
        - obj: object to look into
    """

    return dir(obj)
