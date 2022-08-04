import csv

def export_data():
	with open("HomeWork\HomeWork_7\Example.csv", encoding='utf-8') as r_file:
		headersCSV = ['Surname', 'Name', 'Phone', 'Comment']
		file_reader = csv.DictReader(r_file, delimiter = ";", fieldnames = headersCSV, dialect='excel')
		for row in file_reader:
			print(row['Surname'], row['Name'], row['Phone'], row['Comment'], sep = ', ')

def export_data_2():
	with open("HomeWork\HomeWork_7\Example.csv", encoding='utf-8') as r_file:
		headersCSV = ['Surname', 'Name', 'Phone', 'Comment']
		file_reader = csv.DictReader(r_file, delimiter = ";", fieldnames = headersCSV, dialect='excel')
		for row in file_reader:
			print(row['Surname'], row['Name'], row['Phone'], row['Comment'], sep = '\n')