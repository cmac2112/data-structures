#revised linked list lab 6
#date 10/3/2022
#caden mcarthur
class Node:
     def __init__(self, data):
         self.data = data
         self.next = None

class LinkedList:
    def __init__(self):
        self.head = None #create head pointer
        
    def display(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next #will loop print every node 
    def append(self, data):
        new_node = Node(data) #uses class node to create new node

        #check if list is empty
        if self.head is None:
            self.head = new_node
            return
        #if list is not empty
        
        last_node = self.head
        while last_node.next: #while next pointer is not null
            last_node = last_node.next
             #moves pointer to last node in ll
        last_node.next = new_node #appends node to end of list
    def prepend(self, data): #found on internet to place element at front
        new_node = Node(data) #similar to append but make head point at new front node
        new_node.next = self.head #next new node becomes head
        self.head = new_node #makes it happen
         

    def insert(self, prev_node, data):
        #check if prev node is in list
        if not prev_node:
            print("Previous node not in list")
            return
        new_node = Node(data) #calls on Node class to make new node
        new_node.next = prev_node.next #points to previous node to next
        #make pointer of insert point to next node after it
        prev_node.next = new_node

    #reversal of the pointers
    def reverse(self):
        prev = None
        cur = self.head #will move along list
        while cur:
            temp = cur.next #store pointer in temp variable
            cur.next = prev #makes current node the previous node
            prev = cur
            cur = temp #updates current next in list
        self.head = prev
#SORT PROGRAM BELOW, BREAKS EVERYTHING WITH NO ERROR WHEN RAN
        #RECURSIVE SELECT SORT
    #def swapNodes(head_ref, current_x, current_y, prev_y):
        #makes current y the new head
        #head_ref = current_y
        #adjust links between nodes
        #prev_y.next = current_x

        #swap the next pointers, temp variable to store temp pointer
       # temp = current_y.next
        #current_y.next = current_x.next
        #current_x.next = temp
        #return head_ref #return new head as bigger number to be put in front
         #recursive select sort       
    #def sort(head):
        #if there is only 1 node
        #if(head.next == None):
           # return head
        #small pointer to store node having smallest value
       # small = head
        #before small pointer to store node previous to small node
       # bfsmall = None
        #ptr = head

        #traverse list until the last node
        #while (ptr.next != None):
            #while there is a next node, update vars
            #small = ptr.next
            #bfsmall = ptr
        #ptr = ptr.next
        #if small and the head are not the same, swap head with small node
        #if (small != head):
            #head = swapNodes(head, head, small, bfsmall)

        #sort remaining using recursion
           # head.next = sort(head.next)
        #return head

    
