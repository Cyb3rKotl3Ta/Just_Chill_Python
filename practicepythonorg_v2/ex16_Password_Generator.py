import string
import random


def password_generator(choice):
    strong_string_to_password = list(string.ascii_letters\
                              + string.digits\
                              + string.punctuation)
    if choice == 1:
        return ''.join(random.sample(strong_string_to_password, 18))
    elif choice == 2:
        return ''.join(random.sample(string.digits, 4))


user_input = int(input('1 - strong password\n2 - weak password\n'))

print(password_generator(user_input))
