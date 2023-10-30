def same_structure_as(arr1, arr2):
    if isinstance(arr1, list) and isinstance(arr2, list) and len(arr1) == len(arr2):
        return all(same_structure_as(subarr1, subarr2) for subarr1, subarr2 in zip(arr1, arr2))
    elif not isinstance(arr1, list) and not isinstance(arr2, list):
        return True
    return False

# Example usage:
print(same_structure_as([1, 1, 1], [2, 2, 2]))  # True
print(same_structure_as([1, [1, 1]], [2, [2, 2]]))  # True
print(same_structure_as([1, [1, 1]], [[2, 2], 2]))  # False
print(same_structure_as([1, [1, 1]], [[2], 2]))  # False
print(same_structure_as([[[ ], [ ]]], [[[ ], [ ]]]))  # True
print(same_structure_as([[[ ], [ ]]], [[1, 1]]))  # False