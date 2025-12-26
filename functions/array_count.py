import random
list = []

# Create random List
for i in range(0,20):
	n = random.randint(0,9)
	list.append(n)

# Create Unique List
uniq = set(list)

# Print Lists
print(list)
print(uniq)


for i in list:
	for j in range(list[1+1],len(list)):
		print(list[j], end=",")
		
#print(i)

