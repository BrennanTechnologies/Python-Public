#import random
from random import randint
rnd = randint(1,9)
print(rnd)


while True:
	guess = input("Enter a Guess: ")
	print(guess)
	if int(guess) == rnd:
		print("You Win! The number was: " + str(rnd))
		break

