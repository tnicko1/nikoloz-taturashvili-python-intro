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