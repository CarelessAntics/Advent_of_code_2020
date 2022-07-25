#AOC2020 day 3
#

from Advent_of_code_2020.AOC_input_handler import InputHandler



def vectorAdd(a, b):

	x = a[0] + b[0]
	y = a[1] + b[1]

	return [x, y]

def vectorModuloX(a, modx):

	x = a[0] % modx
	y = a[1]

	return [x, y]

def slopeMapper(mapData, vel):

	width = len(mapData[0])
	height = len(mapData)
	pos = [0, 0]
	trees = 0

	while pos[1] < height:

		if mapData[pos[1]][pos[0]] == '#':
			trees += 1

		pos = vectorAdd(pos, vel)
		pos = vectorModuloX(pos, width)

	return trees

def main():

	f = InputHandler('AOC_3_inputdata.txt')
	f.inputLinesToList()
	data = f.inputData
	#slopes = [[3, 1]] #part1
	slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]] #part2
	mult = 1

	for s in slopes:
		trees = slopeMapper(data, s)
		print(trees)
		mult *= trees

	print('Answer is: {}'.format(mult))



main()