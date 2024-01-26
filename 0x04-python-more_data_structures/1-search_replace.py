#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    found = False

    for index, element in enumerate(new_list):
        if element == search:
            new_list[index] = replace
            found = True

    if not found:
        print("Element not found")
    return new_list
