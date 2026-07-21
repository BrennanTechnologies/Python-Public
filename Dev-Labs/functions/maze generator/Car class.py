# This file contains the Car class, which inherits from the Vehicle class.

# The Vehicle class is the parent class (or superclass) of the Car class.
class Vehicle:  # Parent class (superclass)
    def __init__(self, make, model, year):  # Constructor
        self.make = make
        self.model = model
        self.year = year
        self.gas = 0

    # Method: add_gas
    def add_gas(self, amount):  # Method
        self.gas += amount


class Car(Vehicle):  # Child class (subclass)
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.wheels = 4

    def drive(self):
        if self.gas > 0:
            print("Driving...")
            self.gas -= 1
        else:
            print("Out of gas!")


class Bicycle(Vehicle):
    pass


class Bus(Vehicle):
    pass


class Truck(Vehicle):
    pass


####################
my_car = Car("Toyota", "Corolla", 2022)
print(my_car.make)  # "Toyota"
print(my_car.model)  # "Corolla"
print(my_car.year)  # 2022
print(my_car.wheels)  # 4

my_car.add_gas(10)
print(my_car.gas)  # 10

my_car.drive()  # "Driving..."
print(my_car.gas)  # 9

my_car.drive()  # "Driving..."
print(my_car.gas)  # 8

my_car.drive()  # "Driving..."
print(my_car.gas)  # 7

my_car.add_gas(5)
print(my_car.gas)  # 12

my_car.drive()  # "Driving..."
print(my_car.gas)  # 11

my_car.drive()  # "Driving..."
print(my_car.gas)  # 10

my_car.drive()  # "Driving..."
print(my_car.gas)  # 9

my_car.drive()  # "Driving..."
print(my_car.gas)  # 8

my_car.drive()  # "Driving..."
print(my_car.gas)  # 7

my_car.drive()  # "Driving..."
print(my_car.gas)  # 6

my_car.drive()  # "Driving..."
print(my_car.gas)  # 5

my_car.drive()  # "Driving..."
print(my_car.gas)  # 4

my_car.drive()  # "Driving..."
print(my_car.gas)  # 3

my_car.drive()  # "Driving..."
print(my_car.gas)  # 2

my_car.drive()  # "Driving..."
print(my_car.gas)  # 1

my_car.drive()  # "Driving..."
print(my_car.gas)  # 0

my_car.drive()  # "Out of gas!"
