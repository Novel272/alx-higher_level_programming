#!/usr/bin/python3
"""Module is_same_class
Finds if object is exactly instance of a class
"""


def is_same_class(obj, a_class):
    """Function to determine if obj is instance of a_class

    Args:
        - obj: object to look 
        - a_class: class to verify instanceof

    Returns: True if obj is instance of a_class
    False other wise
    """

    return True if type(obj) is a_class else False
