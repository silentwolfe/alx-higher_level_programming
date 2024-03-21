#!/usr/bin/python3

def best_score(a_dictionary):
    max_value = float('-inf')
    best_key = None

    if a_dictionary == None:
        return None

    for key, value in a_dictionary.items():
        if value > max_value:
            max_value = value
            best_key = key
    return best_key
