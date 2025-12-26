
import random

list = []
for i in range(1,5):
	n = random.randint(0,9)
	list.append(n)
print(list)

# Find Max in list
max = 0
for i in range(len(list)):
	if list[i] > max:
		max = list[i]

print(max)

