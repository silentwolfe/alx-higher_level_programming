#!/usr/bin/python3

# File - 1-my_list.py
# Created by Osaro.E

""" Inheriting the methods and properties of the class list. """


class MyList(list):
    
    """ The function prints out a sorted list.
    Returns:
    None
    """

    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
