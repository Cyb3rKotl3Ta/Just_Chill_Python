# def top_3_words(text: str):
#     str_count = [i for i in text.split()]
#     # str_count.sort()
#     char_count = []
#     res = []
#     # char_count = [count.count(i) for i in count]
#     for i in str_count:
#         char_count.append(str_count.count(i))

#     adress = list(reversed(list(set(char_count))))
#     for i in range(3):
#         for j in range(len(char_count)):
#             if adress[i] == char_count[j]:
#                 res.append(str_count[j])
#                 break
#     print(adress)
#     print(char_count)
#     print(str_count)
#     return res


def top_3_words(text: str):
    exception_lst = list('''!"#$%&()*+,-./:;<=>?@[\]^_`{|}~''')
    print(exception_lst)
    for i in exception_lst:
        text = text.replace(i, ' ')
    if len(text.split()) == 0:
        return []
    counter = {}
    res = []
    for letter in text.split():
        if letter not in counter:
            counter[letter] = 0
        counter[letter] += 1
        a = list(reversed(sorted(counter.items(), key=lambda x:x[1])))
    print(a)
    if len(a) > 3:
        for i in range(3):
            if len(a[i][0]) <= 3:
                res.append(a[i][0])
    else:
        for i in range(len(a)):
            if len(a[i][0]) <= 3:
                res.append(a[i][0])
    return res

# exception_lst = '''!"#$%&()*+,-./:;<=>?@[\]^_`{|}~'''

# str_boba = "a a a  b  c c  d d d d  e e e e e c c ddd fly fly fly fly fly fly fly"
#str_boba = '''g g c bb 77#$%^8 6 b'b'''
str_boba = "  ...  "

print(top_3_words(str_boba))




