class Binary_tree:
	def __init__(self, head=None):
		self.head = head

	def add(self, data):
		node = Node(data)
		current = self.head
		if self.head == None:
			self.head = node
		else:
			while current != None:
				if current.data <= data:
					current = current.get_right()
				else:
					current = current.get_left()
				current = node


class Node:
	def __init__(self, data=None, right=None, left=None):
		self.data = data
		self.right = right
		self.left = left

	def set_right(self, data):
		self.right = data

	def set_left(self, data):
		self.left = data

	def set_data(self, data):
		self.data = data

	def get_right(self):
		return self.right

	def get_left(self):
		return self.left

	def get_data(self):
		return self.data
