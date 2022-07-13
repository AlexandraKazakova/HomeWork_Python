# Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.
# Пример:

# 6782 -> 23
# 0,56 -> 11

num = input('Введите число ')

num = num.replace('.' , '') 
num = num.replace(',' , '')
lst_str = list(num)
lst_num = map(int, lst_str)
s = sum(lst_num)
print(s)