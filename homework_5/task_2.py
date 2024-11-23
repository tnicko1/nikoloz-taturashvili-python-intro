"""
Write a program that prints the multiplication table from 1 to 9 inclusive.
The table should be arranged in columns.
Each subsequent column should not repeat the product from the previous column.
Consider the example of 1x3
1 * 1 = 1
1 * 2 = 2 2 * 2 = 4
1 * 3 = 3 2 * 3 = 6 3 * 3 = 9
"""

row_number = 1

while row_number <= 9:
    for i in range(1, row_number + 1):
        print(f"{i} * {row_number} = {row_number * i}", end="  ")
    print()
    row_number += 1