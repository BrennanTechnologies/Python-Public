import random
list = []

# Create random List
for i in range(0,20):
	n = random.randint(0,3)
	list.append(n)
print(list)


# Create Unique List
uniq = set(list)
#print(uniq)



n = 9
def array_count(list, n):
	itemCount = 0
	for i in list:
		if i == n:
			itemCount = itemCount+1

	return itemCount

itemCount = array_count(list, n)
print("Count of " + str(n) + ": " + str(itemCount))

