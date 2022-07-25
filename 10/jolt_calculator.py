#AOC2020 day 10
#Adapters have different joltage tolerances. Chain adapters together in multiple ways and count the differences
#P2 count how many different ways the adapters can be chained together

from Advent_of_code_2020.AOC_input_handler import InputHandler


def splitData(data):

	newdata = []
	subdata = []
	for i, d, in enumerate(data):

		if d != data[-1]:
			if data[i + 1] - d < 3:
				subdata.append(d)
			else:
				subdata.append(d)
				newdata.append(subdata)
				subdata = []
		else:
			if d - data[i - 1] < 3:
				subdata.append(d)
			else:
				subdata.append(d)
				newdata.append(subdata)
				subdata = []

	if subdata:
		newdata.append(subdata)
	#print(max([len(x) for x in newdata]))
	return newdata


#Split the data into groups separated by gaps of 3. 
#Recursively calculate the combinations for each group and multiply them together to get the total
def countCombinationsP2(data):

	count = 1
	for i, d in enumerate(data):

		#groups of size 1 or 2 have only one possible arrangement
		if len(d) > 2:
			count *= get_combination_count(d, d[0], 0)

	return count

		
def get_combination_count(d, current, count):

	if current < max(d):

		closest = range(current + 1, current + 4)
		#print(current, end=' | ')
		#print(list(closest), end=' \n ')
		for x in closest:
			if x in d:
				count = get_combination_count(d, x, count)
	else:
		return count + 1

	return count

		


def connectAdaptersP1(data, currentJolt, maxJolts, differences):


	if currentJolt < maxJolts - 3:

		closestJolts = {x - currentJolt : x for x in data if x - currentJolt <= 3 and x - currentJolt > 0}
		minJolts = min(closestJolts.keys())
		differences[minJolts] += 1
		
		connectAdapters(data, closestJolts[minJolts], maxJolts, differences)

	#End is reached. Last connection is always 3 jolts higher
	else:
		differences[3] += 1




def main():

	f = InputHandler('AOC_10_inputdata.txt')
	f.inputLinesToList()
	f.stringNumeralsToInt()

	data = f.inputData
	data.append(0) #It is important for P2 to have 0 in the data
	data.sort()

	differences = {1:0, 2:0, 3:0}
	maxJolts = max(data) + 3

	'''#P1
	connectAdapters(data, 0, maxJolts, differences, 0)

	P1_ans = differences[1] * differences[3]
	print("1-jolt differences multiplied by 3-jolt differences is {}".format(P1_ans))
	'''

	#P2
	dataP2 = splitData(data)
	P2_ans = countCombinationsP2(dataP2)
	print("all possible connections count: {}".format(P2_ans))



main()