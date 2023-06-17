def string_to_array(string):
    return string.split(" ")

def string_to_array2(s):
    arr = []
    
    words = s.split(" ")
    if len(s) == 0:
        return [""]
    
    for word in words:
        arr.append(word)
    
    return arr

string_to_array3=lambda s: s.split(" ")