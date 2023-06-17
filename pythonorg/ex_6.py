


def is_palindrome(string: str):
    reversed_string = string[::-1]
    return string == reversed_string


print(is_palindrome('TACOCAT')) # True
print(is_palindrome('TURBO')) # False
