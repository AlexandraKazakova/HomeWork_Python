# Задана последовательность натуральных чисел,
# завершающаяся числом 0. Требуется определить
# значение второго по величине элемента в этой
# последовательности, то есть элемента, который
# будет наибольшим, если из последовательности удалить
# наибольший элемент.

numbers = map(int, input('Введите последовательность чисел ').split())
numbers = list(numbers)

def find_max(arr):
	max_number = arr[0]
	for i in arr:
		if i > max_number:
			max_number = i
	return max_number

new_numbers = numbers.copy()
new_numbers.remove(find_max(numbers))

print(find_max(new_numbers))