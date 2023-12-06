import json

def load_data():
    try:
        with open('data.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_data(data):
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=2)

def add_employee():
    data = load_data()
    user = current_user()
    employee_name = input("Enter employee name: ")
    user['employees'].append(employee_name)
    save_data(data)
    print(f"Employee {employee_name} added successfully.")

def list_employees():
    data = load_data()
    user = current_user()
    print("\nList of Employees:")
    for employee in user['employees']:
        print(employee)

def add_department():
    data = load_data()
    user = current_user()
    department_name = input("Enter department name: ")
    user['departments'].append(department_name)
    save_data(data)
    print(f"Department {department_name} added successfully.")

def list_departments():
    data = load_data()
    user = current_user()
    print("\nList of Departments:")
    for department in user['departments']:
        print(department)

def current_user():
    users = load_data()
    username = input("Enter your username: ")
    return users.get(username)
