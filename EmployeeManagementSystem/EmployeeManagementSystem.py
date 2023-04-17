employees = []

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Salary:", self.salary)

def add_employee():
    name = input("Enter employee name: ")
    age = int(input("Enter employee age: "))
    salary = float(input("Enter employee salary: "))

    employee = Employee(name, age, salary)
    employees.append(employee)

def display_employees():
    for employee in employees:
        employee.display()
        print()

def search_employee(name):
    found = False
    for employee in employees:
        if employee.name.lower() == name.lower():
            employee.display()
            found = True
    if not found:
        print("Employee not found.")

while True:
    print("1. Add employee")
    print("2. Display employees")
    print("3. Search employee")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_employee()
    elif choice == 2:
        display_employees()
    elif choice == 3:
        name = input("Enter employee name to search: ")
        search_employee(name)
    elif choice == 4:
        break
    else:
        print("Invalid choice. Try again.")

