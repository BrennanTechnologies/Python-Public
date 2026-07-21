# code asks user for number and divides 10 by it
# enter '0' to trigger exception

# input = int(input("Enter Number: "))
# print("input: " + str(input))
# breakpoint()
# '''

try:
    a = 10
    answer = 10 + a / int(input("Enter Number: "))
    print(answer)
except ValueError:
    print(_ + "Invalid Input")
except ZeroDivisionError as e:
    print("error: " + str(e))
except:
    print("Caught any exception")

# '''
