# Simple class example
class Cat:
    def __init__(self, name, age, color):  # Constructor
        self.name = name
        self.age = age
        self.color = color

    def info(self):  # Method
        print(
            f"I am a cat. My name is {self.name}. I am a {self.color} {self.age} years old cat.")

    def make_sound(self):  # Method
        print(self.name + " " + "Meow")


cat1 = Cat('Andy', 2, 'black')
cat2 = Cat('Phoebe', 3, 'brown')

cat1.info()
cat2.make_sound()
