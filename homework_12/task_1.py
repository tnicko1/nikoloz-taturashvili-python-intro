def average_temperature(temperature_list):
    return sum(temperature_list) / len(temperature_list)

temperatures = [22, 25, 19, 23, 25, 26, 23]

print(average_temperature(temperatures))