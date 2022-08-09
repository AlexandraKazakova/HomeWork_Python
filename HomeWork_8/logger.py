import sqlite3
from data_create import *

def input_data():
	conn = sqlite3.connect(r"HomeWork\HomeWork_8\work.db")
	cursor = conn.cursor()
	print("Подключен к SQLite")
	surname_input = surname_data()
	name_input = name_data()
	gender_input = gender_data()
	b_day_input = b_day_data()
	address_input = address_data()
	phone_input = phone_data()
	status_input = status_data()
	pos_input = position_data()
	cursor.execute('CREATE TABLE IF NOT EXISTS workers'
				'(worker_id INTEGER PRIMARY KEY AUTOINCREMENT, surname TEXT NOT NULL, name TEXT NOT NULL,'
				'gender TEXT, b_day TEXT, address TEXT, phone TEXT, status TEXT, position TEXT NOT NULL)')
	cursor.execute("""INSERT INTO workers (surname, name, gender, b_day, address, phone, status, position)
				VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", (surname_input, name_input,
				gender_input, b_day_input, address_input, phone_input, status_input, pos_input))
	conn.commit()
	cursor.close()
	conn.close()
	print('Данные сохранены')
	print("Соединение с SQLite закрыто")

def delete_data():
	conn = sqlite3.connect(r'HomeWork\HomeWork_8\work.db')
	cursor = conn.cursor()
	print("Подключен к SQLite")
	option = int(input('1 - удалить по уникальному номеру\n2 - удалить по фамилии\n-> '))
	if option == 1:
		worker_id_del = int(input('Введите ID работника, которого необходимо удалить из базы -> '))
		cursor.execute("DELETE from workers where worker_id = ?", [worker_id_del])
	else:
		surname_del = input('Введите фамилию работника, которого необходимо удалить -> ')
		cursor.execute("SELECT worker_id, surname, name FROM workers WHERE surname = ?",[surname_del])
		print(cursor.fetchall())
		worker_id_del = int(input('Введите ID работника, которого необходимо удалить из базы -> '))
		cursor.execute("DELETE from workers where worker_id = ?", [worker_id_del])
		
	conn.commit()
	print("Запись успешно удалена")
	cursor.close()
	conn.close()
	print("Соединение с SQLite закрыто")

def find_data():
	conn = sqlite3.connect(r'HomeWork\HomeWork_8\work.db')
	cursor = conn.cursor()
	print("Подключен к SQLite")
	surname_find = input('Введите фамилию работника, которого необходимо найти -> ')
	cursor.execute("SELECT * FROM workers WHERE surname = ?",[surname_find])
	result = cursor.fetchall()
	print(result)
	cursor.close()
	conn.close()
	print("Соединение с SQLite закрыто")

def change_data():
	conn = sqlite3.connect(r'HomeWork\HomeWork_8\work.db')
	cursor = conn.cursor()
	print("Подключен к SQLite")
	id_input = id_data()
	surname_input = surname_data()
	name_input = name_data()
	gender_input = gender_data()
	b_day_input = b_day_data()
	address_input = address_data()
	phone_input = phone_data()
	status_input = status_data()
	pos_input = position_data()
	cursor.execute("""UPDATE workers set surname = ?, name = ?, gender = ?,
					b_day = ?, address = ?, phone = ?, status = ?, position = ?
					WHERE worker_id = ?""", (surname_input, name_input,
					gender_input, b_day_input, address_input, phone_input, status_input, pos_input, id_input))
	conn.commit()
	cursor.close()
	conn.close()
	print("Запись успешно обновлена")
	print("Соединение с SQLite закрыто")

def print_data():
	conn = sqlite3.connect(r"HomeWork\HomeWork_8\work.db")
	cursor = conn.cursor()
	print("База сотрудников: ")
	sql = "SELECT * FROM workers"
	cursor.execute(sql)
	print(cursor.fetchall())