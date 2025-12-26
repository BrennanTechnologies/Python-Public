import sys
import os
import random
import array as arr
import CB_Module as cb
from datetime import date
from datetime import datetime

### Function Template:
### -----------------------------------
def function_template(a,b):
	try:
		print("Try")
	except NameError:
		print ("Name Error")
	except TypeError:
		print("Error: cannot add an int and a str")
	except ZeroDivisionError:
		print("Div by Zero")
	except:
		error_type, error_instance, traceback = sys.exc_info()
		print(sys.exc_info())
		print("Other Error")
	else:
		print("Else")
	finally:
		print("Finally")

### Timer Decorator:
def timer_decorator(func):
	def wrapper(*args, **kwargs):
		start_time = datetime.now()
		result = func(*args, **kwargs)
		end_time = datetime.now()
		elapsed_time = end_time - start_time
		print(f"Function '{func.__name__}' executed in: {elapsed_time}")
		return result
	return wrapper

@timer_decorator
def find_sum_up_to_n(n):
	total = 0
	for i in range(1, n + 1):
		total += i
	return total
print(find_sum_up_to_n(1000000))

result = find_sum_up_to_n(1000000)
print(result)


def print_function_name():
	func_name = sys._getframe().f_code.co_name
	print("\n\t EXECUTING: ==> \t ***** " + func_name + " *****")

	print("\n\t EXECUTING: ==> \t ***** " + str(sys._getframe().f_code.co_name) + " *****")

### Say Hello:
### -----------------------------------
def say_hello(name="World"):
	return f"Hello {name}"


### Write Log:
### -----------------------------------
def write_log(msg, cat="INFO"):
	print("\n\t EXECUTING: ==> \t ***** " + str(sys._getframe().f_code.co_name) + " *****")

	# Print Msg
	print(msg)

	# Open Log File
	log_file = "logfile.log"
	file = open(log_file, 'a+')

	# Date/Time
	today = date.today()
	time = datetime.now()
	time = time.strftime("%H:%M:%S")

	# Build Msg String
	msg = str(time) + "\t" +str(today) + "\t" + cat + "\t" + msg + "\n"

	# Write File / Close File
	file.write(msg)
	file.close()

### Read File:
### -----------------------------------
def read_file(file_name):
	file = open(file_name, 'r')
	print(file.read())
	file.close()

### Create random array
### -----------------------------------
def make_random_array(num_elements, min_val, max_val):
	#a = arr.array("i")
	a = []
	for i in range(0,num_elements):
		a.append(random.randint(min_val,max_val))
	return a

### Linear search
### -----------------------------------
def linear_search(arr, n):
	found = False
	for i in range(len(arr)):
		if arr[i] == n:
			found = True
	return i

### Binary Search
### -----------------------------------
'''
Binary Search:
	- The array must be sorted
	- The algorithm compares the target value to the middle element of the array
	- If they are not equal, the half in which the target cannot lie is eliminated and the search continues on the remaining half, again taking the middle element to compare to the target value, and repeating this until the target value is found
	- If the search ends with the remaining half being empty, the target is not in the array
	- The algorithm is O(log n)
	- The algorithm is O(1) space complexity
	- The algorithm is O(n) time complexity
'''
def binary_search(arr, n, start=0, end=None):
	'''
	example:
		index_of_target_value = binary_search(arr, n, start, end)

		- arr: array
		- n: target value
		- start: start index
		- end: end index
		- mid: middle index
		- return: index of target value
	'''
	if end is None:
		end = len(arr) - 1

	if start > end:
		return -1  # Element not found

	mid = start + (end - start) // 2

	if arr[mid] == n:
		return mid
	elif arr[mid] > n:
		return binary_search(arr, n, start, mid - 1)
	else:
		return binary_search(arr, n, mid + 1, end)

### Lazy Git:
### -----------------------------------
def lazygit():
	print("\n\t EXECUTING: ==> \t ***** " + str(sys._getframe().f_code.co_name) + " *****")

	cmds = [
				'git add .',
				'git commit -m "Sync"',
				'git push'
			]
	for cmd in cmds:
		print("\t***** EXECUTING: ***** ==> " + cmd)
		os.system(cmd)
		#os.system(cmd + " > null")
		#output = os.system(cmd + " 2> null")
		#print(output)
#g = lazygit()

### List Modules:
### -----------------------------------
def list_modules():
	import sys
	output = [module.__name__ for module in sys.modules.values() if module]
	output = sorted(output)
	for o in output:
		print(o)

### Is Module Loaded?:
### -----------------------------------
def isModule_loaded():
	module_name = "CB_Module"
	if module_name in sys.modules:
		print("Found ME!!!")
		#print(module_name + " was found!")
	else:
		print(module_name + " was NOT found!")

def print_format_table():
    """
    prints table of formatted text format options
    """
    for style in range(8):
        for fg in range(30,38):
            s1 = ''
            for bg in range(40,48):
                format = ';'.join([str(style), str(fg), str(bg)])
                s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
            print(s1)
        print('\n')

def show_colors():
	class bcolors:
		HEADER = '\033[95m'
		OKBLUE = '\033[94m'
		OKCYAN = '\033[96m'
		OKGREEN = '\033[92m'
		WARNING = '\033[93m'
		FAIL = '\033[91m'
		ENDC = '\033[0m'
		BOLD = '\033[1m'
		UNDERLINE = '\033[4m'

	print(bcolors.HEADER + "HEADER: " + bcolors.ENDC)
	print(bcolors.OKBLUE + "OKBLUE: " + bcolors.ENDC)
	print(bcolors.OKCYAN + "OKCYAN: " + bcolors.ENDC)
	print(bcolors.WARNING + "WARNING: " + bcolors.ENDC)
	print(bcolors.FAIL + "FAIL: " + bcolors.ENDC)
	print(bcolors.ENDC + "ENDC: " + bcolors.ENDC)
	print(bcolors.BOLD + "BOLD: " + bcolors.ENDC)
	print(bcolors.UNDERLINE + "UNDERLINE: " + bcolors.ENDC)
