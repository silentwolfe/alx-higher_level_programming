#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) < 1:
        return None
    else:
        max_val = my_list[0]
        for elem in my_list:
            if elem > max_val:
                max_val = elem
        return max_val
