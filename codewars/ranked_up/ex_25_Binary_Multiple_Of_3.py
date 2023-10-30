import re

def multiple_of_3(binary_string):
    pattern = r"^(0*(1(01*0)*10*)*)$"
    return re.match(pattern, binary_string) is not None


PATTERN = re.compile(r'^(0*(1(01*0)*10*)*)$')

# Example usage:
print(multiple_of_3('000'))  # True
print(multiple_of_3('001'))  # False
print(multiple_of_3('011'))  # True
print(multiple_of_3('110'))  # True
print(multiple_of_3(' abc '))  # False