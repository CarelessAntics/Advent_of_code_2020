#AOC input handler
import re

class InputHandler():

	def __init__(self, file):

		self.file = file
		self.inputData = []


	def checkData(self, data):

		if data is None:
			return self.inputData
		else:
			return data

	def inputLinesToList(self):

		with open(self.file, 'r') as f:
			self.inputData = f.read().splitlines()


	def inputToStr(self):

		with open(self.file, 'r') as f:
			self.inputData = f.read().replace('\n\n', '|').replace('\n', ' ')


	def dataToInt(self):

		self.inputData = [int(d) for d in self.inputData]


	#Delete characters from start and end of string only
	def removeChars(self, c, data = None, endOnly = False, startOnly = False):

		data = self.checkData(data)

		for i, d in enumerate(data):

			if isinstance(d, list):
				data[i] = self.removeChars(c, d, endOnly, startOnly)

			#Character removal happens here
			elif isinstance(d, str):
				if not endOnly:
					while data[i][0] == c:
						data[i] = data[i][1:]

				if not startOnly:
					while data[i][-1] == c:
						data[i] = data[i][:-1]

		return data


	#Splits every found string by character
	def splitByChar(self, c, data = None, root = True):

		data = self.checkData(data)

		if not isinstance(data, list):
			data = [data]

		for i, d in enumerate(data):
			
			if isinstance(d, str) and c in d:
				entry = d.split(c)
				data[i] = entry

			elif isinstance(d, list):
				data[i] = self.splitByChar(c, d, False)

		if root and len(data) == 1:
			self.inputData = data[0]

		return data


	def stringNumeralsToInt(self, data = None):

		data = self.checkData(data)

		for i, d in enumerate(data):
			
			if isinstance(d, str): 
				#print(len(re.search(r'([+\-]?[0-9]*)', d).group(0)) > 0)
				if len(re.search(r'([+\-]?[0-9]*)', d).group(0)) > 0:
					data[i] = int(d)

			elif isinstance(d, list):
				data[i] = self.stringNumeralsToInt(d)

		return data
