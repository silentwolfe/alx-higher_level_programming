#!/usr/bin/python3

"""_summary_
The function checks for if the object is an instance of,
or if the object is an instance of a class that inherited
from, the specified class.
"""


def is_kind_of_class(obj, a_class):
    """_summary_

    Args:
        obj: object to be checked
        a_class: To be checked against
    Returns:
        True: If the object is an instanceof.
        False: Otherwise.
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
