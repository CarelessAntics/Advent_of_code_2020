#AOC2020 day 4
#Validate passport data

import re
from Advent_of_code_2020.AOC_input_handler import InputHandler


def valYear(value, minY, maxY):

	return int(value) >= minY and int(value) <= maxY


def valHeight(value):

	if value[-2:] == 'cm':
		return int(value[:-2]) >= 150 and int(value[:-2]) <= 193
	elif value[-2:] == 'in':
		return int(value[:-2]) >= 59 and int(value[:-2]) <= 76
	return False


def valHairColor(value):

	if len(value) == 7 and value[0] == '#' and re.match(r'[0-9a-fA-F]{6}', value[1:]):
		return True
	return False


def valEyeColor(value):

	colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
	return value in colors


def valID(value):

	if re.match(r'[0-9]{9}', value) and len(value) == 9:
		return True
	return False


def validator(values):

	return all([valYear(values['byr'], 1920, 2002),
				valYear(values['iyr'], 2010, 2020),
				valYear(values['eyr'], 2020, 2030),
				valHeight(values['hgt']),
				valHairColor(values['hcl']),
				valEyeColor(values['ecl']),
				valID(values['pid'])
				])



def main():

	f = InputHandler('AOC_4_inputdata.txt')
	f.inputToStr()
	f.splitByChar('|')
	f.splitByChar(' ')
	#print(f.inputData)

	passports = []

	for d in f.inputData:
		passports.append({x.split(':')[0]:x.split(':')[1] for x in d})

	validation = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
	validated = 0

	''' #part1
	for p in passports:
		if all([x in p.keys() for x in validation]):
			validated += 1
	'''

	#part2
	for p in passports:
		if all([x in p.keys() for x in validation]):
			if validator(p):
				validated += 1

	print("Valid passwords: {}".format(validated))



main()