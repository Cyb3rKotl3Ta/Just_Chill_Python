import random
import string


def rand_password(S: int):
    ran = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=S))
    return print("The randomly generated string is : " + str(ran))

word = input("Enter \"+\" to generate password\n")

while word == "+":
    str_length = 10
    rand_password(str_length)
    word = input("Enter \"+\" to generate password or \"-\" to close \n")
    if word == "-":
        break
