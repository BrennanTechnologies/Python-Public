import random
import array as arr
#from array import *

# Manual Array
# myArr = arr.array('i', [1,2,3,4])
# myArr[1] = 100
# myArr.append(2000)

# Create random array
def make_array(num_elements, min_val, max_val):
	a = arr.array("i")
	for i in range(0,num_elements):
		a.append(random.randint(min_val,max_val))
	return a

# find Min/Max
# ------------------------------------
def find_minmax(a):
	max_val = 0
	min_val = a[0]

	for i in range(len(a)):
		if a[i] > max_val:
			max_val = a[i]

		if a[i] < min_val:
			min_val = a[i]

	return (min_val, max_val)

num_elements = 15
min_val = 0
max_val = 100
a = make_array(num_elements=4, min_val=0, max_val=10)
print(a)
a.reverse()
print(a)
print(find_minmax(a))

print(min(a))
print(max(a))

