#queues

class Node:
    def __init__(self, data):
        self.data = data #use just normal list not linked list
        self.next_node - None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0

    def isEmpty(self):
        return self._size == 0

    def enqueue(self, item):
        current = Node(item)

        if self.isEmpty():
            self.front = current
        else:
            self.rear.next_node = current
        self.rear = current
        self._size += 1

    def dequeue(self):
        if self.isEmpty():
            return
        val_returned = self.front.data
        self.front = self.front.next_node
        self._size -= 1
        if self.front is None:
            self.rear = None


    def peek(self):
        if self.isEmpty():
            return "Q empty"
        else:
            return self.front.data

    def size(self):
        return self._size

    def show(self):
        current = self.front
        while current:
            print(current.data)
            current = current.next_node
