

def end_other(a, b):
	lenA = len(a)
	lenB = len(b)
	
	endA = a[len(a)-lenB:]
	endB = b[len(b)-lenA:]
	
	print(lenA)
	print(endB)
	
	if a == endB or b == endA:
		print("True")



end_other('abc', 'abXabc') 
#end_other('Hiabc', 'abc')