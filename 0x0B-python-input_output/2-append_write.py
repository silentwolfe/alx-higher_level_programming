#!/usr/bin/python3

""" This program creates a function that appends to a file """


def append_write(filename="", text=""):
    """ Appending text contents to a file """
    if not filename:
        print("Please provide a file name")
        return
    try:
        with open(filename, "a", encoding="utf-8") as file:
            nb = file.write(text)
            return nb
    except Exception as e:
        print(f"Error occured {e}")
    except PermissionError:
        print("[PermissionError] [Errno 13] Permission denied: 'no_perm/o_file'")