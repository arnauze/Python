from objects.data import Binary_tree, Node

b = Binary_tree()

b.add(2)
b.add(3)

bb = b.head

print(bb.data)
bb = bb.get_right()
print(bb.data)