from objects.data import Node, Linked_list

l = Linked_list()
l.add(10)
l.add(20)
l.add(30)

l.print_list()

l.add_first("Hello")

print()
l.print_list()

print()
l.print_index(30)

print()

if l.remove_data(20) == True:
	l.print_list()

print()
l.print_index(30)