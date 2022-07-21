# Задайте список из вещественных чисел.
# Напишите программу, которая найдет разницу
# между максимальным и минимальным значением
# дробной части элементов.

import random

def fillArray(arr):
	for i in range(len(arr)):
		arr[i] = round(random.random() * 10, 2)
	return arr

def newArray(arr):
	for i in range(len(arr)):
		arr[i] = round(arr[i] - int(arr[i]), 2)
	return arr

def diffMaxMin(arr):
	max = arr[0]
	min = arr[0]
	for i in range(len(arr)):
		if arr[i] > max:
			max = arr[i]
		if arr[i] < min:
			min = arr[i]
	return max - min


numbers = [None] * 10
print(fillArray(numbers))
print(newArray(numbers))
print(diffMaxMin(newArray(numbers)))