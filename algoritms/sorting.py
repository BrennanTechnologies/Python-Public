import CB_Module as cb


def bubble_sort(arr):
	# O(n^2)
	# Outer Loop: Traverse through all array elements
	for i in range(len(arr)):
		# Inner Loop: Remove last element i (bubble up)
		for j in range(len(arr) - i - 1): 
			# compare
			if arr[j] > arr[j+1]:
				# swap
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
	return arr

def insertion_sort(arr):
	# O(n)
	for i in range(len(arr)):
		print(arr[i])


if __name__=="__main__": 
	
	num_elements = 10
	min_val = 0
	max_val = 9
	arr = cb.make_random_array(num_elements, min_val, max_val)
	print(str(arr))

	bubble_sorted = bubble_sort(arr)
	#print(bubble_sorted)

	insertion_sorted = insertion_sort(arr)
	print(insertion_sorted)

