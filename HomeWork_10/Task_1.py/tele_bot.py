import telebot
from logger import *

surname = ''
name = ''
phone = ''

new_s = ''
new_n = ''
new_p = ''

bot = telebot.TeleBot("5427888305:AAHAEe-tJzNd7Vx3PK11HpiQ12i61vsAadE", parse_mode=None)

@bot.message_handler(commands=['start'])

def start(message):
	bot.send_message(message.chat.id, "Привет, это бот-телефонная книга!\nНажмите /menu, чтобы выбрать действие")

@bot.message_handler(commands=['menu'])

def menu(message):
	bot.send_message(message.chat.id,'Здравствуйте! Что необходимо сделать?\n'
			'/input - Внести данные в телефонную книгу\n'
			'/delete - Удалить данные из телефонной книги\n'
			'/change - Внести изменения в телефонную книгу\n'
			'/find - Найти информацию в телефонной книге\n'
			'/output - Вывести всю телефонную книгу\n')

@bot.message_handler(commands=['input'])

def input_(message):
	bot.send_message(message.chat.id, 'Введите фамилию')
	bot.register_next_step_handler(message, input_surname)

def input_surname(message):
	global surname
	surname = message.text
	bot.send_message(message.chat.id, 'Введите имя')
	bot.register_next_step_handler(message, input_name)


def input_name(message):
	global name
	name = message.text
	bot.send_message(message.chat.id, 'Введите номер телефона')
	bot.register_next_step_handler(message, input_phone)

def input_phone(message):
	global phone
	phone = message.text
	input_data(surname, name, phone)
	bot.send_message(message.chat.id, 'Данные сохранены')

@bot.message_handler(commands=['delete'])

def delete_(message):
	bot.send_message(message.chat.id, 'Введите фамилию')
	bot.register_next_step_handler(message, delete_surname)

def delete_surname(message):
	global surname
	surname = message.text
	bot.send_message(message.chat.id, 'Введите имя')
	bot.register_next_step_handler(message, delete_name)

def delete_name(message):
	global name
	name = message.text
	delete_data(surname, name)
	bot.send_message(message.chat.id, 'Данные удалены')

@bot.message_handler(commands=['change'])

def change_(message):
	bot.send_message(message.chat.id, 'Введите фамилию контакта, который хотите изменить')
	bot.register_next_step_handler(message, change_surname)

def change_surname(message):
	global surname
	surname = message.text
	bot.send_message(message.chat.id, 'Введите имя контакта, который хотите изменить')
	bot.register_next_step_handler(message, change_name)

def change_name(message):
	global name
	name = message.text
	bot.send_message(message.chat.id, 'Введите новую фамилию')
	bot.register_next_step_handler(message, new_surname)

def new_surname(message):
	global new_s
	name = message.text
	bot.send_message(message.chat.id, 'Введите новое имя')
	bot.register_next_step_handler(message, new_name)

def new_name(message):
	global new_n
	new_n = message.text
	bot.send_message(message.chat.id, 'Введите новый номер телефона')
	bot.register_next_step_handler(message, change_phone)

def change_phone(message):
	global new_p
	new_p = message.text
	change_data(surname, new_s, name, new_n, new_p)
	bot.send_message(message.chat.id, 'Данные изменены')

@bot.message_handler(commands=['find'])

def find_(message):
	bot.send_message(message.chat.id, 'Введите фамилию')
	bot.register_next_step_handler(message, find_surname)

def find_surname(message):
	global surname
	surname = message.text
	bot.send_message(message.chat.id, 'Введите имя')
	bot.register_next_step_handler(message, find_name)

def find_name(message):
	global name
	name = message.text
	bot.send_message(message.chat.id, find_data(surname, name))

@bot.message_handler(commands=['output'])

def output_phone(message):
	bot.send_message(message.chat.id, print_data())


if __name__ == "__main__":
	bot.infinity_polling()
