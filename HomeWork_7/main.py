from import_data import import_data
from export_data import export_data
from export_data import export_data_2

choice_act = input('Для ввода введите - 1, для вывода - 2\n')

if choice_act == '1':
	import_data()
elif choice_act == '2':
	a = input('Вывод в строку - 1, в столбец - 2 \n')
	if a == '1':
		export_data()
	elif a == '2':
		export_data_2()
	else:
		print('Некорректное значение')
else:
	print('Некорректное значение')