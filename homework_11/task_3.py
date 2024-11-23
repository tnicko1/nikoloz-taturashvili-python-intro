"""
Write a program that accepts two integers a and b, where 0 < a , b < 10000,
and prints the least common multiple of these two numbers.

The notation is lcm(a, b) = (a * b) / gcd(a, b).
Import and use the greatest common divisor calculation functionality from the first task file.
"""

from task_2 import highest_common_factor

def lowest_common_multiple(a, b):
    return a * b // highest_common_factor(a, b)

a = int(input("Enter a: "))
b = int(input("Enter b: "))
print("LCM: ", lowest_common_multiple(a, b))