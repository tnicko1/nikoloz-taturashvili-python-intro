"""
Write a program that generates 50 random numbers from 1 to 30 and writes them to a list.
The program should iterate over the list and for each element,
write that element into a new list as many times as its value.
Print the length of the new list and the list itself to the screen.
"""

from random import randint

def foo():
    numbers = []
    for _ in range(50):
        num = randint(1, 30)
        numbers.append(num)

    new_numbers = []
    for number in numbers:
        for i in range(number):
            new_numbers.append(number)

    print("List - ", new_numbers)
    print("Length - ", len(new_numbers))

foo()