number = int(input("Enter a number (10 <= number <= 5432):"))

if number <= 10 or number >= 5432:
    print("Program received an incorrect input. Number must be between 10 and 5432")
    exit(1)
else:
    numbers = []
    for i in range(1, number):
        if i % 13 == 0:
            numbers.append(i)

    print("All numbers that fit the description")
    print(numbers)
    print("Number of elements:", len(numbers))