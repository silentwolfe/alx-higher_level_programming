#!/usr/bin/python3

if __name__ == "__main__":
    """ This function imports the add_0 function using the import module """
    from add_0 import add
    """ Now initialize variable for the add function """

    a = 1
    b = 2

    result = add(a, b)

    """ 
    Have a print statement that would print out
    the value of 'a' and 'b' using the add function
    """

    print("{:d} + {:d} = {:d}".format(a, b, result))
