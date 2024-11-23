"""
Write a program that accepts a date.
The program should convert the date to a different format and print it on the screen.
See the examples for the input and output date formats.

Example 1:
Input: 2024-03-22T19:17:42.956376+00:00
Output: 22-03-2024 7:17:42 +0

Example 2:
Input: 2024-03-04T11:17:42.000123+04:00
Output: 04-03-2024 11:17:42 +4

Example 3:
Input: 2024-11-14T15:17:42.123000-03:00
Output: 14-11-2024 3:17:42 -3
"""

from datetime import datetime

date = input("Enter the date in format YYYY-mm-ddTHH:MM:SS.ffffff+zz:zz\n")
try:
    date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f%z")
except ValueError:
    print("Invalid date format")
    exit(1)
date = date.strftime("%d/%m/%Y %H:%M %z")
print(date)