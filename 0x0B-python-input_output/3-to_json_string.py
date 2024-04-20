import json
#!/usr/bin/python3

""" The function stringifies all object passed into it """


def to_json_string(my_obj):
    """
    Args:
        my_obj (object): The function stringifies

    Returns:
        _type_: the strings
    """
    return json.dumps(my_obj)
