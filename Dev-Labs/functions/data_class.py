from dataclasses import dataclass, field

@dataclass
class Employee:
	name: str
	address: str
	active: bool = True

class Person:
	def __init__(self,name: str, address: str):
		self.name = name
		self.address = address
	
	def __str__(self) -> str:
		return f"Name: {self.name}, Address: {self.address}"

	def __post_init__(self) -> None:
		self.search_string = f"{self.name}, {self.address}"

	def __repr__(self) -> str:
		return f"rName: {self.name}, rAddress: {self.address}"
	
	def __get__(self) -> str:
		return self.search_string
	
	def __eq__(self, o: object) -> bool:
		return self.search_string == o.search_string
	
def main():
	person = Person(name="Chris", address="123 Main St.")
	print(person)
	#print(str(person))
	#print(repr(person))

	emp = Employee(name="Chris", address="123 Main St.")
	print(emp)


if __name__=="__main__": 
	main() 
