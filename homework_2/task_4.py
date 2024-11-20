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