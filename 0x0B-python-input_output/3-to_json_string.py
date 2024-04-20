#!/usr/bin/python3
import json

""" The function stringifies all object passed into it """


def to_json_string(my_obj):
    """ my_obj (object): The function stringifies """
    return json.dumps(my_obj)
