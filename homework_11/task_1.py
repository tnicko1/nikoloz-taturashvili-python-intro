"""
Write a function that can convert Celsius to Fahrenheit and vice versa.
C = (F - 32) * 5/9
F = C * 9/5 + 32

In the Main function, write some examples to demonstrate how the function you created works.
"""

def temperature_converter(temp, to):
    if to == "C":
        return (temp - 32) * 5 / 9
    elif to == "F":
        return temp * 9 / 5 + 32
    else:
        return "Invalid input"

print(temperature_converter(32, "C"))
print(temperature_converter(0, "C"))
print(temperature_converter(100, "C"))
print(temperature_converter(32, "F"))
print(temperature_converter(0, "F"))
print(temperature_converter(100, "F"))