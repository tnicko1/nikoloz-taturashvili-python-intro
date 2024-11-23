"""
Write a program that generates a non-integer random number and rounds it to the nearest tenth.
Print the result on the screen. Choose the rounding function of your choice. See module math
"""

import random

print("The program will display a random floating-point number")
maximum_value = int(input("Please input the maximum value (can be negative): "))
random_number = round(random.uniform(0, maximum_value), 1)

print(f"Random number: {random_number}")