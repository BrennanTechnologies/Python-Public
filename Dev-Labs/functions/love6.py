'''
The number 6 is a truly great number. Given two int values, a and b, return True if either one is 6. Or if their sum or difference is 6. Note: the function abs(num) computes the absolute value of a number.

love6(6, 4) → True
love6(4, 5) → False
love6(1, 5) → True
'''

import random

A = random.randint(0,9)
B = random.randint(0,9)
print(str(A) + " and " + str(B))

def findLove(a, b):
	if A == 6 or B== 6:
		love = True
	elif A+B == 6:
		love = True
	elif A-B == 6:
		love = True
	else:
		love = False
	return love

love = findLove(A,B)
print(love)

### Refactored Version
### -----------------------------------
import random

A = random.randint(0, 9)
B = random.randint(0, 9)
print(f"{A} and {B}")

def findLove(a, b):
    return 6 in (a, b) or abs(a + b) == 6 or abs(a - b) == 6

love = findLove(A, B)
print(love)
