import sys
import os
import random
import array as arr
import CB_Module as cb
from datetime import date
from datetime import datetime

class bcolors:
	HEADER  = '\033[95m'
	OKBLUE  = '\033[94m'
	OKCYAN  = '\033[96m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL    = '\033[91m'
	ENDC    = '\033[0m'
	BOLD    = '\033[1m'
	UNDERLINE = '\033[4m'

# ----------------------------------------
# MAIN:
# ----------------------------------------
def main(): 
	os.system('cls')

	func_name = sys._getframe().f_code.co_name 	# print(" *** __main__ ***") 
	print(bcolors.HEADER + "\n\t EXECUTING: ==> \t ***** " + func_name + " *****" + bcolors.ENDC)

	#####################################
	### Start: -- MAIN -- 
	#####################################
		
	print("Hello World!")

	cb.write_log("New Log")

	cb.lazygit() # See def end()

	#cb.show_colors()

	#print(f"{bcolors.WARNING}Warning: No active frommets remain. Continue?{bcolors.ENDC}")

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
	#cb.lazygit()

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

