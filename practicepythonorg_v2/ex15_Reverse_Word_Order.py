

def str_reverse1(string_to_reverse):
    string_to_reverse = string_to_reverse.split()[::-1]
    return print(" ".join(string_to_reverse))


str1 = "My name is Michele"
str_reverse1(str1)


