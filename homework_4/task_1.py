from random import randint

player_number = int(input("How many players: "))
if player_number <= 0:
    print("Invalid player count")
    exit(1)

for i in range(player_number):
    random_dice_one = randint(1, 6)
    random_dice_two = randint(1, 6)

    print(random_dice_one, random_dice_two)