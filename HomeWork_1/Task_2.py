# Напишите программу для проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
print('Если утверждение X истинно ввдедите 1, если нет - 0 -> ', end = '')
x = int(input())
print('Если утверждение Y истинно ввдедите 1, если нет - 0 -> ', end = '')
y = int(input())
print('Если утверждение Z истинно ввдедите 1, если нет - 0 -> ', end = '')
z = int(input())
if x > 1 or y > 1 or z > 1:
	result = 'Некорректный ввод'
else:
	a = not (x or y or z)
	b = (not x) and (not y) and (not z)
	result = a == b
print(result)