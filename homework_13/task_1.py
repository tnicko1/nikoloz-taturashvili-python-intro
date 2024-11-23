"""
Write a program that generates 100 random numbers from 10 to 1000000000.
The program should find the shortest number in the sequence, the longest number.
The program should sort the numbers by length in ascending, descending order.
Print the result on the screen.

Use the min, max, sorted functions
"""

from random import randint

numbers = [randint(10, 1000000000) for _ in range(100)]

shortest = min(numbers, key=lambda x: len(str(x)))
longest = max(numbers, key=lambda x: len(str(x)))

sorted_numbers = sorted(numbers, key=lambda x: len(str(x)), reverse=True) # remove reverse=True to sort in ascending order

print("Generated numbers sorted by length (descending):")
for num in sorted_numbers:
    print(f"{num} (length: {len(str(num))})")

print("\nSummary:")
print(f"Shortest number: {shortest} (length: {len(str(shortest))})")
print(f"Longest number: {longest} (length: {len(str(longest))})")