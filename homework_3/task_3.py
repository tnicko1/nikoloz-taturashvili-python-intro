"""
Write a program that takes 3 values: the year a person was born, the month they were born in, and the day they were born.
Then it prints the day of the week the person was born on.
See module datetime
"""

import datetime

birth_year = int(input("Enter your birth year: "))
birth_month = int(input("Enter your birth month in numbers (e.g. '8' for August): "))
birth_day = int(input("Enter your birth day: "))

birth_date = datetime.date(birth_year, birth_month, birth_day)

week_day = birth_date.strftime("%A")

print(f"The day of the week you're born in is: {week_day}")