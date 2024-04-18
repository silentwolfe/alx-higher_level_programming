#!/usr/bin/python3

""" Checks if obj is exactly an instance of the same class"""


def is_same_class(obj, a_class):
    """_summary_

    Args:
        obj (): The object to check
        a_class (): The class used to compare with.

    Returns:
        True: if its exactly the same type
        else False: if otherwise
    """
    return type(obj) is a_class
