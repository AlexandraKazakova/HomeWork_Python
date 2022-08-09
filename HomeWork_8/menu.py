from logger import*

def menu():
	print('Здравствуйте! Что необходимо сделать?\n'
			'1 - Внести сотрудника в базу данных\n'
			'2 - Удалить данные о сотруднике из базы\n'
			'3 - Внести изменения в информацию о сотруднике\n'
			'4 - Найти информацию о сотруднике\n'
			'5 - Вывести список всех сотрудников\n')

	command = int(input('Введите номер операции -> '))

	while command < 1 or command > 5:
		print('Неверный номер операции')
		command = int(input("Введите номер операции -> "))

	if command == 1:
		input_data()
	elif command == 2:
		delete_data()
	elif command == 3:
		change_data()
	elif command == 4:
		find_data()
	else:
		print_data()