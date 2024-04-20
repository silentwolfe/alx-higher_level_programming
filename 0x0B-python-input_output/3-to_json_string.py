#!/usr/bin/python3
import json

"""_summary_:
        The function stringifies all object passed into it
"""

def to_json_string(my_obj):
    """_summary_

    Args:
        my_obj (object): The function stringifies

    Returns:
        _type_: the strings 
    """
    return json.dumps(my_obj)