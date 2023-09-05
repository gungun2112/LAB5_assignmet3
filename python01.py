class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeDatabase:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def search_by_age(self, age):
        result = []
        for employee in self.employees:
            if employee.age == age:
                result.append(employee)
        return result

    def search_by_name(self, name):
        result = []
        for employee in self.employees:
            if employee.name == name:
                result.append(employee)
        return result

    def search_by_salary(self, operator, salary):
        result = []
        for employee in self.employees:
            if operator == '>' and employee.salary > salary:
                result.append(employee)
            elif operator == '<' and employee.salary < salary:
                result.append(employee)
            elif operator == '>=' and employee.salary >= salary:
                result.append(employee)
            elif operator == '<=' and employee.salary <= salary:
                result.append(employee)
        return result

    def print_results(self, results):
        if not results:
            print("No matching records found.")
        else:
            for employee in results:
                print(f"Employee ID: {employee.emp_id}, Name: {employee.name}, Age: {employee.age}, Salary: {employee.salary}")

def main():
    database = EmployeeDatabase()

    # Populate the employee database with sample data
    database.add_employee(Employee("161E90", "Raman", 41, 56000))
    database.add_employee(Employee("161F91", "Himadri", 38, 67500))
    database.add_employee(Employee("161F99", "Jaya", 51, 82100))
    database.add_employee(Employee("171E20", "Tejas", 30, 55000))
    database.add_employee(Employee("171G30", "Ajay", 45, 44000))

    print("Choose a search parameter:")
    print("1. Age")
    print("2. Name")
    print("3. Salary (>, <, <=, >=)")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        age = int(input("Enter the age to search: "))
        results = database.search_by_age(age)
    elif choice == 2:
        name = input("Enter the name to search: ")
        results = database.search_by_name(name)
    elif choice == 3:
        operator = input("Enter the operator (> < <= >=): ")
        salary = int(input("Enter the salary to compare: "))
        results = database.search_by_salary(operator, salary)
    else:
        print("Invalid choice")
        return

    database.print_results(results)

if __name__ == "__main__":
    main()
