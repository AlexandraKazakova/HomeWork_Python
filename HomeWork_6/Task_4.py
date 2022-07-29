# Все равны
values = [14, 34, 24, 0]

def same_by(characteristic, objects):
	for i in range(len(objects) - 1):
		if characteristic(objects[i]) != characteristic(objects[i + 1]):
			return False
	return True

if same_by(lambda x: x % 2, values):
	print('same')
else:
	print('different')