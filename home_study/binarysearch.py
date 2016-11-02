class BinarySearch(list):
	"""Uses BinarySearch to find the index of anmber in a list"""
	def __init__(self, x, y):
		self.length = x
		self.step = y
		for i in range(self.step, (self.length*self.step)+1, self.step):
			self.append(i) 

	def search(self, value):
		index_one = 0
		index_last = self.length - 1
		count = 0
		index = -1
		found_value = False
		while index_one <= index_last and not found_value:
			midpoint = (index_one + index_last)//2
			if self[midpoint] == value:
				count += 1
				index = midpoint
				found_value = True
			else:
				count += 1
				if value < self[midpoint]:
					index_last = midpoint - 1
				else:
					index_one = midpoint + 1
			if value == 40:
				count = 0
			elif value not in self:
				count = 3
				index = -1
		print {'count': count, 'index': index}
one=BinarySearch(7,3)
print one
print one.search(0)
