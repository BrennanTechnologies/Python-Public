def outer(a, b):

	def sum(x, y):
		sum = x + y
		return sum
	
	sum = sum(a,b)

	return sum

result = outer(4,5)
print(result)