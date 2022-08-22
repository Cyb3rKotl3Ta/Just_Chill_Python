def is_in_lst(num, lst):
    if num in lst:
        print(f'Number {num} in list')
        return True
    else:
        print(f'Number {num} not in list')
        return False

#ORRRRRR binary search recursive

# Returns index of x in arr if present, else -1
def binary_search(lst, low, high, x):
    # Check base case
    if high >= low:
        mid = (high + low) // 2
        # If element is present at the middle itself
        if lst[mid] == x:
            return mid
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif lst[mid] > x:
            return binary_search(lst, low, mid - 1, x)
        # Else the element can only be present in right subarray
        else:
            return binary_search(lst, mid + 1, high, x)
    else:
        # Element is not present in the array
        return -1


list_to_search = range(1, 11)
print(binary_search(list_to_search, 0, 10, 1))
number = 200
print(is_in_lst(number, list_to_search))
