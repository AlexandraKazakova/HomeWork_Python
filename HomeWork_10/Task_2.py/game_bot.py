import telebot
from telebot import types
from logger import *

bot = telebot.TeleBot("5776440439:AAEkmcqQMY09mONuP4KgE_5Lu2hSV4TszyU", parse_mode=None)

sweet = 2021

@bot.message_handler(commands=['start'])
def start_message(message):
	bot.send_message(message.chat.id, text="""Правила игры:\nНа столе лежит 2021 конфета.\n
				Играют человек против бота, делая ход друг после друга.\n
				Первый ход определяется жеребьёвкой.\n
				За один ход можно забрать не более чем 28 конфет.\n
				Все конфеты оппонента достаются сделавшему последний ход.\n
				Введите /game для начала""")

@bot.message_handler(commands=['game'])

def start_game(message):
	global sweet
	sweet = 2021
	answer = who_the_first()
	if answer == 1:
		bot.send_message(message.chat.id, text = 'Бот ходит первым')
		bot.send_message(message.chat.id, bot_move(sweet))
		sweet -= bot_move(sweet)
		bot.send_message(message.chat.id, text = (f"На столе {sweet} конфет\nВведите количество конфет\n"))
		
	else:
		bot.send_message(message.chat.id, text = (f"Вы ходите первым\nНа столе {sweet} конфет\nВведите количество конфет\n"))

@bot.message_handler(content_types=['text'])

def get_text(message):
	global sweet
	i = int(message.text.lower())
	if i < 1 or i > 28:
		bot.send_message(message.chat.id, text = (f"Количество конфет должно быть от 1 до 28"))
	else:
		sweet -= i
		if sweet < 1:
			bot.send_message(message.chat.id, text = (f"Вы выиграли! Сыграть еще? /game"))
		else:
			bot.send_message(message.chat.id, text = (f"На столе {sweet} конфет"))
			bot.send_message(message.chat.id, bot_move(sweet))
			sweet -= bot_move(sweet)
			if sweet < 1:
				bot.send_message(message.chat.id, text = (f"Бот выиграл! Сыграть еще? /game"))
			else:
				bot.send_message(message.chat.id, text = (f"На столе {sweet} конфет\nВведите количество конфет\n"))



bot.polling(none_stop=True)