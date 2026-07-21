
import random

lst1 = []
for i in range(1,21):
	rnd = random.randint(0,9)
	lst1.append(rnd)
print(lst1)

################

lst2 = [random.randint(0, 9) for _ in range(1, 21)]
print(lst2)



