import random
import CB_Module as cb

def isSorted(arr):
	for i in range(len(arr)):
		print([i])
		# if arr[i] > arr[i]+1:
		# 	print("bigger")
		# 	print(arr[i])
		# 	#return False
		# else:
		# 	print("else")
		# 	#print(arr[i])

	#print()
def random_sort(arr):

	print()

if __name__=="__main__": 
	
	num_elements = 10
	min_val = 0
	max_val = 9
	arr = cb.make_random_array(num_elements, min_val, max_val)
	print(str(arr))

	isSorted = isSorted(arr)
	print(isSorted)



