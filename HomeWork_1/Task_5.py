# Напишите программу, которая принимает на вход координаты 
# двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21


print('Введите координаты точки A -> ', end = '')
a1, a2 = float(input()), float(input())
print('Введите координаты точки B -> ', end = '')
b1, b2 = float(input()), float(input())
result = round(pow((b1 - a1)**2 + (b2 - a2)**2, 1/2), 2)
print(result)
