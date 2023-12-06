# A single node of a singly linked list
# Linked List - LAB 6
# programmer: Leroy Wilson
# date: 9/22/2022
class Node:
    # Stuff to remember
    # Each element of a linked list is called a node
    # Each node has two different fields
    #   1. Data contains the value to be stored in the node.
    #   2. Next contains a reference to the next node on the list.
    # The first node is called the head and used as starting point for iteration
    # The last node must have its next reference pointing to None for end of list

    # Constructor
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


# A Linked List class with a single head node
class LinkedList:
    def __init__(self):
        self.head = Node()   # The head/start of the list
        # count attribute so that when adding or removing items, we can
        # can add or minus one from this. Keeps track of number of items.
        # Not necessary and adds to complexity, but it can save time in some instances
        self.count = 0 # count atrribute


    # insertion method for the linked list at the begining of the list
    def insert(self, in_data):
        # create a new node to hold the data
        new_node = Node(in_data)

        # set the next of the new node to the current head
        new_node.set_next(self.head)

        # set the head of the Linked List to the new head
        self.head = new_node

        # add 1 to the count of nodes
        self.count += 1


    # Insert method to insert at the end of the list
    def insert_end(self, in_data):
        new_node = Node(in_data)
        if(self.head == None):
            new_node = self.head
        else:
            current = self.head
            while current.next_node is not None:
                current = current.next_node
            current.next_node = new_node
        self.count += 1


    # Insert data at specific index
    def insert_at(self, in_data, index):
        newNode = Node(in_data)
        if (index < 1):  # this is an error
            print("\nindex should be >= 1.")
        elif (index == 1):  # make this the new head
            newNode.next_node = self.head
            self.head = newNode
            self.count += 1
        else:  # traverse node to previous insert position and check if i
            temp = self.head

        # Traverse to the node that is previous to the insert position and
        # check if it is null or not. In case of null, the specified position
        # does not exist. In other cases, assign next of the new node as next
        # of the previous node and next of previous node as the new node
        for i in range(1, index - 1):  # loop until previous position before insert
            if temp != None:
                temp = temp.next_node
        if temp != None:
            newNode.next_node = temp.next_node
            temp.next_node = newNode
            self.count += 1
        else:
            print("\nThe previous node is null.")


    # Count nodes until the end, return the count
    def length(self):

        # start with the first item in the Linked List
        current = self.head
        count = 0  # Create a counter

        # Loop through each item in the list
        while current:

            # Add one to counter
            count += 1

            # Get the next item in the list
            current = current.get_next()
        return count


    # Alternative method to get the count using the count variable in program
    def get_count(self):
        # Return the length of the linked list with complexity of 0(1)
        return self.count


    # Check if the linked list is empty, only if head is equal to None
    def is_empty(self):
        return self.head == None

    # Traverse each node from top to bottom until in_data matches node
    def search(self, in_data):

        # start with the first item in the Linked List
        current = self.head
        found = False # Set flag to found
        while current and found is False:

            # if the data in current matches in_data
            if current.get_data() == in_data:
                found = True
            # otherwise we get the next item in the list
            else:
                current = current.get_next()
        # Return true or false for the search results
        return found


    # Traverse each node from top to bottom until search item
    # matches node. Once correct node is found, remove node. It
    # takes the previous node and resets the node's pointer to pointer
    # of the node being deleted.
    def delete(self, in_data):

        # set the current node starting with the head
        current = self.head

        #create a previous node to hold the one before
        #the node we want to remove
        previous = None
        found = False  # Set flag to found

        # Loop from top until found is true or end of linkedlist
        while current and found is False:


            if current.get_data() == in_data:
                found = True

            # otherwise we set previous to current and
            # current to the next item in list
            else:
                previous = current
                current = current.get_next()

        # if the current is None then item, not in the list
        if current is None:
            raise ValueError(f"Data {in_data} not in list")

        # if previous None then the item is at the head
        if previous is None:
            self.head = current.get_next()
            self.count -= 1  # subtract 1 from number of nodes

        # otherwise we remove that node from the list
        else:
            previous.set_next(current.get_next())
            self.count -= 1

    # Delete an element at the given index
    def delete_at(self, index):
        if index < 1:  # Make sure index is not less than one
            print("\nIndex should be >= 1.")

        # if the index is 1 and head is not null, make
        # head next as head and delete previous head
        elif index == 1 and self.head != None:
            nodeToDelete = self.head
            self.head = self.head.next_node
            nodeToDelete = None
            self.count -= 1  # subtract 1 from number of nodes

        # Else, make a temp node and traverse to the
        # node previous to the index
        else:
            temp = self.head
            for i in range(1, index - 1):
                if (temp != None):
                    temp = temp.next_node
            self.count -= 1  # subtract 1 from number of nodes


            # If the previous node and next of the previous
            # is not null, adjust links
            if (temp != None and temp.next_node != None):
                nodeToDelete = temp.next_node
                temp.next_node = temp.next_node.next_node
                nodeToDelete = None

            # Else the given node will be empty.
            else:
                print("\nThe node is already null.")

    # display the nodes in the list
    def display(self):
        current = self.head
        while (current):
            print(current.data)
            current = current.next_node

    # test bubble sort
    # perform bubble sort in single linked list
    def bubbleSort(self):
        if self.head != None:  # ensure list is not empty
            current = None
            new_head = None
            move_node = None
            previous = None

            # Traverse through each item in the linked list
            while self.head != None:
                previous = None
                current = self.head
                move_node = self.head
                while (current != None):

                    # When current node value is grator than previous node
                    if current.next_node != None and current.next_node.data > move_node.data:
                        # Swap node values
                        move_node = current.next_node
                        previous = current

                    current = current.next_node

                if move_node == self.head:
                    self.head = (self.head).next_node

                if previous != None:
                    previous.next_node = move_node.next_node

                move_node.next_node = new_head
                new_head = move_node

            # make new head
            self.head = new_head

        else:
            print("Empty Linked list")

    # Update the data item.
    def replace(self, in_data, new_data):
        # start with the first item in the Linked List
        current = self.head
        found = False  # Set flag to found
        while current and found is False:

            # if the data in current matches in_data
            if current.get_data() == in_data:
                current.set_data(new_data)
                found = True
            # otherwise we get the next item in the list
            else:
                current = current.get_next()

        # if while loop breaks with current equals to None, then nothing found
        if current is None:
            return found

