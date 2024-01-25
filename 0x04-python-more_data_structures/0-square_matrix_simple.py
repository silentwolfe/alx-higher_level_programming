#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    def square(x): return x ** 2

    squared_value = map(lambda row: list(map(square, row)), matrix)
    result_value = list(squared_value)
    return result_value
