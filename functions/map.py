b = [1, 3, 4, 6]
a = [1, 65, 7, 9]

# Declare a separate function to handle the addition:</strong> 
def add(a, b):
	return a+b

# Pass the function and the two lists into the built-in map() function:</strong> 
a = sum(map(add, b, a))
print(a) 

# Output: 96