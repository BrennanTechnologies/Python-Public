import array as arr
import random
import sys

rows = 5
cols = 6

# Make array of len = 6
def make_array():
	#a = arr.array('i')
	a = []
	for _ in range(0,cols):
		a.append(random.randint(0,9))
	return a


# # make 2-dimensional array
# def make_multi_array1(rows,cols):
# 	#multi_arr = arr.array('i') # <--- Can't!!! - need NumPy
# 	multi_arr = [[]]
# 	for _ in range(0,rows):
# 		row = make_array()
# 		multi_arr.append(row)
# 	multi_arr = make_multi_array(5,6)
# 	print(multi_arr)


# def make_multi_array(rows, cols):
# 	arr = [[0]*cols]*rows
# 	print(arr)


def make_multi_array(rows, cols):
	multi_arr = []
	for _ in range(rows):
		row = make_array()
		multi_arr.append(row)
	return multi_arr

# ----------------------------------------
# MAIN:
# ----------------------------------------
def main(): 
	print(" *** __main__ ***") 
	func_name = sys._getframe(  ).f_code.co_name
	print("**** __" + func_name + "__ ****")

	# Make 1D array
	a = make_array()
	#print(a)

	print("my array:")	
	ma1 = make_multi_array(5,6)
	print(ma1)

	ma2 = make_multi_array(4,1)
	print(ma2)


# ---------------------------------------- 
# __name__ 
# ----------------------------------------
if __name__=="__main__": 
	main() 