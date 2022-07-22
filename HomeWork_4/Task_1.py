# Вычислить число c заданной точностью d
# Пример:
# - при d = 3, π = 3.141

# import math

d = int(input('Введите число -> '))
# p = str(math.pi)

# for i in range(len(p)):
# 	if i < d + 2:
# 		print(p[i], end = '')

n = 100

pi2 = str(sum(1/16**x*(4/(8*x + 1) - 2/(8*x + 4) - 1 / (8*x + 5) - 1/(8*x + 6)) for x in range(n)))

for i in range(len(pi2)):
	if i < d + 2:
		print(pi2[i], end = '')
