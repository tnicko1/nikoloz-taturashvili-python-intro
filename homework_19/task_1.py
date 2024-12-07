"""
Write a program that reads a JSON file.
The program should handle an error if the file does not exist and print an informational message to the screen.
The program should calculate the average salary for each department for the departments in the file.
It should also handle potential errors.
The calculated average salaries should be printed to the screen and written to a JSON file avg_salary_input.json in the following format.
{
    "department_name": "<average_salary>",
    "department_name": "<average_salary>"
}
"""

import json

def read_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"File {file_path} does not exist.")
        return None
    except json.JSONDecodeError:
        print(f"Error decoding JSON from file {file_path}.")
        return None

def calculate_average_salaries(data):
    avg_salaries = {}
    for department, details in data.items():
        employees = details.get('employees', [])
        total_salary = 0
        count = 0
        for employee in employees:
            try:
                salary = float(employee['salary'])
                total_salary += salary
                count += 1
            except (ValueError, TypeError):
                print(f"Invalid salary for employee {employee['name']} in {department}. Skipping.")
        if count > 0:
            avg_salaries[details['name']] = total_salary / count
        else:
            avg_salaries[details['name']] = 0
    return avg_salaries

def write_json_file(file_path, data):
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    except IOError:
        print(f"Error writing to file {file_path}.")

def main():
    input_file = 'avg_salary_input.json'
    output_file = 'avg_salary.json'

    data = read_json_file(input_file)
    if data is not None:
        avg_salaries = calculate_average_salaries(data)
        print("Average Salaries:")
        for department, avg_salary in avg_salaries.items():
            print(f"{department}: {avg_salary:.2f}")
        write_json_file(output_file, avg_salaries)

if __name__ == "__main__":
    main()