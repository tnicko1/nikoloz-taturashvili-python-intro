"""
(*) Write a program that accepts an integer - n, where 0 < n < 10.
The program should print the structure shown. Use while loop

          0
        1 0 1
      2 1 0 1 2
    3 2 1 0 1 2 3
  4 3 2 1 0 1 2 3 4
5 4 3 2 1 0 1 2 3 4 5
"""

n = int(input("Enter a number from 0 to 10: "))
if n < 0 or n > 10:
    print("Invalid input")
else:
    for i in range(n + 1):
        row = []
        for j in range(-i, i + 1):
            if j == 0:
                row.append('0')
            elif j < 0:
                row.append(str(-j))
            else:
                row.append(str(j))
        print(' '.join(row).center((2 * n + 1) * 2 - 1))
        # 2 * n + 1 is the number of columns in the longest row
        # I multiplied it by 2 and minus 1 to account for the space between the numbers