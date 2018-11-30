class Linked_list:
	def __init__(self, head=None):
		self.head = head

	# All of the list handlers: add, add_first, remove_at, remove_data
	def add(self, data):

		# Adds a new node at the END of the linked list 

		node = Node(data)
		if self.head == None:
			self.head = node
		else:
			current = self.head
			while current.get_link() != None:
				current = current.get_link()
			node.prev = current
			current.link = node

	def add_first(self, data):

		# Adds a new node at the HEAD of the linked list 

		node = Node(data, self.head)
		self.head.prev = node
		self.head = node

	def remove_at(self, index):

		# Removes the node at index

		current = self.head
		i = 0
		while i < index:
			current = current.get_link()
			i += 1
		p = current.prev
		n = current.link
		current = None
		del current
		if p == None:
			self.head = n
		else:
			p.link = n

	def remove_data(self, data):

		# Removes node of data's first appearance

		current = self.head
		while current != None:
			if current.data == data:
				break
			current = current.get_link()
		if current != None:
			p = current.prev
			n = current.link
			current = None
			del current
			if p == None:
				self.head = n
			else:
				p.link = n
			return True
		else:
			print("Data doesn't exist")

	# All the ways to output data: print_at, print_index, print_list
	def print_at(self, index):

		# Outputs the value at index

		print("{}".format(self.getvalue(index)))

	def print_index(self, search):

		# Outputs the index of search first appearance

		print("{}".format(self.getindex(search)))

	def print_list(self):

		# Outputs every node of the list

		node = self.head
		while node != None:
			print("{}".format(node.data))
			node = node.link

	# All the ways to return data: getvalue, getindex
	def getvalue(self, index):

		# Returns the data at index

		i = 0
		current = self.head
		while i < index:
			current = current.get_link()
			i += 1
		return current.data

	def getindex(self, search):

		# Return the index of search first appearance

		i = 0
		current = self.head
		while current != None:
			if current.data == search:
				return i
			current = current.get_link()
			i += 1

# Class called Node representing a node of the list
class Node:
	def __init__(self, data=None, link=None, prev=None):
		# Initialize the data and set next and previous to None
		self.data = data
		self.link = link
		self.prev = prev

	def set_data(self, data):
		# Change node's data
		self.data = data

	def set_link(self, link):
		# Change node's link to next
		self.link = link

	def set_prev(self, prev):
		# Change node's link to previous
		self.prev = prev

	def get_data(self):
		return self.data

	def get_link(self):
		return self.link

	def get_prev(self):
		return self.prev
