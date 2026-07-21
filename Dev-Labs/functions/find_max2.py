import random

def find_max(lst):
	max = 0
	for i in lst:
		if i > max:
			max = i
	return max



lst = []
for i in range(1,21):
	rnd = random.randint(0,9)
	print("rnd:" + str(rnd))
	lst.append(rnd)
print(lst)

lst = [random.randint(0, 99) for _ in range(1, 21)]
print(lst)

print("max: " + str(find_max(lst)))