import sys

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

def myTest():
	#func_name = sys._getframe().f_code.co_name 	# print(" *** __main__ ***") 
	print(bcolors.HEADER + "\n\t EXECUTING: ==> \t ***** " + sys._getframe().f_code.co_name + " *****" + bcolors.ENDC)


# ----------------------------------------
# MAIN:
# ----------------------------------------
def main(): 
	print(f'__name__: {__name__}')
	func_name = sys._getframe().f_code.co_name 	# print(" *** __main__ ***") 
	print(bcolors.HEADER + "\n\t EXECUTING: ==> \t ***** " + func_name + " *****" + bcolors.ENDC)

if __name__=="__main__": 
	main() 
	myTest()
