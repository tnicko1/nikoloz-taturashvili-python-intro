def temperatureConverter(temp, to):
    if to == "C":
        return (temp - 32) * 5 / 9
    elif to == "F":
        return temp * 9 / 5 + 32
    else:
        return "Invalid input"

print(temperatureConverter(32, "C"))
print(temperatureConverter(0, "C"))
print(temperatureConverter(100, "C"))
print(temperatureConverter(32, "F"))
print(temperatureConverter(0, "F"))
print(temperatureConverter(100, "F"))