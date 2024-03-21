#!/usr/bin/python3

def roman_to_int(roman_string):
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    prev_value = 0
    total = 0

   if not isinstance(roman_string, str) or roman_string is None:
       return 0

    for num in reversed(roman):
        value = roman_values[num]

        if value >= prev_value:
            total += value
            prev_value = value
        else:
            total -= value

    return total
