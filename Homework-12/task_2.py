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