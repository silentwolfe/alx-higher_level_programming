def add_integer(a, b=98):
    # Check if a and b are integers or floats
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    # Cast a and b to integers if they are floats
    a = int(a)
    b = int(b)
    
    # Return the sum of a and b
    return a + b
