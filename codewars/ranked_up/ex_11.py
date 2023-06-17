import numpy as np
def snail(snail_map):
    return list(np.array(snail_map).flatten())

def snail1(snail_map):
    return list(np.array(snail_map).reshape(len(snail_map)*len(snail_map[0]),1))

def snail2(sequence):
    return [[i for i in sequence] for j in sequence]

def snail3(snail_map):
    return list(np.array(snail_map).ravel())

ini_array1 = [[1, 2, 3], 
              [2, 4, 5], 
              [1, 2, 3]]

def snail4(snail_map):
    list_of_numbers = []

    while snail_map:
        for i in snail_map[0]:
            list_of_numbers.append(i)
        snail_map.pop(0)
        
        if not snail_map:
            break
                    
        for j in snail_map:
            list_of_numbers.append(j[-1])
            j.pop()
        for k in range(len(snail_map[-1]) -1, -1, -1):
            list_of_numbers.append(snail_map[-1][k])
        snail_map.pop()
        if not snail_map:
            break
        for l in reversed(snail_map):
            list_of_numbers.append((l[0]))
            l.pop(0)
        
    return list_of_numbers

def snail5(array):
    m = []
    array = np.array(array)
    while len(array) > 0:
        m += array[0].tolist()
        array = np.rot90(array[1:])
    return m

print(snail5(ini_array1))









# import numpy as np
 
# ini_array1 = np.array([[1, 2, 3], [2, 4, 5], [1, 2, 3]])
 
# # printing initial arrays
# print("initial array", str(ini_array1))
 
# # Multiplying arrays
# result = ini_array1.ravel()
 
# # printing result
# print("New resulting array: ", result)