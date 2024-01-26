#!/usr/bin/python3

def uniq_add(my_list=[]):
    uniq_element = list(set(my_list))
    sum_total = 0

    for total in uniq_element:
        sum_total += total
    return sum_total
