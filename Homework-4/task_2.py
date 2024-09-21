from random import randint

number_of_integers = int(input("Enter how many integers (max: 30): "))
if number_of_integers > 30 or number_of_integers < 1:
    print("Invalid number of integers")
    exit(1)

for i in range(number_of_integers):
    random_number = randint(0, 1000)
    print(f"Integer {i + 1}: {random_number}")