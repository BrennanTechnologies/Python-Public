class Car:

    wheels = 4

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.is_running = False

    def start_engine(self):
        self.is_running = True
        print("Engine started.")

    def stop_engine(self):
        self.is_running = False
        print("Engine stopped.")

    def honk(self):
        if self.is_running:
            print("Beep beep!")
        else:
            print("Cannot honk. The engine is not running.")


my_car = Car("Toyota", "Corolla", 2021)
print(my_car.make)  # Output: Toyota
print(my_car.model)  # Output: Corolla
print(my_car.year)  # Output: 2021

my_car.start_engine()  # Output: Engine started.
my_car.honk()  # Output: Beep beep!

my_car.stop_engine()  # Output: Engine stopped.
my_car.honk()  # Output: Cannot honk. The engine is not running.
