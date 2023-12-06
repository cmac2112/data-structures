#stack()
class Stack:
    def __init__(self):
        self.elements = [] #create stack
        
    def push (self, data):
        self.elements.append(data) #push elements into stack using append

    def pop(self):
        if self.elements: #pop elements
            return self.elements.pop()
        else:
            return None

    def size(self): #find the siZE
        return len(self.elements)
    
    def isempty(self):
        if self.size(): #check if stack is empty
            return False
        else:
            return True
    def peek(self):
        if self.size(): #peek at top element
            return self.elements[-1]
        else:
            return None
    def traverse(self): #peek at all elements
        if self.size():
            for i in range(len(self.elements)-1,-1,-1):
                return Stack[i]
        else:
            return None

    def show(self):
        for i in range(n, 0, -1):
            s.push(i)

    def __str__(self):
        return str(self.Stack)
