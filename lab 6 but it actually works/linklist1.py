class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data  # Assign data which is the value to be stored
        self.next_node = next_node  # Initialize next_node which reference to next node on the list

    def get_data(self):
        return self.data  # Get the data

    def set_data(self, data):
        self.data = data  # So we can change data in the node

    def get_next(self):
        return self.next_node  # Get the next node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0
        

    def reverseList(head):
        prev = None
        temp = head
        nex = head.next_node
        while temp != None:
            nex = temp.next_node #1st node temp variable
            temp.next_node = prev #var head becomes next node
             #changes pointer to point other way
            prev = temp #previous node becomes new temp to move it along thechai
            temp = nex
        head = prev
        return prev #return value of prevous so head is equal to something
        #and doesnt just skip the loop

    def insert(self, in_data):
        new_node = Node(in_data)

        new_node.set_next(self.head)

        self.head = new_node

        self.count += 1

    def display(self):
        current = self.head
        while (current):
            print(current.data)
            current = current.next_node
