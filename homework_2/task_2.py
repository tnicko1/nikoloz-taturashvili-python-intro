"""
Write a program that takes two numbers, determines whether the first number is a multiple of the second number, and prints it to the screen.
"""

#I wanted to add input validation as well, but it seems too advanced for now
#So I will assume that user correctly enters the integer value
number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))

if number_1 == 0 or number_2 == 0:
    print("Neither number can be zero")
    exit(1)

if number_1 % number_2 == 0:
    print(f"{number_1} is multiple of {number_2}")
else:
    print(f"{number_1} is not multiple of {number_2}")