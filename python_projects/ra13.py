import random

def rand13():
	for i in range(0, 14): 
		# print i
		num = random.randint(0, 53)
		# print num
		array = []
		array.append(num)
		# print array
		return array

def two_el():
		# print rand13(), rand13()
		return rand13(), rand13()
