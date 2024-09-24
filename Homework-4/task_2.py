from random import randint

number_of_integers = int(input("Enter how many integers (max: 30): "))
if number_of_integers > 30 or number_of_integers < 1:
    print("Invalid number of integers")
    exit(1)

max_number = 0
for i in range(number_of_integers):
    random_number = randint(0, 1000)
    if random_number > max_number:
        max_number = random_number

print(f"Max number is {max_number}")