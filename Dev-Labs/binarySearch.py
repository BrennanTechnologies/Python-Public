# Binary Search
def binary_search(arr, x):
	low = 0
	high = len(arr)
	mid = low + high // 2

	print("High : " + str(arr[high-1]))
	print("Mid  : " + str(arr[mid]))
	print("X    : " + str(x))

	if arr[mid] == x:
		print("Equal")
		return mid
	elif arr[mid] < x:
		print("GreaterThan")
		print(arr[mid+1:])
		return binary_search(arr[mid+1:], x)
	elif arr[mid] > x:
		print("LessThan") 
		print(arr[:mid-1])
		#return binary_search(arr[:mid-1], x)
	else:
		# Element Not Found in List
		return -1

arr = [1, 3, 4, 10, 40]
mid = len(arr) // 2
print("Mid       i: " + str(mid) + " = " + str(arr[mid]))
print("Mid-->End : " + str(arr[mid:]))
#print(arr[mid:])
x = 10
result = binary_search(arr, x)
print(result)
