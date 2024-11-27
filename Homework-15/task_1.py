from random import randint

numbers = [randint(1, 100) for _ in range(100)]

even = []
odd = []

for i in numbers:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

my_dict = {'Even numbers': len(even), 'Odd numbers': len(odd)}
print(my_dict)