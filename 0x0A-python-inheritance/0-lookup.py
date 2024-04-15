#!/usr/bin/bash

# 0-lookup.py
# created by Osaro. E

""" This function returns a list of all methods and attributes """


def lookup(obj):
    """ The returning of a list """
    return list(dir(obj))
