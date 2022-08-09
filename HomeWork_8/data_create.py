def id_data():
	id_worker = int(input('Введите уникальный номер сотрудника -> '))
	return id_worker

def name_data():
	name = input('Введите имя -> ')
	return name


def surname_data():
	surname = input('Введите фамилию -> ')
	return surname


def phone_data():
	phone = input('Введите телефон -> ')
	return phone


def address_data():
	address = input('Введите адрес -> ')
	return address

def b_day_data():
	b_day = input('Введите дату рождения -> ')
	return b_day

def status_data():
	status = int(input('1 - женат\n2 - холост\n-> '))
	if status == 1:
		return 'married'
	else:
		return 'unmarried'

def gender_data():
	gender = int(input('Пол:\n1 - мужской\n2 - женский\n-> '))
	if gender == 1:
		return 'male'
	else:
		return 'female'

def position_data():
	position = int(input('1 - рабочий\n2 - менеджер\n3 - руководитель отдела\n4 - директор\n5 - курьер\n6 - стажер\n-> '))
	if position == 1:
		return 'worker'
	elif position == 2:
		return 'manager'
	elif position == 3:
		return 'supervisor'
	elif position == 4:
		return 'director'
	elif position == 5:
		return 'courier'
	else:
		return 'improver'
