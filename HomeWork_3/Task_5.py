# Задайте число. составьте список
# чисел Фибоначчи, в том числе для
# отрицательных интексов.
# *Пример:*

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

# num = int(input())
# n1 = 0
# n2 = 1

# def fibo(n, m, count):
# 	i = 0
# 	m1 = m
# 	while i < count:
# 		print(m1, end = ' ')
# 		m1 = n + m
# 		n = m
# 		m = m1
# 		i += 1

# print(n1, end = ' ')
# fibo(n1, n2, num)
fib1 = fib2 = 1
n = int(input())
print( fib1, fib2, end=' ')
for i in range(2, n):
	fib1, fib2 = fib2, fib1 + fib2
	print(fib2, end=' ')

