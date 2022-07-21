# Напишите программу, которая найдет произведение
# пар чисел списка. Парой считаем первый и последний
# элемент, и т.д.

import random

def fillArray(arr):

	for i in range(len(arr)):
		arr[i] = random.randint(1,10)
	return arr

def findMulti(arr):
	index = 0
	if len(arr) % 2 != 0:
		count = len(arr) // 2 + 1
	else:
		count = len(arr) // 2
	while index < count:
		num = arr[index] * arr[-(index+1)]
		print(num, end = ' ')
		index += 1


numbers = [None] * 9

print(fillArray(numbers))
findMulti(numbers)