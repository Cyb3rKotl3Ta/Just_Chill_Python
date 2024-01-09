def dir_reduc_v1(arr):
    if len(arr) == 0:
        return arr
    
    i = 0
    while i < len(arr) - 1:
        if arr[i] == 'NORTH' and 'SOUTH' in arr[i+1:]:
            arr.pop(i)
            arr.pop(arr.index('SOUTH', i+1))
        elif arr[i] == 'SOUTH' and 'NORTH' in arr[i+1:]:
            arr.pop(i)
            arr.pop(arr.index('NORTH', i+1))
        elif arr[i] == 'EAST' and 'WEST' in arr[i+1:]:
            arr.pop(i)
            arr.pop(arr.index('WEST', i+1))
        elif arr[i] == 'WEST' and 'EAST' in arr[i+1:]:
            arr.pop(i)
            arr.pop(arr.index('EAST', i+1))
        else:
            i += 1

    return arr


def dir_reduc_v2(arr):
    opposites = {'NORTH': 'SOUTH', 'SOUTH': 'NORTH', 'EAST': 'WEST', 'WEST': 'EAST'}
    stack = []

    for direction in arr:
        if stack and stack[-1] == opposites[direction]:
            stack.pop()
        else:
            stack.append(direction)

    return stack

def dir_reduc_v3(arr):
    dir = " ".join(arr)
    dir2 = dir.replace("NORTH SOUTH",'').replace("SOUTH NORTH",'').replace("EAST WEST",'').replace("WEST EAST",'')
    dir3 = dir2.split()
    return dir_reduc_v3(dir3) if len(dir3) < len(arr) else dir3

a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
print(dir_reduc_v2(a))




a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
print(dir_reduc_v1(a))
