import csv

def import_data():
	headersCSV = ['Surname', 'Name', 'Phone', 'Comment']
	surname = input('Введите фамилию -> ')
	name = input('Введите имя -> ')
	phone = input('Введите номер телефона -> ')
	comment = input('Введите комментарий -> ')
	dict = {'Surname': surname, 'Name': name, 'Phone': phone, 'Comment': comment}
	with open("HomeWork\HomeWork_7\Example.csv", mode="a", encoding='utf-8') as a_file:
		file_writer = csv.DictWriter(a_file, delimiter = ";", fieldnames = headersCSV, lineterminator="\r")
		file_writer.writerow(dict)


# Surname;Name;Phone;Comment
