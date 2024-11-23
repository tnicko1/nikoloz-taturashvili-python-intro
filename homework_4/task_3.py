"""
Write a program that accepts a positive integer.
The program should find and print on the screen all the divisors of this number in one line.
0 < n < 1000.
For example: Enter number: 18
1 2 3 6 9 18
"""

num = int(input("Enter a number (<1000): "))
if abs(num) > 1000: #I'm allowing negative numbers as well
    print("Invalid number")
    exit(1)
elif num == 0:
    print("Every number is a divisor of 0")
elif num < 0:
    numbers = []
    print("\nEvery divisor of the given number:")
    for i in range(1, abs(num) + 1):
        if num % i == 0:
            numbers.append(i)
            numbers.append(-i) #Program will print negative divisors too only for negative input
    numbers.sort()
    for number in numbers:
        print(number, end=" ")
else:
    print("\nEvery divisor of the given number:")
    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end=" ")