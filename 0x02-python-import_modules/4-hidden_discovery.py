#!/usr/bin/python3

if __name__ == "__main__":
    """ This function prints all the names in a compiled pyc file  """
    import hidden_4

    all_names = dir(hidden_4)
    for all_name in all_names:
        if all_name[:2] != "__":
            print(all_name)
