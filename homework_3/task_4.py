import random

random_color_index = random.randint(1, 4)

if random_color_index == 1:
    card_color = "Clubs"
elif random_color_index == 2:
    card_color = "Diamonds"
elif random_color_index == 3:
    card_color = "Hearts"
else:
    card_color = "Spades"

random_card_number = random.randint(2, 14)

if random_card_number == 11:
    card_number = "Jack"
elif random_card_number == 12:
    card_number = "Queen"
elif random_card_number == 13:
    card_number = "King"
elif random_card_number == 14:
    card_number = "Ace"
else:
    card_number = random_card_number

print(f"Random card is {card_number} of {card_color}")