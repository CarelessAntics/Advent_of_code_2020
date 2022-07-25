#AOC2020 day 1
#Find 2(3) numbers from input that add up to 2020, and multiply them together

from Advent_of_code_2020.AOC_input_handler import InputHandler


#Test each number by adding them together. 
# To reduce processing time, only add numbers that come after the current number, as previous ones have already been tested
def find2020(data):

	for i,d in enumerate(data):
		for j in range(i+1, len(data)):

			if d + data[j] == 2020:
				return (d, data[j])
			else:
				continue

#2nd part. same as 1st but add a loop
def findThree2020(data):

	for i,d in enumerate(data):
		for j in range(i+1, len(data)):
			for k in range(j+1, len(data)):

				if d + data[j] + data[k] == 2020:
					return (d, data[j], data[k])
				else:
					continue


def main():

	f = InputHandler('AOC_1_inputdata.txt')
	f.inputLinesToList()
	f.dataToInt()

	#a = find2020(f.inputData) #1st part
	a = findThree2020(f.inputData) #2nd part

	#ans = a[0] * a[1] #1st part
	ans = a[0] * a[1] * a[2] #2nd part

	#print("answer is: " + str(a[0]) + ' * ' + str(a[1]) + ' = ' + str(ans)) #1st part
	print("answer is: " + str(a[0]) + ' * ' + str(a[1]) + ' * ' + str(a[2]) + ' = ' + str(ans)) #2nd part

main()