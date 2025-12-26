# Python3 code to demonstrate 
# to check if list is sorted
# using naive method 
 
# initializing list
import random


#test_list = [1, 4, 5, 8, 7, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20]
test_list = [1, 2, 3, 4, 5, 6, 7, 8]
random.shuffle(test_list)
listCount = len(test_list)

# printing original list 
print ("Original list : " + str(listCount) + " " + str(test_list))

def isSorted(arr):
	for i in range(1, len(arr)):
		if arr[i] < arr[i-1]:
			return False
	return True

i = 0
while isSorted(test_list) == False:
	i += 1
	random.shuffle(test_list)

print(str(i) + ": " + str(test_list))

#isSorted = isSorted(test_list)
#print(isSorted)



# using naive method to 
# check sorted list 
#flag = 0
#i = 1
#while i < len(test_list):
#    if(test_list[i] < test_list[i - 1]):
#        flag = 1
#    i += 1
     
# printing result
#if (isSorted) :
#    print ("Yes, List is sorted.")
#else :
#    print ("No, List is not sorted.")
#    random.shuffle(test_list)