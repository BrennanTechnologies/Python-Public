# Python 3.x code to demonstrate the working of the reduce() function

# Importing functools to use reduce()
import functools

#Defining function which will be used with reduce to find sum
def sum(num1,num2):
    print("num1= ", num1, " num2= ", num2)
    return num1+num2

# Using reduce with the above sum function to find the sum of listExample
print("The sum of numbers from 1 to 5, i.e., in the range [1,6), is: ", functools.reduce(sum, range(1,6)))

# Creating a list
listExample = [1, 2, 3, 4, 5]

# Using reduce with lambda to find the sum of listExample
print("The sum of all the elements in the list is: ", end="")
print(functools.reduce(lambda num1, num2: num1+num2, listExample))

# Using reduce to find the product of listExample
print("The product of all the elements in the list is: ", end="")
print(functools.reduce(lambda num1, num2: num1*num2, listExample))

# Using reduce to find the maximum element from listExample
print("The maximum element of the list is: ", end="")
print(functools.reduce(lambda num1, num2: num1 if num1 > num2 else num2, listExample))