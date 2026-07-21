import logging

# Using a custom logger:
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')

file_handler = logging.FileHandler('employee.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

# Using the root logger:
# logging.basicConfig(level=logging.DEBUG,
#                    format='%(asctime)s - %(funcName)s - %(levelname)s - %(message)s')


class Employee:
    """A Sample Employee Class"""

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        # print('Created Employee: {} - {}'.format(self.fullname, self.email))
        logger.info(
            'Created Employee: {} - {}'.format(self.fullname, self.email))

    @property
    def email(self):
        renamecount = 1
        # return '{}.{}@company1.com'.format(self.first, self.last)

    @email.setter
    def email(self, email):
        if email is None:
            self.first = None
            self.last = None
            return
        else:
            self.first, self.last = email.split('@')[0].split('.')
            # first, last = email.split('@')[0].split('.')
            # self.first = first
            # self.last = last
            return

    @email.getter
    def email(self):
        return '{}.{}@company.com'.format(self.first, self.last)

    @email.deleter
    def email(self):
        # self.first = None
        # self.last = None
        self.email = None

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last


emp1 = Employee('Corey', 'Schafer', 50000)
emp2 = Employee('Test', 'User', 60000)

# emp1.fullname = 'John Smith'
# emp1.email = 'chris.brennan@email.com'

# email deleter
del emp1.email


print(emp1.first)
print(emp1.last)
print(emp1.email)
print(emp1.fullname)


# print(dir(emp1))
# print(dir(Employee))
