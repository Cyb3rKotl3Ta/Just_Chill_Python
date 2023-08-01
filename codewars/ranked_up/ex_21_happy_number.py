def is_happy_number(n, seen=set()):
    if n == 1:
        return True
    if n in seen:
        return False
    seen.add(n)
    return is_happy_number(sum(int(digit) ** 2 for digit in str(n)), seen)

def is_happy_number_v2(n):
    def get_next_number(num):
        # Calculate the sum of squares of digits of the number
        total = 0
        while num > 0:
            digit = num % 10
            total += digit ** 2
            num //= 10
        return total
    
    seen_numbers = set()
    while n != 1 and n not in seen_numbers:
        seen_numbers.add(n)
        n = get_next_number(n)
        
    return n == 1

# Test the function with some numbers
numbers_to_check = [19, 7, 82, 68, 100, 139]
for num in numbers_to_check:
    if is_happy_number(num):
        print(f"{num} is a happy number.")
    else:
        print(f"{num} is not a happy number.")