class Linked_list:
	def __init__(self, head=None):
		self.head = head

	def add(self, data):
		node = Node(data)
		if self.head == None:
			self.add_first(data)
		else:
			current = self.head
			while current.get_link() != None:
				current = current.get_link()
			current.link = node
			tmp = node
			current = current.link
			current.prev = node
			current.prev.link = current

	def add_first(self, data):
		node = Node(data, self.head)
		self.head = node

	def print(self):
		node = self.head
		while node != None:
			print("{}".format(node.data))
			node = node.link

class Node:
	def __init__(self, data=None, link=None, prev=None):
		self.data = data
		self.link = link
		self.prev = prev

	def set_data(self, data):
		self.data = data

	def set_link(self, link):
		self.link = link

	def set_prev(self, prev):
		self.prev = prev

	def get_data(self):
		return self.data

	def get_link(self):
		return self.link

	def get_prev(self):
		return self.prev
