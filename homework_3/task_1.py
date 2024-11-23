"""
Write a program that accepts two numbers (x,y) and prints the number obtained by raising x to the y power.
See module math
"""

from math import pow

print("X^Y")
x = int(input("Please input X: "))
print(f"{x}^Y")
y = int(input("Please input Y: "))
print(f"{x}^{y} = {pow(x, y)}")