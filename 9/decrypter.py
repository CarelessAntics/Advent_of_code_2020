#AOC2020 day 8
#Process input code and find the loop
#Part2: fix the loop by changing a single operation

from Advent_of_code_2020.AOC_input_handler import InputHandler

def isPreviousSum(data):

	for i in range(len(data)-1):
		for j in range(i+1, len(data)-1):

			if data[-1] == data[i] + data[j]:
				return True

	return False

def findIncorrect(data, size):

	invalidNum = None

	for i in range(size,len(data)):

		if not isPreviousSum(data[i-size : i+1]):
			#return data[i] #uncomment for part1

			invalidNum = data[i]

			#part2:
			for j, d in enumerate(data[:i]):

				encryptSum = 0
				sumNums = []

				for k in data[j:i]:

					encryptSum += k
					sumNums.append(k)

					if encryptSum > invalidNum:
						break

					elif encryptSum == invalidNum:
						return sumNums
	
	return None

	

def main():

	#Make data into dictionaries, where key = color and value = list of bags and amounts contained in the bag
	f = InputHandler('AOC_9_inputdata.txt')
	f.inputLinesToList()
	f.stringNumeralsToInt()

	data = f.inputData

	'''#part1
	P1_answer = findIncorrect(data, 25)

	print("First number without a previous sum is {}".format(P1_answer))
	'''

	#part2
	contiguousSum = findIncorrect(data, 25)
	P2_answer = max(contiguousSum) + min(contiguousSum)
	print(contiguousSum)
	print("The sum of min and max is {}".format(P2_answer))
	


main()