# python code to demonstrate working of reduce() 

# importing functools for reduce() 
import functools 
import random
# initializing list 
# lst = [1, 3, 5, 6, 2] 

# lst = []
# for i in range(0,9):
# 	lst.append(random.randint(0,9))
# print(lst)


# lst = [random.randint(1,999) for i in range(0,15)]
# print(lst)
# #exit()

# #lst.append(66)

# # using reduce to compute sum of list 
# print("The sum of the list elements is : ", end="") 
# print(functools.reduce(lambda a, b: a+b, lst)) 

# print("The Multi of the list elements is : ", end="") 
# print(functools.reduce(lambda a, b: a-b, lst)) 

# # using reduce to compute maximum element from list 
# print("The maximum element of the list is : ", end="") 
# print(functools.reduce(lambda a, b: a if a > b else b, lst)) 

# print("The MIN element of the list is : ", end="") 

def sum(lst):
	sum = 0
	for e in lst:
		sum = sum + e
	return sum 

lst = [10,2,3]
min = min(lst)
max = max(lst)
print(min)
print(max)

#my_sum = sum(lst)
#print(my_sum)
#print(functools.reduce(lambda a, b: a if a > b else b, lst)) 

