#!/usr/bin/python3

""" The function turns json represented objects
into actaul objects
"""
import json


def from_json_string(my_str):
    """From json strings to objects

    Args:
        my_str (json_strings): The json string to be converted
    """
    return json.loads(my_str)
