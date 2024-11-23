"""
Write a program that generates 50 random numbers from 1 to 30 and writes them to a list.
The program should iterate over the list and remove all duplicates.
Print the length of the new list and the list itself to the screen.
"""

from random import randint

def foo():
    numbers = []
    for _ in range(50):
        num = randint(1, 30)
        numbers.append(num)
    # remove all duplicates from the list
    new_numbers = []
    for number in numbers:
        if number not in new_numbers:
            new_numbers.append(number)

    print("List - ", new_numbers)
    print("Length - ", len(new_numbers))

foo()