user_input = int(input("Enter a number between 1 and 50: "))
if user_input < 1 or user_input > 50:
    print("Please enter a number between 1 and 50")
else:
    for num in range(1, user_input + 1):
        divisors = [1]
        for i in range(2, num + 1):
            if num % i == 0:
                divisors.append(i)
                if len(divisors) == 3:
                    break

        print(f"{num} - {divisors[0]}", end="")
        if len(divisors) > 1:
            print(f", {divisors[1]}", end="")
        if len(divisors) > 2:
            print(f", {divisors[2]}", end="")
        print()