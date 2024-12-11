import json
import os
from decimal import Decimal

class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = Decimal(salary)

class Department:
    def __init__(self, name, description, employees):
        self.name = name
        self.description = description
        self.employees = employees

    def average(self):
        if not self.employees:
            return 0
        total_salary = sum(emp.salary for emp in self.employees)
        return total_salary / len(self.employees)

    def max(self):
        if not self.employees:
            return None
        return max(emp.salary for emp in self.employees)

    def min(self):
        if not self.employees:
            return None
        return min(emp.salary for emp in self.employees)

    def positions(self):
        position_count = {}
        for emp in self.employees:
            position_count[emp.position] = position_count.get(emp.position, 0) + 1
        return position_count

def main():
    file_path = "departments.json"

    if not os.path.exists(file_path):
        print(f"Error: The file '{file_path}' does not exist.")
        return

    with open(file_path, "r") as file:
        data = json.load(file)

    departments = []
    for key, dept_data in data.items():
        employees = [Employee(emp["name"], emp["position"], emp["salary"]) for emp in dept_data["employees"]]
        department = Department(dept_data["name"], dept_data["description"], employees)
        departments.append(department)

    for department in departments:
        print(f"\nDepartment: {department.name}")
        print(f"Description: {department.description}")
        print(f"Average Salary: {department.average():.2f}")
        print(f"Maximum Salary: {department.max()}")
        print(f"Minimum Salary: {department.min()}")
        print("Positions:")
        for position, count in department.positions().items():
            print(f"  {position}: {count}")

if __name__ == "__main__":
    main()
