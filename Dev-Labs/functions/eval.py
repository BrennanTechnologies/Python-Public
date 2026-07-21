# number = 9

# # eval performs the multiplication passed as argument
# square_number = eval('number * number')
# print(square_number)

# # Output: 81


#############################

# Perimeter of Square
def calculatePerimeter(l):
    return 4*l

# Area of Square
def calculateArea(l):
    return l*l

expression = input("Type a function: ")

for l in range(1, 5):
    if (expression == 'calculatePerimeter(l)'):
        print("If length is ", l, ", Perimeter = ", eval(expression))
    elif (expression == 'calculateArea(l)'):
        print("If length is ", l, ", Area = ", eval(expression))
    else:
        print('Wrong Function')
        break