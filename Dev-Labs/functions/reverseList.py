
#list = [1,2,3]
list = range(1,50,1)

def reverseList(list):
	for i in list:
		print(list[len(list)-i],end=", ")

reverseList(list)