"""
Write a program that evaluates to true or false. If the program evaluates to true, print “whoala” to the screen.
"""

user_value = input("Enter true or false - ").lower()

if user_value == "true":
    value = True
elif user_value == "false":
    value = False
else:
    print("Please enter true or false")
    exit(1)

if value:
    print("whoala")