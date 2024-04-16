#!/usr/bin/python3

""" The function reads from a file """


def read_file(filename=""):
    """ Reading from a file """
    with open(filename, encoding="utf-8") as f:
        print(f.read())
