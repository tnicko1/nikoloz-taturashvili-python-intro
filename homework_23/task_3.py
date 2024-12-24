class Student:
    def __init__(self, name):
        self._name = name
        self._scores = []

    def add_score(self, score):
        if 0 <= score <= 100:
            self._scores.append(score)
        else:
            print("Invalid score")

    def get_average(self):
        if not self._scores:
            return 0
        return sum(self._scores) / len(self._scores)

    def get_scores(self):
        return self._scores


def main():
    student = Student("John")
    student.add_score(90)
    student.add_score(85)
    student.add_score(95)
    print(student.get_scores())
    print(student.get_average())

    student2 = Student("Alice")
    student2.add_score(80)
    student2.add_score(75)
    student2.add_score(85)
    print(student2.get_scores())
    print(student2.get_average())

if __name__ == "__main__":
    main()