"""
Write a program that accepts a natural number n. n > 1
The program should generate n pairs of random numbers a,b, where 0<a<1 and 0<b<1.
Count the counter, if the generated number satisfies the condition math.sqrt(a ** 2 + b ** 2) <= 1,
increment the value of counter by 1.
Print 4 * counter / n on the screen.

Run the program and pass the following values: 10, 100, 100000, 10000000.
What do you notice?
"""

from random import random
from math import sqrt

n = int(input("Enter a number: "))

if n < 1:
    print("Number should be greater than 1")
else:
    counter = 0
    for _ in range(n):
        a = random()
        b = random()
        if sqrt(a ** 2 + b ** 2) <= 1:
            counter += 1

    # x = 10, 100, 1000, 10000 I notice that the result is getting closer to pi

    print(4 * counter / n)
