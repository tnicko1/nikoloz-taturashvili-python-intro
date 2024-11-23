"""
(*) Write a program that accepts a non-negative integer - n.
0 <= n < 20.
The program must find the nth term of a sequence.
A sequence is defined as follows: the zero term is 0, the first term is 1, and each subsequent term is the sum of the previous two terms.
For example:
Enter number: 4
3
"""

num = int(input("Enter a number (<20): "))

a, b = 0, 1
if num > 20:
    print("Invalid input")
    exit(1)
elif num <= 0:
    print("Please enter a positive integer")
else:
    for i in range(0, num):
        a, b = b, a + b
        if i == num - 1:
            suffix = "st" if num == 1 else "nd" if num == 2 else "rd" if num == 3 else "th"
            print(f"{num}{suffix} number in sequence is {a}")