class Pet:
	def __init__(self, name=None, age=None):
		self.name = name
		self.age = age

	def show(self):
		print("I am am " + self.name + " and I am " + str(self.age) + " years old.")
		print(f"I am {self.name} and I am {self.age} years old.")

	def speak(self):
		print("I dont know what to say")

class Dog(Pet):
	def __init__(self,name=None,color="Red"):
		super().__init__(name, age=None)
		self.color = color

	def speak(self):
		print("Bark")


class Cat(Pet):
	def speak():
		print("Meow")


d = Dog()
c = Cat("Angie",12)

print(type(d))
c.show()
d.speak()