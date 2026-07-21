
import CB_Module as cb
import random
import time

# Linear search
def linear_search(arr, n):
	found = False
	for i in range(len(arr)):
		if arr[i] == n:
			found = True
	return i

# Binary Search
def binary_search(arr, n, start=0, end=None):
	if end is None:
		end = len(arr) - 1

	if start > end:
		return -1  # Element not found

	mid = start + (end - start) // 2

	if arr[mid] == n:
		return mid
	elif arr[mid] > n:
		return binary_search(arr, n, start, mid - 1)
	else:
		return binary_search(arr, n, mid + 1, end)

if __name__=="__main__": 
	arr = []
	size = 10000000
	for i in range(0,size):
		arr.append(random.randint(0,9))
	#arr = [ 2, 3, 4, 10, 40 ]
	print(arr)

	n = 11
	arr.append(11)

	# binary
	start_time = time.time()
	bsearch = binary_search(arr, n,)
	end_time = time.time()
	run_time = end_time - start_time
	print(run_time)
	print(bsearch)

	# linear
	start_time = time.time()
	lsearch = linear_search(arr, n,)
	end_time = time.time()
	run_time = end_time - start_time
	print(run_time)
	print(lsearch)

	# exponential search








