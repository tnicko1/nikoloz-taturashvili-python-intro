"""
Write a program that accepts an integer.
The program should print all the prime factors on a single line.
The maximum value of the prime factor should be 10.
Example: If we pass 6 to the program, the output should be 2, 3.
Explanation: 6 is divisible by both 2 and 3. 2 and 3 are prime numbers.
Protect the program from arguments that are not allowed.
"""

user_input = int(input("Enter a positive integer(max: 10) - "))

if user_input < 0 or user_input > 10:
    print("Number must be between 0 and 10.")
    exit(1)
elif user_input == 0:
    print("Every number is a divisor of 0")
    exit(1)

excluded_numbers = {0, 1, 4, 6, 8, 9, 10}
#I would make a separate "is_prime" function that determines if the number is prime
#,but we haven't learned it yet and since the maximum possible number is 10
#I simply excluded all possible wrong numbers using a set

prime_divisors = []

for i in range(1, user_input + 1):
    if user_input % i == 0 and i not in excluded_numbers:
        prime_divisors.append(i)
# we haven't learned loops yet
# but without it, I would have to write many if statements which is unpleasant

if prime_divisors:
    print(prime_divisors)
else:
    print("No prime divisors were found.")
