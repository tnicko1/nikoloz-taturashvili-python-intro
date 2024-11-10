temperature_tup_by_day = ((33, 34, 28), (24, 31, 27), (24, 23, 27), (28, 32, 34), (33, 21, 28), (20, 25, 31), (21, 31, 28))

def format_temp_tup(temp_by_day_tup):
    formatted_temp_tup = ()
    for i in temp_by_day_tup:
        formatted_temp_tup += ((float(f"{sum(i) / len(i):.1f}"), max(i), min(i)),)
    return formatted_temp_tup


def average_temperature_in_week(formatted_temp_tup):
    average_temp = 0
    for i in formatted_temp_tup:
        average_temp += i[0]

    average_temp /= len(formatted_temp_tup)
    return float(f"{average_temp:.1f}")


def display_weekly_weather():
    formatted_temp_tup = format_temp_tup(temperature_tup_by_day)
    average_temp = average_temperature_in_week(formatted_temp_tup)
    print(f"Average temperature for the week: {average_temp}")
    for i in range(len(temperature_tup_by_day)):
        print(f"Day {i + 1} -- Avg: {formatted_temp_tup[i][0]} | Max: {formatted_temp_tup[i][1]} | Min: {formatted_temp_tup[i][2]}")


display_weekly_weather()