def array_contains_value(arr, x):
    return x in arr

arr = [1, 2, 3, 4, 5]
x = 3
result = array_contains_value(arr, x)
print(result) 

arr = ["apple", "banana", "cherry"]
x = "pear"
result = array_contains_value(arr, x)
print(result) 