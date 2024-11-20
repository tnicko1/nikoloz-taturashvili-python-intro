n = int(input("Enter a number (0 < n < 50): "))
if n <= 0 or n > 50:
    print("Please enter a number between 1 and 50")
else:
    row_count = 1

    print(f"{" " * n}*")
    while row_count <= n:
        if row_count != n:
            print(f"{" " * (n - row_count)}{"/" * row_count}|{"\\" * row_count}")
            row_count += 1
        else:
            print(f"{" " * n}|")
            break