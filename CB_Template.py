import sys
import random
import array as arr
import CB_Module as cb
from datetime import date
from datetime import datetime


# ----------------------------------------
# MAIN:
# ----------------------------------------
def main(): 
	print(" *** __main__ ***") 
	func_name = sys._getframe().f_code.co_name
	print("\n\t EXECUTING: ==> \t ***** " + func_name + " *****")

	#####################################
	### Start: -- MAIN --
	#####################################

	cb.write_log("Hello World!")
	cb.write_log("An error ocurred!", "ERROR")
	
	wl = cb.write_log
	wl("Alias of write-log function.")

	cb.read_file("logfile.log")

	#####################################
	### End: -- MAIN --
	#####################################

	try:
		print("Try")
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

def begin():
	pass

def end():
	pass

def module():
	pass

# ---------------------------------------- 
# Runtime Execution Mode:
# ----------------------------------------
# Run at Runtime
if __name__=="__main__": 
	begin()
	main() 
	end()
# Run on Import
if __name__!="__main__": 
	module()