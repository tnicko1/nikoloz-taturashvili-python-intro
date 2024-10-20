from datetime import datetime

date = input("Enter the date in format YYYY-mm-ddTHH:MM:SS.ffffff+zz:zz\n")
try:
    date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f%z")
except ValueError:
    print("Invalid date format")
    exit(1)
date = date.strftime("%d/%m/%Y %H:%M %z")
print(date)