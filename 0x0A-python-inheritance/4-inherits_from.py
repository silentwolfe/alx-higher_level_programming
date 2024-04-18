#!/usr/bin/python3

"""_summary_
"""


def inherits_from(obj, a_class):
    """_summary_

    Args:
        obj: Object to be Compared with
        a_class: class compared against.
    Returns:
        True: If it is directly or indirectly an instance of
        the class
        False: If it isnt at all.
    """

    return issubclass(type(obj), a_class) and type(obj) is not a_class
