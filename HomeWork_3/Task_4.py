# Напишиет программу, которая будет
# преобразовывать десятичное число
# в двоичное.

num10 = int(input('Введите число в десятичной системе счисления -> '))

def convertToBinary(num):
	if num > 0:
		n = num % 2
		num = num // 2
		convertToBinary(num)
		print (n, end = ' ')

convertToBinary(num10)