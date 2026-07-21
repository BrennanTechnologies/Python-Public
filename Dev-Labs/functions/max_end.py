import random

list = []
for i in range(0,3):
	n = random.randint(0,9)
	list.append(n)
print(list)


beg = list[0]
end = list[-1]
if beg > end:
	max = beg
else:
	max = end


for i in range(len(list)):
	list[i] = max

print(list)
