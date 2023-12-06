#binary search 2
class Node:
    def __init__(self, data):
        self.element = data
        self.left = None #point to left node, default None
        self.right = None #point to right node , default None

class BSTree2:
    def __init__(self):
        self.root = None
        self.size = 0

    #return true if element is in tree
    def search(self, data):
        current = self.root #start at root

        while current is not None:
            if data < current.element:
                current = current.left
            elif data > current.element:
                current = current.right
            else: #element matches current.element
                return True #element is found

        return False
        #insert element data into binary search tree
        #return true if element is inserted successfully
    def insert(self, data):
        if self.root is None:
            self.root = self.createNewNode(data) #create root
        else:
            #locate parent node
            parent = None
            current = self.root
            while current is not None:
                if data < current.element:
                    parent = current
                    current = current.left
                elif data > current.element:
                    parent = current
                    current = current.right
                else:
                    return False #duplicate node not inserted

            #create new node and attach it to the parent node
            if data < parent.element:
                parent.left = self.createNewNode(data)
            else:
                parent.right = self.createNewNode(data)

            self.size += 1 #increase tree size
            return True #element inserted
    #create a new treenode for element data
    def createNewNode(self, data):
        return Node(data)

    #return size of tree
    def getSize(self):
        return self.size

    #inorder traversal from the root
    def inorder(self):
        self.inorderHelper(self.root)
    #inorder traversal from a subtree
    def inorderHelper(self, r):
        if r is not None:
            self.inorderHelper(r.left)
            print(r.element, end=" ")
            self.inorderHelper(r.right)

    #postorder traversal from root
    def postorder(self):
        self.postorderHelper(self.root)

    #postorder traversal from subtree
    def postorderHelper(self, root):
        if root is not None:
            self.postorderHelper(root.left)
            self.postorderHelper(root.right)
            print(root.element, end=" ")

    #preorder traversal from root
    def preorder(self):
        self.preorderHelper(self.root)

    #preorder traveral from subtree
    def preorderHelper(self, root):
        if root is not None:
            print(root.element, end=" ")
            self.preorderHelper(root.left)
            self.preorderHelper(root.right)
    #returns a path from root leading to the specified element
    def path(self, data):
        list = []
        current = self.root #start at root

        while current is not None:
            list.append(current) #add the node to the list
            if data < current.element:
                current = current.left
            elif data > current.element:
                current = current.right
            else:
                break
        return list #return an array of nodes
    #delete and element from binary search tree
    #return true if element is deleted
    #return flase if element is not in the tree
    def delete(self, data):
        #locate the node to be deleted and its parent node
        parent = None
        current = self.root
        while current is not None:
            if data < current.element:
                parent = current
                current = current.left
            elif data > current.element:
                parent = current
                current = current.right
            else:
                break #element is in the tree pointed by current
        if current is None:
            return False #element is not in tree
        #case 1 current has no left children
        if current.left is None:
            #connect the parent with the right child of the current node
            if parent is None:
                self.root = current.right
            else:
                if data < parent.element:
                    parent.left = current.right
                else:
                    parent.right = current.right
        else:
            #case 2: The current node has a left child
            #locate the rightmost node in the left subtree of current node and its parent
            parentOfRightMost = current
            rightMost = current.left

            while rightMost.right is not None:
                parentOfRightMost = rightMost
                rightMost = rightMost.right #keep going right

            #replace the element in current by the element in rightMost
            current.element = rightMost.element

            #eliminate rightmost node
            if parentOfRightMost.right == rightMost:
                parentOfRightMost.right = rightMost.left
            else:
                #special case:
                parentOfRightMost == current
                parentOfRightMost.left = rightMost.left

            self.size -= 1
            return True #element deleted
    #return true if tree is empty
    def isEmpty(self):
        return self.size == 0

    #remove all elements from tree
    def clear(self):
        self.root = None
        self.size = 0

    #return the root of the tree
    def getRoot(self):
        return self.root
