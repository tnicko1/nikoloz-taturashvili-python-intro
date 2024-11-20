num = int(input("Enter a number (<20): "))

a, b = 0, 1
if num > 20:
    print("Invalid input")
    exit(1)
elif num <= 0:
    print("Please enter a positive integer")
else:
    for i in range(0, num):
        a, b = b, a + b
        if i == num - 1:
            suffix = "st" if num == 1 else "nd" if num == 2 else "rd" if num == 3 else "th"
            print(f"{num}{suffix} number in sequence is {a}")