import numpy as np

def sort_odd_numbers(arr):
    odd_numbers = sorted([num for num in arr if num % 2 != 0])

    sorted_arr = []
    odd_index = 0
    for num in arr:
        if num % 2 != 0:
            sorted_arr.append(odd_numbers[odd_index])
            odd_index += 1
        else:
            sorted_arr.append(num)

    return sorted_arr


def sort_odd_numbers_v2(arr):
    odd_numbers = sorted(num for num in arr if num % 2)
    return [odd_numbers.pop(0) if num % 2 else num for num in arr]