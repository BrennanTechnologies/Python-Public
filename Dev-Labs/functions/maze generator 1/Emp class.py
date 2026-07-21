class Employee:
    """A Sample Employee Class"""

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        print('Created Employee: {} - {}'.format(self.fullname, self.email))

    @property
    def email(self):
        return '{}.{}@company.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp1 = Employee('Corey', 'Schafer', 50000)
emp2 = Employee('Test', 'User', 60000)

# print(dir(emp1))
# print(dir(Employee))
