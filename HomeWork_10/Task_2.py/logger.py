from random import randint

def who_the_first():
	n = randint(1,2)
	return n

def bot_move(num):
	number = num % 29
	if number == 0:
		return 1
	else:
		return number
