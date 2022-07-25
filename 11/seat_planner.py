#AOC2020 day 11
#Simulate people finding seats based on certain rules. After simulation stabilizes, find amount of occupied seats
#P2 same but with different rules


from Advent_of_code_2020.AOC_input_handler import InputHandler
import pprint
import copy


def vectorAdd(a, b):

	x = a[0] + b[0]
	y = a[1] + b[1]

	return (x, y)

def movePos(data, pos, direction):

	while True:
		#print(data[pos[1]][pos[0]])
		newpos = vectorAdd(pos, direction)

		if any(x < 0 for x in newpos):
			return None	
		else:
			pos = newpos

		if data[pos[1]][pos[0]] != '.':
			return pos

#P1
def getAdjacentP1(data, currentPos):

	directions = [	(-1, -1), 	(0, -1), 	(1, -1),
					(-1, 0),				(1, 0),
					(-1, 1), 	(0, 1), 	(1, 1),
					]

	adjacent = []
	for d in directions:

		try: 
			pos = vectorAdd(currentPos, d)
			if not any(x < 0 for x in pos):
				adj = data[pos[1]][pos[0]]

				if adj != '.':
					adjacent.append(adj)

		except IndexError:
					continue

	return adjacent

#P2
def getAdjacentP2(data, currentPos):

	directions = [	(-1, -1), 	(0, -1), 	(1, -1),
					(-1, 0),				(1, 0),
					(-1, 1), 	(0, 1), 	(1, 1),
					]

	adjacent = []
	for d in directions:

		try: 
			pos = movePos(data, currentPos, d)
			if pos is not None:
				adj = data[pos[1]][pos[0]]
				adjacent.append(adj)

		except IndexError:
					continue

	return adjacent

def update(data):

	newdata = copy.deepcopy(data)

	for y, row in enumerate(data):
		for x, seat in enumerate(row):

			#adjacent = getAdjacentP1(data, (x, y))#P1
			adjacent = getAdjacentP2(data, (x, y))#P2

			noAdjacent = all([x == 'L' for x in adjacent])
			tooManyOccupiedP1 = len([x for x in adjacent if x == '#']) >= 4
			tooManyOccupiedP2 = len([x for x in adjacent if x == '#']) >= 5

			if seat == 'L' and noAdjacent:
				newdata[y][x] = '#'

			elif seat == '#' and tooManyOccupiedP2:
				newdata[y][x] = 'L'

			else:
				continue

	return newdata



def main():

	f = InputHandler('AOC_11_inputdata.txt')
	f.inputLinesToList()

	data = [list(s) for s in f.inputData]


	while True:

		prevdata = copy.deepcopy(data)
		data = update(data)

		if prevdata == data:
			break
	'''
	data = update(data)
	data = update(data)
	pprint.pprint(data)
	'''

	count = 0
	for y in data:
		for x in y:
			if x == '#':
				count += 1

	print('{} seats end up occupied'.format(count))


main()