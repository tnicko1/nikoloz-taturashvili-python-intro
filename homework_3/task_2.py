import random

print("The program will display a random floating-point number")
maximum_value = int(input("Please input the maximum value (can be negative): "))
random_number = round(random.uniform(0, maximum_value), 1)

print(f"Random number: {random_number}")