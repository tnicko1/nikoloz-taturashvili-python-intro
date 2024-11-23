"""
Write a program that accepts the number of players.
The program should generate a pair of random dice for each player and print them on the screen.
For example:
Enter players number: 2
3 4
2 1
"""

from random import randint

player_number = int(input("How many players: "))
if player_number <= 0:
    print("Invalid player count")
    exit(1)

for i in range(player_number):
    random_dice_one = randint(1, 6)
    random_dice_two = randint(1, 6)

    print(random_dice_one, random_dice_two)