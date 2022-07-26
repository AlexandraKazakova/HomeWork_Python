# Реализуйте RLE алгоритм: реализуйте модуль
# сжатия и восстановления данных.

def coding(message):
	count = 1
	result = ''
	for i in range(len(message)-1):
		if message[i] == message[i+1]:
			count += 1
		else:
			result = result + str(count) + message[i]
			count = 1
	if count > 1 or (message[len(message)-2] != message[-1]):
		result = result + str(count) + message[-1]
	return result


def decoding(message):
	number = ''
	result = ''
	for i in range(len(message)):
		if not message[i].isalpha():
			number += message[i]
		else:
			result = result + message[i] * int(number)
			number = ''
	return result


txt = input("Введите текст -> ")
print(f"Текст после кодировки -> {coding(txt)}")
print(f"Текст после дешифровки -> {decoding(coding(txt))}")
