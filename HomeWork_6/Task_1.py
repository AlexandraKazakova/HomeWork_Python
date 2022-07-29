# Мимикрия
global transformation

transformation = lambda y: 1 * y
values = [2,323,4,5,'abc',7,8, 'wjf', -3, 0]
transformed_values = list(map(transformation, values))
if values == transformed_values:
	print('OK')
else:
	print('NO')

print(transformed_values)