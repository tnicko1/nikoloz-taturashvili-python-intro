class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_info(self):
        return f"Name: {self._name}, Age: {self._age}"


def main():
    person = Person("John", 25)
    print(person.get_info())

    person2 = Person("Alice", 30)
    print(person2.get_info())

if __name__ == "__main__":
    main()