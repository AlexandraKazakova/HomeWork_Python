# Создайте программу для игры в "Крестики-нолики".
from random import randint
from unittest import result

def checkArr(arr):
	if (arr[0][0] == 'X' and arr[1][1] == 'X' and arr[2][2] == 'X'
	or arr[0][2] == 'X' and arr[1][1] == 'X' and arr[2][0] == 'X'
	or arr[0][0] == 'X' and arr[0][1] == 'X' and arr[0][2] == 'X'
	or arr[1][0] == 'X' and arr[1][1] == 'X' and arr[1][2] == 'X'
	or arr[2][0] == 'X' and arr[2][1] == 'X' and arr[2][2] == 'X'
	or arr[0][0] == 'X' and arr[1][0] == 'X' and arr[2][0] == 'X'
	or arr[0][1] == 'X' and arr[1][1] == 'X' and arr[2][1] == 'X'
	or arr[0][2] == 'X' and arr[1][2] == 'X' and arr[2][2] == 'X'):
		return 'X'
	elif (arr[0][0] == '0' and arr[1][1] == '0' and arr[2][2] == '0'
	or arr[0][2] == '0' and arr[1][1] == '0' and arr[2][0] == '0'
	or arr[0][0] == '0' and arr[0][1] == '0' and arr[0][2] == '0'
	or arr[1][0] == '0' and arr[1][1] == '0' and arr[1][2] == '0'
	or arr[2][0] == '0' and arr[2][1] == '0' and arr[2][2] == '0'
	or arr[0][0] == '0' and arr[1][0] == '0' and arr[2][0] == '0'
	or arr[0][1] == '0' and arr[1][1] == '0' and arr[2][1] == '0'
	or arr[0][2] == '0' and arr[1][2] == '0' and arr[2][2] == '0'):
		return '0'
	else:
		return -1


tttArray = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]

name1 = input('Введите свое имя -> ')
name2 = input('Введите свое имя -> ')
print('')

num = randint(1, 2)

if num == 1:
	theFirst = name1
	theSecond = name2
	print(f'У {theFirst} крестики')
else:
	theFirst = name2
	theSecond = name1
	print(f'У {theFirst} крестики')

def printArr(arr):
	print(*arr[0])
	print(*arr[1])
	print(*arr[2])

for i in range(9):
	if i % 2 == 0:
		step = 'X'
		print(f'Сейчас ходит {theFirst}')
	else:
		step = '0'
		print(f'Сейчас ходит {theSecond}')
	row = int(input('Введите номер строки -> '))
	column = int(input('Введите номер столбца -> '))
	while row > 3 or row < 0 or column < 0 or column > 3:
		print('Строки и столбцы могут быть только числами от 1 до 3')
		row = int(input('Введите номер строки -> '))
		column = int(input('Введите номер столбца -> '))
	while tttArray[row - 1][column - 1] != '_':
		print('Эта клетка занята, выбери другую')
		row = int(input('Введите номер строки -> '))
		column = int(input('Введите номер столбца -> '))
		while row > 3 or row < 0 or column < 0 or column > 3:
			print('Строки и столбцы могут быть только числами от 1 до 3')
			row = int(input('Введите номер строки -> '))
			column = int(input('Введите номер столбца -> '))
	if tttArray[row - 1][column - 1] == '_':
		tttArray[row - 1][column - 1] = step
	res = checkArr(tttArray)
	if res == 'X':
		print(f'{theFirst} выиграл!')
		printArr(tttArray)
		exit()
	elif res == '0':
		print(f'{theSecond} выиграл!')
		printArr(tttArray)
		exit()
	elif res == -1 and i == 8:
		print('Ничья!')
	printArr(tttArray)
