#AOC2020 day 5
#Validate passport data

from Advent_of_code_2020.AOC_input_handler import InputHandler

def splitter(data, lo, hi):

	'''#debug
	print("lo: {}".format(lo), end=' ')
	print("hi: {}".format(hi), end='\n')
	'''

	split = int(lo + ((hi - lo) / 2))
	current = data.pop(0)

	#lower half
	if current == 'F' or current == 'L':
		if len(data) == 0:
			return lo

		return splitter(data, lo, split)

	#higher half
	elif current == 'B' or current == 'R':
		if len(data) == 0:
			return hi

		return splitter(data, split + 1, hi)


def main():

	f = InputHandler('AOC_5_inputdata.txt')
	f.inputLinesToList()

	highest_id = 0
	my_id = 0
	ids = set()

	#part1
	for d in f.inputData:

		row = splitter(list(d[:7]), 0, 127)
		col = splitter(list(d[7:]), 0, 7)
		seat_id = row * 8 + col
		highest_id = max(highest_id, seat_id)
		ids.add(seat_id)

	'''#part2
	for i in range(min(ids), max(ids)):
		if i not in ids:
			my_id = i
			break
	'''
	#part2 made differently
	my_id = set(range(min(ids), max(ids))).difference(ids)


	print("highest seat ID is: {}".format(highest_id)) #part1
	print("My seat ID is: {}".format(my_id)) #part2



main()