import sqlite3
from data_create import *
from tele_bot import *

def input_data(surname, name, phone):
	conn = sqlite3.connect(r"HomeWork\HomeWork_10\Task_1.py\tele.db")
	cursor = conn.cursor()
	print("Подключен к SQLite")
	
	surname_input = surname
	name_input = name
	phone_input = phone
	cursor.execute("""CREATE TABLE IF NOT EXISTS telephone
				(person_id INTEGER PRIMARY KEY AUTOINCREMENT, surname TEXT NOT NULL, name TEXT NOT NULL, phone TEXT NOT NULL)""")
	cursor.execute("""INSERT INTO telephone (surname, name, phone)
				VALUES (?, ?, ?)""", (surname_input, name_input, phone_input))
	conn.commit()
	cursor.close()
	conn.close()
	print('Данные сохранены')
	print("Соединение с SQLite закрыто")

def delete_data(surname, name):
	conn = sqlite3.connect(r'HomeWork\HomeWork_10\Task_1.py\tele.db')
	cursor = conn.cursor()
	print("Подключен к SQLite")
	surname_del = surname
	name_del = name
	cursor.execute("DELETE from telephone where surname = ? AND name = ?", (surname_del, name_del))
	conn.commit()
	print("Запись успешно удалена")
	cursor.close()
	conn.close()
	print("Соединение с SQLite закрыто")

def find_data(surname, name):
	conn = sqlite3.connect(r'HomeWork\HomeWork_10\Task_1.py\tele.db')
	cursor = conn.cursor()
	print("Подключен к SQLite")
	surname_find = surname
	name_find = name
	cursor.execute("SELECT * FROM telephone WHERE surname LIKE ? AND name LIKE ?",('%' + surname_find + '%', '%' + name_find + '%'))
	result = cursor.fetchall()
	s = ' '.join(map(str,result))
	cursor.close()
	conn.close()
	print("Соединение с SQLite закрыто")
	return(s)


def change_data(surname, new_s, name, new_n, new_p):
	conn = sqlite3.connect(r'HomeWork\HomeWork_10\Task_1.py\tele.db')
	cursor = conn.cursor()
	print("Подключен к SQLite")
	surname_update = surname
	name_update = name
	phone_input = new_p
	surname_input = new_s
	name_input = new_n
	cursor.execute("""UPDATE telephone set phone = ?, name = ?, surname = ?
					WHERE surname = ? AND name = ?""", (phone_input, name_input, surname_input, surname_update, name_update))
	conn.commit()
	cursor.close()
	conn.close()
	print("Запись успешно обновлена")
	print("Соединение с SQLite закрыто")

def print_data():
	conn = sqlite3.connect(r"HomeWork\HomeWork_10\Task_1.py\tele.db")
	cursor = conn.cursor()
	print("Телефонная книга: ")
	sql = "SELECT * FROM telephone"
	cursor.execute(sql)
	result = cursor.fetchall()
	s = ' '.join(map(str, result))
	cursor.close()
	conn.close()
	print("Соединение с SQLite закрыто")
	return(s)
