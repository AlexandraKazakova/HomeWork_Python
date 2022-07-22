# Задана натуральная степень k. Сформировать случайным образом
# список коэффициентов (значения от 0 до 100) многочлена и вывести на экран.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

k = int(input('Введите степень многочлена -> ' ))
m = k + 1

def listOfCoef(coef):
	lstCoef = [random.randint(0,100) for i in range(coef +1)]
	return lstCoef

def poly(co, arr):
	for i in arr:
		if co == 1:
			i = print(i, '* x', end = ' + ')
		elif co == 0:
			i = print(i, ' = 0')
		else:
			i = print(i, '* x ^', co, end = ' + ')
		co -= 1

poly(k, listOfCoef(k))
