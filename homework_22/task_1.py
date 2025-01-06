class InSet:
    def __init__(self):
        self.list = list()

    def insert(self, item):
        if item not in self.list:
            self.list.append(item)
        else:
            raise ValueError(f"{item} is already in the set")

    def remove(self, item):
        if item in self.list:
            self.list.remove(item)
        else:
            raise ValueError(f"{item} is not in the set")

    # changed the name from "member" to "is_member" to better reflect the naming convention
    def is_member(self, item):
        return item in self.list

    def __str__(self):
        self.list.sort()
        return str(self.list)


def main():
    s = InSet()
    s.insert(5)
    s.insert(4)
    s.insert(3)
    print(s)
    s.remove(4)
    print(s)
    print(s.is_member('mango'))
    print(s.is_member(5))


if __name__ == '__main__':
    main()