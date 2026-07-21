


x = 5
y = "hello"

try:
	#a = 1/0
	#z = x + y
	y = 1+1
	print(y)
	#raise NameError("Hi there")

except NameError:
    print ("Name Error")
except TypeError: 
	print("Error: cannot add an int and a str")
except ZeroDivisionError:
	print("Div by Zero")
except:
	print("Other Error")
else:
	print("Else")
finally:
	print("Finally")