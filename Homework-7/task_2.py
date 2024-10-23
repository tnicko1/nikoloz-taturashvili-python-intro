user_input = input("Enter a string: ")
for i in range(len(user_input)):
    if user_input[i] in "aeiouAEIOU":
        continue
    print(user_input[i], end="")