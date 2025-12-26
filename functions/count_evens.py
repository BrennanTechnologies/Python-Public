import random

list = []
for i in range(0,5):
	n = random.randint(0,9)
	list.append(n)
print(list)

count = 0
for i in range(len(list)):
	if list[i] % 2 == 0 and list[i] != 0:
		count += 1

print(count)