"""
Write a program that “guesses” an integer from 0 to 100.
The user must enter his or her guess of the number.
If the user’s guess matches the number the program guessed, print You are winner.
If the user’s guess is greater than the number the computer guessed, print high.
If the user’s guess is less than the number the computer guessed, print low.
The user has a maximum of 10 attempts.
If the user fails to guess the number in 10 attempts, print Computer is winner.
"""

from random import randint

random_number = randint(0, 100)
user_guess = int(input("Guess the number between 0 and 100: "))
attempts = 0

while user_guess != random_number and attempts < 10:
    if user_guess < random_number:
        print("Too low")
    else:
        print("Too high")
    user_guess = int(input("Guess again: "))
    attempts += 1

if user_guess == random_number:
    print("You guessed the number!")
else:
    print(f"Sorry, the number was {random_number}")