#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    sorted_dict = sorted(a_dictionary.items(), key=lambda item: item[0])

    for key, value in sorted_dict:
        print(f'{key}: {value}')
