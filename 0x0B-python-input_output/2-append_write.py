#!/usr/bin/python3

""" This program creates a function that appends to a file """


def write_file(filename="", text=""):
    """ Appending to a file """
    if not filename:
        print("Please provide a file name")
        return
    try:
        with open(filename, "a", encoding="utf-8") as file:
            nb = file.write(text)
            return nb
    except Exception as e:
        print(f"Error occured {e}")
