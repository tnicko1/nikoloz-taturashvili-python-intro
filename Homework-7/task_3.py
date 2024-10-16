user_input = input("Enter a string: ")

length = len(user_input)
index = 0
first_char = ""
last_char = ""
middle_chars = ""

while index < length:
    if index == 0:
        first_char = user_input[index]
    elif index == length - 1:
        last_char = user_input[index]

    if length % 2 == 0:  # Even length
        if index == length // 2 - 1 or index == length // 2:
            middle_chars += user_input[index]
    else:  # Odd length
        if index == length // 2:
            middle_chars = user_input[index]

    index += 1

print(f"First character: {first_char}")
print(f"Last character: {last_char}")
print(f"Middle character(s): {middle_chars}")