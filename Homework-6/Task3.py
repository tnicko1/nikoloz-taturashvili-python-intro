number = int(input("Enter a number from 0 to 10000: "))

if number < 0 or number > 10000:
    print("Invalid input")
else:
    reversed_number = 0
    digits = 0
    _sum = 0

    while number != 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number = number // 10
        digits += 1
        _sum += digit

    print(f"Reversed number: {reversed_number}")
    print(f"Number of digits: {digits}")
    print(f"Sum of digits: {_sum}")