#queue using list
class Queue:
    def __init__(self):
        self.list = []

    def size(self):
        return len(self.list)
    #find size of list
    def isempty(self):
        if self.size(): #use size of list to determine if empty
            return False
        else:
            return True

    def peek(self):
        if self.size():
            return self.elements[-1]
        else:
            return None
    def show(self):
        return self.list

    def enqueue(self, item):
        self.list.append(item)

    def dequeue(self, index):
        self.list.pop(index)
        
