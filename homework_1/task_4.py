"""
Write a program that converts the temperature entered by the user in Celsius to Fahrenheit.
"""

print("Celsius to Fahrenheit calculator")
celsius_value = int(input("Temperature in Celsius: "))
fahrenheit_value = (celsius_value * 9 / 5) + 32
print("Temperature in Fahrenheit:",fahrenheit_value)