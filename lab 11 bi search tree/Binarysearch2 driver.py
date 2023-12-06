import BinarySearch2

bst = BinarySearch2.BSTree2()
bst.insert('gemma')
bst.insert('margaux')
bst.insert('thalia')
bst.insert('aditya')
bst.insert('jaspal')
bst.insert('penny')
bst.insert('darla')
print()
print('----')

#traverse tree'
print("inorder (sorted): ", end="")
bst.inorder()
print()
print('----')
print("\nPostorder: ", end="")
bst.postorder()
print()
print('----')

print("\nPreorder: ", end="")
bst.preorder()
print()
print('----')

print("\nThe number of nodes is", bst.getSize())

#search for an element
print("Is penny in the tree?", bst.search("penny"))

#get a path from the root to penny
print("A path from the root to penny is: ")
path = bst.path('penny')
for node in path:
    print(node.element, end=" ")
print()
print('----')

numbers = [2, 4, 3, 1, 8, 5, 6, 7]
bstTree = BinarySearch2.BSTree2()
for xdata in numbers:
    bstTree.insert(xdata)
print('----')
print("\nInorder (sorted): ", end="")
bstTree.inorder()
