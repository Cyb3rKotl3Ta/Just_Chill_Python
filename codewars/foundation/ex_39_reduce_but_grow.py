from functools import reduce

def multiply_values_in_order(arr):
    return reduce(lambda x, y: x * y, arr)