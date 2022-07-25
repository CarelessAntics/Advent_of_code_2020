#AOC2020 day 8
#Process input code and find the loop
#Part2: fix the loop by changing a single operation

from Advent_of_code_2020.AOC_input_handler import InputHandler

class LoopError(Exception):
	pass

def processCode(code):

	index = 0
	accumulator = 0
	visited = set()

	while True:

		#If an index is already visited, code is in an infinite loop
		if index in visited:
			#print("Infinite loop detected") #part1
			#print("Accumulator reads: {}".format(accumulator))
			raise LoopError
			break

		#Code processed successfully if index goes out of bounds
		if index >= len(code):
			print("Program terminated succesfully")
			print("Accumulator reads: {}".format(accumulator))
			break

		#No operation. Move to next index
		if code[index][0] == 'nop':
			visited.add(index)
			index += 1

		#Accumulate. Add or subtract from accumulator variable
		elif code[index][0] == 'acc':
			visited.add(index)
			accumulator += code[index][1]
			index += 1

		#Move to a different point in code
		elif code[index][0] == 'jmp':
			visited.add(index)
			index += code[index][1]



def main():

	#Make data into dictionaries, where key = color and value = list of bags and amounts contained in the bag
	f = InputHandler('AOC_8_inputdata.txt')
	f.inputLinesToList()
	f.splitByChar(' ')
	f.stringNumeralsToInt()

	data = f.inputData

	#part1
	#processCode(data)

	#part2
	#Go through orders one by one, switch them, and try processing the code
	#If an error is raised, try the next one
	for i, d in enumerate(data):
		if d[0] == 'nop':
			try:
				data[i][0] = 'jmp'
				processCode(data)
				break
			except LoopError:
				data[i][0] = 'nop'
				continue

		elif d[0] == 'jmp':
			try:
				data[i][0] = 'nop'
				processCode(data)
				break
			except LoopError:
				data[i][0] = 'jmp'
				continue




main()