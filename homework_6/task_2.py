"""
Write a program that accepts a positive integer - n. 0 < n <= 1000.
The program should print a sequence of numbers that are obtained under the following conditions:
if the number is even, we must divide this number by 2,
and if the number is odd, we must multiply this number by 3 and add 1, until we get 1.

Example:
Enter number: 10
10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
"""

user_input = int(input("Enter a number from 0 to 1000: "))

if user_input < 0 or user_input > 1000:
    print("Invalid input")
else:
    while user_input != 1:
        if user_input % 2 == 0:
            user_input = user_input // 2
        else:
            user_input = user_input * 3 + 1
        print(user_input, end=" -> ")