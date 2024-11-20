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
