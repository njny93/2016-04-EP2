import bst

tree = bst.create(2)
bst.add(tree, 6)
bst.add(tree, 7)
bst.add(tree, 2)
bst.add(tree, 5)
bst.add(tree, 3)
bst.add(tree, 8)
bst.add(tree, 9)

print(bst.find(5))
