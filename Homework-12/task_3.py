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