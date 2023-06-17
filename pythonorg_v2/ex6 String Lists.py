

user = input("Enter to check palindrome:\n")

if user == user[::-1]:
    print('Is Palindrome')
if user != user[::-1]:
    print("Isn`t Palindrome")
