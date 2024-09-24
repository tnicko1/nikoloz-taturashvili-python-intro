row_number = 1

while row_number <= 9:
    for i in range(1, row_number + 1):
        print(f"{i} * {row_number} = {row_number * i}", end="  ")
    print()
    row_number += 1