# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока
# делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. Все конфеты
# оппонента достаются сделавшему последний ход. Сколько конфет
# нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) (доп) Подумайте как наделить бота ""интеллектом""

from random import randint

def faceToFace():
	name_1 = input('Введите свое имя - > ')
	name_2 = input('Введите свое имя - > ')

	n = randint(1, 2)
	sweet = 2021
	count = 0

	if n == 1:
		theFirst = name_1
		theSecond = name_2
	else:
		theFirst = name_2
		theSecond = name_1

	print(f'Правила игры:\nНа столе лежит 2021 конфета.\n'
				'Играют два игрока, делая ход друг после друга. \n'
				'Первый ход определяется жеребьёвкой.\n'
				'За один ход можно забрать не более чем 28 конфет.\n'
				'Все конфеты оппонента достаются сделавшему последний ход.\n')

	print(f'Игрок {theFirst} будет ходить первым')

	while sweet > 0:
		if count == 0:
			sw = int(input(f'Введите количество конфет, {theFirst} -> '))
			while 1 > sw > 28:
				sw = int(input(f'За 1 ход можно забрать только 28 конфет, {theFirst} -> '))
			sweet -= sw
			print(f'На столе {sweet} конфет')
			count = 1
		if count == 1:
			sw = int(input(f'Введите количество конфет, {theSecond} -> '))
			while 1 > sw > 28:
				sw = int(input(f'За 1 ход можно забрать только 28 конфет, {theSecond} -> '))
			sweet -= sw
			print(f'На столе {sweet} конфет')
			count = 0
	if count == 0:
		print(f'{theSecond} выииграл - Поздравляем!')
	if count == 1:
		print(f'{theFirst} выииграл - Поздравляем!')

def withBot():
	name = input('Введите свое имя - > ')

	n = randint(1, 2)
	sweet = 2021
	count = 0

	if n == 1:
		theFirst = name
		theSecond = 'Bot'
	else:
		theFirst = 'Bot'
		theSecond = name

	print(f'Правила игры:\nНа столе лежит 2021 конфета.\n'
				'Играют игрок против компьютера, делая ход друг после друга. \n'
				'Первый ход определяется жеребьёвкой.\n'
				'За один ход можно забрать не более чем 28 конфет.\n'
				'Все конфеты оппонента достаются сделавшему последний ход.\n')

	print(f'Игрок {theFirst} будет ходить первым')
	if theFirst == name:
		while sweet > 0:
			if count == 0:
				sw = int(input(f'Введите количество конфет, {theFirst} -> '))
				while 1 > sw > 28:
					sw = int(input(f'За 1 ход можно забрать только 28 конфет, {theFirst} -> '))
				sweet -= sw
				print(f'На столе {sweet} конфет')
				count = 1
			if count == 1:
				sw = randint(1,28)
				print('Bot -', sw)
				sweet -= sw
				print(f'На столе {sweet} конфет')
				count = 0
		if count == 0:
			print(f'{theSecond} выииграл - Поздравляем!')
		if count == 1:
			print(f'{theFirst} выииграл - Поздравляем!')
	elif theSecond == name:
		while sweet > 0:
			if count == 0:
				sw = randint(1,28)
				print('Bot -', sw)
				sweet -= sw
				print(f'На столе {sweet} конфет')
				count = 1
			if count == 1:
				sw = int(input(f'Введите количество конфет, {theSecond} -> '))
				while 1 > sw > 28:
					sw = int(input(f'За 1 ход можно забрать только 28 конфет, {theSecond} -> '))
				sweet -= sw
				print(f'На столе {sweet} конфет')
				count = 0
		if count == 0:
			print(f'{theSecond} выииграл - Поздравляем!')
		if count == 1:
			print(f'{theFirst} выииграл - Поздравляем!')

def smatBot():
	name = input('Введите свое имя - > ')

	n = randint(1, 2)
	sweet = 2021
	count = 0
	maxSw = 28

	if n == 1:
		theFirst = name
		theSecond = 'SmartBot'
	else:
		theFirst = 'SmartBot'
		theSecond = name

	print(f'Правила игры:\nНа столе лежит 2021 конфета.\n'
				'Играют игрок против компьютера, делая ход друг после друга. \n'
				'Первый ход определяется жеребьёвкой.\n'
				'За один ход можно забрать не более чем 28 конфет.\n'
				'Все конфеты оппонента достаются сделавшему последний ход.\n')

	print(f'Игрок {theFirst} будет ходить первым')
	if theFirst == name:
		while sweet > 0:
			if count == 0:
				sw = int(input(f'Введите количество конфет, {theFirst} -> '))
				while 1 > sw > 28:
					sw = int(input(f'За 1 ход можно забрать только 28 конфет, {theFirst} -> '))
				sweet -= sw
				print(f'На столе {sweet} конфет')
				count = 1
			if count == 1:
				if sweet > maxSw * 2:
					sw = maxSw
					print('SmartBot -', sw)
					sweet -= sw
					print(f'На столе {sweet} конфет')
					count = 0
				elif maxSw < sweet <= maxSw * 2:
					if sweet == 29:
						sw = 1
					else:
						sw = sweet - (maxSw + 1)
					print('SmartBot -', sw)
					sweet -= sw
					print(f'На столе {sweet} конфет')
					count = 0
				elif 0 < sweet <= maxSw:
					sw = sweet
					print('SmartBot -', sw)
					sweet -= sw
					print(sweet)
					print(f'SmartBot победил!')
					return
		if count == 1:
			print(f'{theFirst} выиграл - Поздравляем!')
	if theSecond == name:
		while sweet > 0:
			if count == 0:
				if sweet > maxSw * 2:
					sw = maxSw
					print('SmartBot -', sw)
					sweet -= sw
					print(f'На столе {sweet} конфет')
					count = 1
				elif maxSw < sweet <= maxSw * 2:
					if sweet == 29:
						sw = 1
					else:
						sw = sweet - (maxSw + 1)
					print('SmartBot -', sw)
					sweet -= sw
					print(f'На столе {sweet} конфет')
					count = 1
				elif 0 < sweet <= maxSw:
					sw = sweet
					print('SmartBot -', sw)
					sweet -= sw
					print(sweet)
					print(f'SmartBot победил!')
					return
			if count == 1:
				sw = int(input(f'Введите количество конфет, {theSecond} -> '))
				while 1 > sw > 28:
					sw = int(input(f'За 1 ход можно забрать только 28 конфет, {theSecond} -> '))
				sweet -= sw
				print(f'На столе {sweet} конфет')
				count = 0
		if count == 0:
			print(f'{theSecond} выииграл - Поздравляем!')


choiceGame = int(input('Введите 1, если хотите играть вдвоем\n'
											'Введите 2, если хотите играть против компьютера\n'
											'Введите 3, если хотите играть против умного компьютера\n'))

while choiceGame != 1 and choiceGame != 2 and choiceGame != 3:
	choiceGame = int(input('Введите 1, если хотите играть вдвоем\n'
												'Введите 2, если хотите играть против компьютера\n'
												'Введите 3, если хотите играть против умного компьютера\n'))

if choiceGame == 1:
	faceToFace()
if choiceGame == 2:
	withBot()
if choiceGame == 3:
	smatBot()

