# Monkey Trouble

'''
We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.
monkey_trouble(True, True) → True
monkey_trouble(False, False) → True
monkey_trouble(True, False) → False
'''

import random
class Monkey:
	def __init__(self, name):
		self.name = name

	def tellJoke(self):
		rnd = random.randint(0,1)
		if rnd == 1:
			self.smile = True
		else:
			self.smile = False



def monkey_trouble():
	A = Monkey("Monkey A")
	A.tellJoke()
	#print(A.name + " : " + str(A.smile))

	B = Monkey("Monkey B")
	B.tellJoke()
	#print(B.name + " : " + str(B.smile))

	#if (A.smile and B.smile) == True or (A.smile and B.smile) == False:
	if A.smile == True and B.smile == True:
		print("Your in trouble!!!")
	elif A.smile == False and B.smile == False:
		print("Your in trouble!!!")
	else:
		print("Your GOOD.")


for i in range(0, 10):
	#print("Count:" + str(i))
	monkey_trouble()

