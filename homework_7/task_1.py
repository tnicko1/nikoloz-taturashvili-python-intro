user_input = input("Enter a string: ")

for i in range(len(user_input)):
    if i % 2 == 0:
        if user_input[i] == 'e':
            continue
        print(user_input[i], end="")