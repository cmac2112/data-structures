#binary search tree 1

class BSTree:
    #store node
    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data

    #search method to find data in tree
    def search(self, tdata):
        if tdata < self.data:
            if self.left is None:
                return str(tdata)+"Not Found"
            return self.left.search(tdata)
        elif tdata > self.data:
            if self.right is None:
                return str(tdata)+ "Not Found"
            return self.right.search(tdata)
        else:
            print(str(self.data) + 'is found')

    #recursive function ti insert a key into a Binary search tree
    def insert(self, data):

        #if root is none, create a new node and return it
        if not self.data:
            self.data = data
            return
        if self.data == data:
            return
        #recursion for left subtree
        if data < self.data:
            if self.left:
                self.left.insert(data)
                return
            self.left = BSTree(data)
            return
        #recursion for right
        if self.right:
            self.right.insert(data)
            return
        self.right = BSTree(data)

        #get min value in tree
    def get_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.data
    #get max value
    def get_max(self):
        current = self
        while current.right is not None:
            current = current.right
            return current.data
    #remove node from tree
    def delete(self, data):
        if self is None:
            return self
        if data < self.data:
            if self.left:
                self.left = self.left.delete(data)
            return self
        if data > self.data:
            if self.right:
                self.right = self.right.delete(data)
            return self
        if self.right is None:
            return self.left
        if self.left is None:
            return self.right
        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        self.data = min_larger_node.data
        self.right = self.right.delete(min_larger_node.data)
        return self

    # check if value exists in tree
    def exists(self, data):
        if data == self.data:
            return True
        if data < self.data:
            if self.left is None:
                return False
            return self.left.exists(data)

        if self.right is None:
            return False
        return self.right.exists(data)
    #print list in preorder order
    def preorder(self, datax):
        if self.data is not None:
            datax.append(self.data)
        if self.left is not None:
            self.left.preorder(datax)
        if self.right is not None:
            self.right.preorder(datax)
        return datax

    #print out inorder order
    def inorder(self, datax):
        if self.left is not None:
            self.left.inorder(datax)
        if self.data is not None:
            datax.append(self.data)
        if self.right is not None:
            self.right.inorder(datax)
        return datax

    #print list in postorder
    def postorder(self, datax):
        if self.left is not None:
            self.left.postorder(datax)
        if self.right is not None:
            self.right.postorder(datax)
        if self.data is not None:
            datax.append(self.data)
        return datax

    
