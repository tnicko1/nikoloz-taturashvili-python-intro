import datetime

birth_year = int(input("Enter your birth year: "))
birth_month = int(input("Enter your birth month in numbers (e.g. '8' for August): "))
birth_day = int(input("Enter your birth day: "))

birth_date = datetime.date(birth_year, birth_month, birth_day)

week_day = birth_date.strftime("%A")

print(f"The day of the week you're born in is: {week_day}")