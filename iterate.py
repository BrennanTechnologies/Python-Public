fruits = ["grape", "apple", "mango"]
for i, j in enumerate(fruits):
	print(i, j)



# Whereas, you might've wasted valuable time using the following method to achieve this:

fruits = ["grape", "apple", "mango"]
for i in range(len(fruits)):
	print(i, fruits[i])