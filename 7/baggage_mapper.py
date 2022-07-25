#AOC2020 day 7
#Find out how many different bags can contain a single bag
#P2: Find out how many total bags can the bag contain

from Advent_of_code_2020.AOC_input_handler import InputHandler
import re

#part1
#Take dict input. Recursively crawl backwards through the bag colors depending on which bags contain the current color.
#Return a set of bag colors crawled through
def bagMapper(rules, current, bags):

	for k, v in rules.items():
		if any(current in s for s in v):
			bagMapper(rules, k, bags)
			bags.add(k)


#part2
#Take dict input. Crawl recursively forwards through the bags and count the amount of total bags contained within the root
def bagCounter(rules, current):

	count = 0

	if 'no other bag' in rules[current]:
		return count

	for d in rules[current]:
		amount = re.search(r'[0-9]*', d).group(0)
		count += int(amount) * (1 + bagCounter(rules, d.replace(amount + ' ', ''))) 

	return count


def main():

	#Make data into dictionaries, where key = color and value = list of bags and amounts contained in the bag
	f = InputHandler('AOC_7_inputdata.txt')
	f.inputLinesToList()
	f.removeChars('.')
	f.splitByChar(' contain ')
	f.splitByChar(', ')
	f.removeChars('s', endOnly = True)

	data = f.inputData

	rules = {d[0]: d[1] for d in data}
	for k, v in rules.items(): #some values are still strings. Make them into lists
		if not isinstance(v, list):
			rules[k] = [v]

	'''#part1
	bags = set()
	bagMapper(rules, 'shiny gold bag', bags)
	print("amount of bag colors capable of holding a shiny gold bag is {}".format(len(bags)))
	'''

	#part2
	count = bagCounter(rules, 'shiny gold bag')
	print("amount of bags capable of being held in a shiny gold bag is {}".format(count))



main()