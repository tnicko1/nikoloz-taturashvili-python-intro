user_input = int(input("Enter a number from 0 to 1000: "))

if user_input < 0 or user_input > 1000:
    print("Invalid input")
else:
    while user_input != 1:
        if user_input % 2 == 0:
            user_input = user_input // 2
        else:
            user_input = user_input * 3 + 1
        print(user_input, end=" -> ")