# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов
# исходной последовательности.

import random

def fillArray(arr):
	for i in range(len(arr)):
		arr[i] = random.randint(0,9)
	return arr
numbers = [None] * 10
print(fillArray(numbers))
newNum = []
[newNum.append(i) for i in numbers if i not in newNum]
print(newNum)
