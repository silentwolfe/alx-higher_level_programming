#!/usr/bin/python3

""" The function reads from a file """


def read_file(filename=""):
    """ Reading from a file """
    if not filename:
        print("Provide a file name")
        return
    try:
        with open(filename, encoding="utf-8") as f:
            for line in f:
                print(line, end="")
    except FileNotFoundError:
        print(f"Couldn't find {filename}")
