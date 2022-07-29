from collections import Counter
poem = input('Введите стихотворение -> ')
poem_arr = []
letters = ['а', 'о', 'у', 'ё', 'е', 'ы', 'э', 'я', 'ю']

for word in poem.split(' '):
	poem_arr.append(word)

sum = 0
count_arr = []

for i in range(len(poem_arr)):
	counter = Counter(poem_arr[i])
	for j in letters:
		if j in counter:
			sum += counter[j]
	count_arr.append(sum)
	sum = 0

def pamParam(arr):
	for n in range(len(arr) - 1):
		if arr[n] != arr[n + 1]:
			return 'Пам парам'
		if n == len(count_arr) - 2:
			return 'Парам пам-пам'

print(poem_arr)
print(count_arr)
print(pamParam(count_arr))

# пам-пам-пам паропапум пам-пам-пам пэрапапам пам

