#AOC2020 day 6
#Log 'Yes' answers

from Advent_of_code_2020.AOC_input_handler import InputHandler
from collections import Counter


def main():

	f = InputHandler('AOC_6_inputdata.txt')
	f.inputToStr()
	f.splitByChar('|')
	f.splitByChar(' ') #part2

	data = f.inputData

	'''#part1
	processedData = []
	for d in data:
		newstring = d.replace(' ', '')
		processedData.append(set(newstring))

	yesCount = 0
	for p in processedData:
		yesCount += len(p)
	'''

	#part2
	for i, d in enumerate(data):

		if isinstance(d, str):
			data[i] = [d]

	count = 0
	for d in data:
		counts = {}
		for e in d:
			counts.update({k: 0 for k in e})	

		for l in counts.keys():
			counts[l] = sum([x.count(l) for x in d])
			if counts[l] == len(d):
				count += 1

		#print(counts)
		
	#print("Amount of 'Yes' answers: {}".format(yesCount)) #part1
	print("Amount of 'Yes' answers by everyone: {}".format(count)) #part2


main()