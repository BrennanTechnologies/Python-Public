def my_sum(*args):
	my_sum = 0
	for arg in args:
		my_sum = my_sum + arg
	return my_sum

results = my_sum(1, 2, 3, 4, 5)
print(results)