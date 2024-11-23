"""
Write a program that accepts a natural number - n , where 0 < n < 50 .
The program should find the divisors of all numbers up to n.
Print a maximum of 3 divisors.
Example:
The program accepts took number 12
 1 – 1
 2 – 1 2
 3 – 1 3
 4 – 1 2 4
 5 – 1 5
 6 – 1 2 3
 7 – 1 7
 8 – 1 2 4
 9 – 1 3 9
 10 – 1 2 5
 11 – 1 11
 12 – 1 2 3
"""

user_input = int(input("Enter a number between 1 and 50: "))
if user_input < 1 or user_input > 50:
    print("Please enter a number between 1 and 50")
else:
    for num in range(1, user_input + 1):
        divisors = [1]
        for i in range(2, num + 1):
            if num % i == 0:
                divisors.append(i)
                if len(divisors) == 3:
                    break

        print(f"{num} - {divisors[0]}", end="")
        if len(divisors) > 1:
            print(f", {divisors[1]}", end="")
        if len(divisors) > 2:
            print(f", {divisors[2]}", end="")
        print()