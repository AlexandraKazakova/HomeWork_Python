from math import pow

def print_operation_table(operation, num_rows = 10, num_columns = 10):
	m = 0
	for i in range(1, num_rows):
		for j in range(1, num_columns):
			m = operation(i, j)
			print(m, end = '	')
		print('')

print_operation_table(lambda x, y: x * y)
print('')
print_operation_table(lambda x, y: x + y)
print('')
print_operation_table(lambda x, y: x ** y, 5, 5)