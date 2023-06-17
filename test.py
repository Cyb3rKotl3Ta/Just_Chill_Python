import random

# number1 = str(random.randint(1000,9999))
# number2 = str(random.randint(1000,9999))
# number1 = [1,1,1,1]
# number2 = [1,1,1,1]
# for i in range(len(number1)):
#     if number1[i] == number2[i]:                          
#         #print(number1[i])
#         #print(number2[i])
#         pass


# s1 = '4321'
# s2 = '3355'

# for i in range(4):
#     # print(s1[i], s2[i], s1[i]==s2[i])
#     if s1[i] == s2[i]:
#         print("True")
#     if s1[i] != s2[i]:
#         print("False")

# cow = 0
# bull = 0

# password1, password2 = [i for i in s1],[i for i in s2]
# print(type(password1))
# bull += [password1[i] for i in password1 if password1[i] == password1[2]]
# print(bull)


# password1, password2 = [],[]
# for i in range(len(s1)):
#     password1.append(s1[i])
#     password2.append(s2[i])
# for i in range(len(password1)):
#     if password1[i] == password2[i]:
#         cow += 1
#     bull += password1.count(password2[i])



# print(password1)
# print(password2)
# print(cow)
# print(bull)

import math

# num = int(input())
num = -1
def is_square(num):
    if num < 0:
        num *= -1
    sqrt_num = math.sqrt(num)
    if sqrt_num % 1 == 0:
        return True
    else:
        return False

a = is_square(num)
print(a)