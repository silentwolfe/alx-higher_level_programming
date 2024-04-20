#!/usr/bin/python3

""" Module that contains a function that provides
a json representation all object passed into it
"""
import json


def to_json_string(my_obj):
    """Json representation

    Args:
        my_obj (object): The object to be stringified

    Returns:
        string: The json help decode the data type into that
        of a string.
    """
    return json.dumps(my_obj)
