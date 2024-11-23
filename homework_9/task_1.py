"""
Write a program that accepts a natural number n. n > 1
The program should calculate the number x and print it on the screen.
The principle of calculating the number x is as follows.
x = 4 * (1 - 1/3 + 1/5 - 1/7 + 1/9 - ... (+/-)1 / (2n-1))

Run the program and pass the following values: 10, 100, 10000, 100000.
What do you notice?
"""

n = int(input("Enter a number: "))

if n < 1:
    print("Number must be greater than 1")
else:
    x = 0
    for i in range(1, n + 1):
        x += ((-1) ** (i + 1)) / (2 * i - 1)
    x = 4 * x

    # x = 10, 100, 1000, 10000 I notice that the result is getting closer to pi

    print(x)