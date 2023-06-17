arr1 = []
arr2 = ["Peter"]
arr3 = ["Jacob", "Alex"]
arr4 = ["Max", "John", "Mark"]
arr5 = ["Alex", "Jacob", "Mark", "Max"]

names = []

def name_returnall(names_lst):
    len_lst = len(names_lst)
    if len_lst == 0:
        return "no one likes this"
    elif len_lst == 1:
        return f"{names_lst[0]} likes this"
    elif len_lst == 2:
        return f"{names_lst[0]} and {names_lst[1]} like this"
    elif len_lst == 3:
        return f"{names_lst[0]}, {names_lst[1]} and {names_lst[2]} like this"
    else:
        return f"{names_lst[0]}, {names_lst[1]} and {len_lst - 2} others like this"
    
def likes1(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this', 
        2: '{} and {} like this', 
        3: '{}, {} and {} like this', 
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)

def likes2(names):
    # make a dictionary d of all the possible answers. Keys are the respective number
    # of people who liked it.
    
    # {} indicate placeholders. They do not need any numbers but are simply replaced/formatted
    # in the order the arguments in names are given to format
    # {others} can be replaced by its name; below the argument "others = length - 2"
    # is passed to str.format()
    d = {
        0: "no one likes this",
        1: "{} likes this",
        2: "{} and {} like this",
        3: "{}, {} and {} like this",
        4: "{}, {} and {others} others like this"
        }
    length = len(names)
    # d[min(4, length)] insures that the appropriate string is called from the dictionary
    # and subsequently returned. Min is necessary as len(names) may be > 4
    
    # The * in *names ensures that the list names is blown up and that format is called
    # as if each item in names was passed to format individually, i. e.
    # format(names[0], names[1], .... , names[n], others = length - 2
    return d[min(4, length)].format(*names, others = length - 2)

def likes3(names):
    match names:
        case []: return 'no one likes this'
        case [a]: return f'{a} likes this'
        case [a, b]: return f'{a} and {b} like this'
        case [a, b, c]: return f'{a}, {b} and {c} like this'
        case [a, b, *rest]: return f'{a}, {b} and {len(rest)} others like this'

print(name_returnall(arr1))
print(likes1(arr2))
print(likes2(arr3))
print(likes3(arr4))
print(name_returnall(arr5))
