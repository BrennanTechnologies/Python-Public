

def even_nums1(list):
	evens = []
	for i in list:
		if i % 2 == 0:
			evens.append(i)
	return evens
	


def even_nums(list):
	return [i for i in list if i % 2 == 0]

##########
list = [i for i in range(1, 31)]
evens = even_nums(list)

print(list)
print(evens)