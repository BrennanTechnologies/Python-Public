### Recursive Function


def factorial(n):
	print("Inside Function: " + str(n))
	if n == 0:
		return 1
	return n * factorial(n - 1)

n = 5
print("Outside Function: " + str(n))
print(factorial(n)) # 5 * 4 * 3 * 2 * 1 = 120s

