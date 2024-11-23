"""
(*) Write a program that accepts an integer - n, where 0 < n < 10.
The program should print the structure shown. Use while loop

1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
"""

n = int(input("Enter a number from 0 to 10: "))
if n < 0 or n > 10:
    print("Invalid input")
else:
    i = 1
    while i <= n:
        j = 1
        while j <= i:
            print(j, end=" ")
            j += 1
        print()
        i += 1

    i = n - 1
    while i > 0:
        j = 1
        while j <= i:
            print(j, end=" ")
            j += 1
        print()
        i -= 1