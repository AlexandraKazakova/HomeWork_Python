# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

print('Введите номер четверти -> ', end = '')
num = int(input())
if num == 1:
	print('Диапазон возможных координат: x = от 0 до бесконечности, y = от 0 до бесконечности')
elif num == 2:
	print('Диапазон возможных координат: x = от 0 до минус бесконечности, y = от 0 до бесконечности')
elif num == 3:
	print('Диапазон возможных координат: x = от 0 до минус бесконечности, y = от 0 до минус бесконечности')
elif num == 4:
	print('Диапазон возможных координат: x = от 0 до бесконечности, y = от 0 до минус бесконечности')
else:
	print('Введите число от 1 до 4')