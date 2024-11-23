"""
The program should prompt you to enter your name and year of birth.
The screen should say, Hello 'name', You are 'age' years old.
"""

name = input("Enter your name: ")
date_of_birth = int(input("Enter your date of birth: "))
print(f"Hello {name}, You are {2024 - date_of_birth} years old")