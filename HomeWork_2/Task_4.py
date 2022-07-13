# Вклад в банке составляет Х рублей. Ежегодно он 
# увеличивается на Р процентов, после чего дробная
# часть копеек отбрасывается. Требуется определить:
# через сколько лет вклад составит не менее Y рублей.
# Пример:
# 100
# 10
# 200
# Вывод:
# 8
deposit = float(input('Введите сумму вклада -> '))
percent = float(input('Ежегодный процент -> '))
finalDep = float(input('Введите нужную сумму -> '))
years = 0
while(deposit < finalDep):
	deposit = round(deposit + (deposit * (percent * 0.01)),0)
	years += 1
	print(deposit)
print(years)