def read_numbers_from_file(file_path):
    numbers_set = set()
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            number = int(line.strip())
            numbers_set.add(number)
    return numbers_set

# Read prime numbers and happy numbers from their respective files
prime_numbers_set = read_numbers_from_file('practicepythonorg_v2/files_for_ex/ex23_prime_numbers.txt')
happy_numbers_set = read_numbers_from_file('practicepythonorg_v2/files_for_ex/ex23_happy_numbers.txt')

# Find the overlapping numbers
overlapping_numbers = prime_numbers_set.intersection(happy_numbers_set)

# Print the overlapping numbers
print("Overlapping numbers between prime and happy numbers:")
overlapping_numbers = sorted(list(overlapping_numbers))
for number in overlapping_numbers:
    print(number)