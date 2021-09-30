import random

import data

names_count = len(data.names) - 1
surnames_count = len(data.surnames) - 1
streets_num_count = len(data.streets_num) - 1
streets_count = len(data.streets) - 1
city_count = len(data.city) - 1
postcode_count = len(data.postcode) - 1
num_code_count = len(data.num_code) - 1


def identity(count: int = 1):
	"""This function returns random data of people that you can use in your projects."""
	if count > 0:
		while count > 0:
			return '\n' + data.names[random.randint(0, names_count)] + ' ' + data.surnames[random.randint(0, surnames_count)] + '\n' + data.streets_num[random.randint(0, streets_num_count)] + ' ' + data.streets[random.randint(0, surnames_count)] + '\n' + data.city[random.randint(0, city_count)] + ', ' + data.postcode[random.randint(0, postcode_count)] + '\n' +  f'({data.num_code[random.randint(0,num_code_count)]}) xxx-xxxx'
			count = count - 1
	if count < 0:
		print('[ERR] Please write a number greater than 0')
	if count == 0:
		pass
