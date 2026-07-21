a = ("John", "Charles", "Mike", "1")
b = ("Jenny", "Christy", "Monica", "2")
c = ("Chris", "Scott", "Wendy", "Paul")
d = ("A", "B", "C", "D")

z = zip(a, b, c, d)

for x in z:
	#print(x)
	pass



names = ['Mukesh', 'Roni', 'Chari']
ages = [24, 50, 18]

z = zip(names, ages)
y = zip(names, ages)

# for i in enumerate(z):
# 	print("enum: " + str(type(i)))
# 	print(i)

# for i in y:
# 	print("loop: " + str(type(i)))
# 	print(i)

a= [1,2,3]
for i in range(len(a)):
	print("i-" + str(i) + ": " + str(a[i]))
	#print(a[i])

for i,e in enumerate(a):
	print(e)

#for i, (name, age) in enumerate(z):
    #print(i, name, age)

#for i, name, age in enumerate(z):
    #print(i, name, age)
    
# for i in enumerate(z):
#     print(i)