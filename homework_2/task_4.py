"""
Write a program that takes the speed of a car as an argument, determines its speed category, and prints it on the screen.
The speed categories are defined as follows.
If the car's speed is less than 30 km/h, its category is SLOW.
If the car's speed is more than 120 km/h, its category is VERY FAST.
If the car's speed is more than 60 km/h, its category is FAST.
Only if the car's speed is more than 30 km/h, its category is MODERATE.
(If the car falls into two categories, the faster category should be chosen.)
"""

speed = int(input("Please enter a speed of your vehicle(km/h) - "))

if speed > 120:
    print("Speed Category: Very Fast")
elif speed > 60:
    print("Speed Category: Fast")
elif speed > 30:
    print("Speed Category: Moderate")
elif speed > 0:
    print("Speed Category: Slow")
elif speed == 0:
    print("Your car is not moving")
else:
    print("Invalid Speed")