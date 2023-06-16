import json

class Employee:
    def __init__(self, name, dob, height, city, state):
        self.name = name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state

with open(r'C:\Users\rajes\OneDrive\Desktop\Final Project\Json\employee.json') as file:
    data = json.load(file)
employees = []

for employee_data in data['employees']:
    employee = Employee(employee_data['Name'], employee_data['DOB'], employee_data['Height'], employee_data['City'], employee_data['State'])
    employees.append(employee)

for employee in employees:
    print(f"Name: {employee.name}")
    print(f"DOB: {employee.dob}")
    print(f"Height: {employee.height}")
    print(f"City: {employee.city}")
    print(f"State: {employee.state}")
    print()
