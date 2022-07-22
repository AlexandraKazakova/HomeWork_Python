# Задайте натуральное число N. Напишите программу,
# которая составит список простых делителей числа N.
# (1 - составное число)

num = int(input('Введите натуральное число -> '))

def findSimple(n):
	k = 0
	for i in range(2, n):
		if n % i == 0:
			k += 1
	if k == 0:
		return n
	else:
		return

for j in range(2, num + 1):
	if num % j == 0:
		findSimple(j)
		if findSimple(j) == j:
			print(j, end = ' ')

