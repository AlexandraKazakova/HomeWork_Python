# Задайте список из нескольких чисел.
# Напишите программу, которая найдет
# сумму элементов списка, стоящих на
# нечетных позициях.

import random

def fillArray(arr):
	for i in range(len(arr)):
		arr[i] = random.randint(0,100)
	return arr

def findSum(arr):
	sum = 0
	for i in range(len(arr)):
		if i % 2 != 0:
			sum += arr[i]
	return sum

numbers = [None] * 10
print(fillArray(numbers))
print(findSum(numbers))