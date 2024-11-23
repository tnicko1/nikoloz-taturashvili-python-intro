"""
Write a function that takes the car manufacturer and year of manufacture.
The car manufacturer should be a required argument and the default value for year of manufacture should be the current year.
The function should be able to take unspecified name and quantity configuration parameters.
Call the function several times with different arguments to demonstrate its operation.
"""

from datetime import datetime

def car_info(manufacturer, year=datetime.now().year, **kwargs):
    print(f"\nCar Information:")
    print(f"Manufacturer: {manufacturer}")
    print(f"Year: {year}")

    if kwargs:
        print("Additional Specifications:")
        for key, value in kwargs.items():
            print(f"{key}: {value}")


# Test
car_info("Toyota")

car_info("Honda", 2022)

car_info("BMW", color="Black", model="X5", engine="3.0L")

car_info("Mercedes", 2023, model="E-Class", color="Silver", seats=5, fuel_type="Hybrid")

car_info("Audi", transmission="Automatic", body_type="Sedan", hp=300)