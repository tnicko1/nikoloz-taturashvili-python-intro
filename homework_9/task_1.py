n = int(input("Enter a number: "))

if n < 1:
    print("Number must be greater than 1")
else:
    x = 0
    for i in range(1, n + 1):
        x += ((-1) ** (i + 1)) / (2 * i - 1)
    x = 4 * x

    # x = 10, 100, 1000, 10000 I notice that the result is getting closer to pi

    print(x)