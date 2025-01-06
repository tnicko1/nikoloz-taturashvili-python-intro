from abc import ABC, abstractmethod


class Appliance(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class WashingMachine(Appliance):
    def turn_on(self):
        print('Washing machine is turned on')

    def turn_off(self):
        print('Washing machine is turned off')


class Refrigerator(Appliance):
    def turn_on(self):
        print('Refrigerator is turned on')

    def turn_off(self):
        print('Refrigerator is turned off')


def operate_appliance(appliance):
    appliance.turn_on()
    appliance.turn_off()


def main():
    washing_machine = WashingMachine()
    refrigerator = Refrigerator()
    operate_appliance(washing_machine)
    operate_appliance(refrigerator)


if __name__ == '__main__':
    main()