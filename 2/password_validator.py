#AOC2020 day 2
#Find valid passwords. 
#Part1: valid passwords must have a certain amount within range of a specific character
#Part2: range in input is instead position indices. The specific character must be found in ONE index

from Advent_of_code_2020.AOC_input_handler import InputHandler


def checkValidityP1(minc, maxc, c, password):

	return password.count(c) >= minc and password.count(c) <= maxc

def checkValidityP2(pos, c, password):

	#Basically XOR
	check1 = bool(password[pos[0] - 1] == c)
	check2 = bool(password[pos[1] - 1] == c)

	return check1 != check2

def main():

	#prepare input
	f = InputHandler('AOC_2_inputdata.txt')
	f.inputLinesToList()
	f.splitByChar(':')
	f.removeChars(' ')
	f.splitByChar(' ')
	f.splitByChar('-')
	

	validcount = 0
	for d in f.inputData:
		minc = int(d[0][0][0])
		maxc = int(d[0][0][1])
		pos = (minc, maxc)
		c = d[0][1]
		password = d[1]

		''' #part1
		if checkValidityP1(minc, maxc, c, password):
			validcount += 1
		'''

		#part2
		if checkValidityP2(pos, c, password):
			validcount += 1

	print(validcount)

main()