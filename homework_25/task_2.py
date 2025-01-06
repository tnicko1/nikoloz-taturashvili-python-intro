from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass


class Car(Vehicle):
    def move(self):
        print('The car is driving')

class Bike(Vehicle):
    def move(self):
        print('The bike is cycling')

class Truck(Vehicle):
    def move(self):
        print('The truck is hauling')


def test_vehicles(vehicles: list):
    for vehicle in vehicles:
        vehicle.move()

def main():
    car = Car()
    bike = Bike()
    truck = Truck()
    test_vehicles([car, bike, truck])


if __name__ == '__main__':
    main()