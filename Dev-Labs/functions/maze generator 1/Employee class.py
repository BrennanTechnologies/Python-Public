class Employee:
    raise_amount = 1.04  # Class variable

    def __init__(self, name, age, gender, employee_id, department):
        self.name = name  # Instance variable
        self.age = age
        self.gender = gender
        self.employee_id = employee_id
        self.department = department
        self.salary = 0

    def give_raise(self, amount):
        self.salary += amount

    def print_me(self):
        print("Name: " + self.name + "\tDept: " + self.department)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):

    raise_amount = 1.10  # Class variable

    def __init__(self, name, age, gender, employee_id, department, programming_language):
        # super().__init__(name, age, gender, employee_id, department) # same as below  # super() is used to call the parent class

        # same as above # Employee is the parent class
        Employee.__init__(self, name, age, gender, employee_id, department)

        self.programming_language = programming_language    # Instance variable

    def print_me(self):
        print(str(super().print_me()) +
              "Language: " + self.programming_language)
        # print("Name: " + self.name + "\tDept: " + self.department +
        #      "\t\tLanguage: " + self.programming_language)


class Manager(Employee):

    raise_amount = 1.50  # Class variable

    def __init__(self, name, age, gender, employee_id, department, direct_reports=None):
        # super() is used to call the parent class
        super().__init__(name, age, gender, employee_id, department)

        if direct_reports is None:
            self.direct_reports = []  # direct_reports if direct_reports is None else direct_reports
        else:
            self.direct_reports = direct_reports

    def add_report(self, employee):
        self.direct_reports.append(employee)

    def remove_report(self, employee):
        self.direct_reports.remove(employee)

    def print_reports(self):
        if len(self.direct_reports) > 0:
            print("Direct Reports:")
            for employee in self.direct_reports:
                print("\t" + employee.name)
        else:
            print("No direct reports")

    def give_raise(self, amount):
        self.salary += amount * 1.1

    def print_me(self):
        print(str(super().print_me()) +
              "Direct Reports: " + str(self.direct_reports))


# print(help('modules'))  # shows all the modules that are available to import
help('modules')
breakpoint()

employee1 = Employee("Alice", 30, "Female", "12345", "Employee")
# print(Employee)  # <class '__main__.Employee'>
# print(employee1.name)  # "Alice"

# developer1 = Developer("Waldo", 30, "Male", "13364", "Developer", "Python")
# print(help(developer1))  # <__main__.Developer object at 0x0000020F1F6F4F70>
# print(developer1.name)  # "Ralph"
# print(developer1.print_me())  # "Ralph"


manager1 = Manager("Chico", 30, "Male", "133264", "Manager")
# print(help(developer1))  # <__main__.Developer object at 0x0000020F1F6F4F70>
# print("Name: " + manager1.name)  # "Ralph"
print(manager1.print_me())  # "Ralph"
print(manager1.print_reports())
manager1.add_report(employee1)
print(manager1.print_reports())

print(help(manager1))

'''
breakpoint()

print(employee1.name)  # "Alice"
print(employee1.age)  # 30
print(employee1.gender)  # "Female"
print(employee1.employee_id)  # "12345"
print(employee1.department)  # "Marketing"
print(employee1.salary)  # 0

employee1.give_raise(10000)
print(employee1.salary)  # 10000

manager1 = Manager("Bob", 40, "Male", "54321", "Sales")
print(manager1.name)  # "Bob"
print(manager1.age)  # 40
print(manager1.gender)  # "Male"
print(manager1.employee_id)  # "54321"
print(manager1.department)  # "Sales"
print(manager1.salary)  # 0
print(manager1.direct_reports)  # []

employee2 = Employee("Charlie", 25, "Male", "67890", "Sales")
manager1.add_report(employee2)
print(manager1.direct_reports)  # [employee2]

'''
