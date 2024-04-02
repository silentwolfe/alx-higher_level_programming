def custom_len(my_list):
    i = 0
    for _ in my_list:
        i += 1
    return i


def safe_print_list(my_list=[], x=0):
    try:
        i = 0
        while (i < x):
            print(my_list[i], end="")
            i += 1
        print()
        return i
    except IndexError:
        if i < custom_len(my_list):
            print(my_list[i:], end="")
        print()
        return custom_len(my_list)

