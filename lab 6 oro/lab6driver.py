
# Linked List Demo
# programmer: Leroy Wilson
# date: 9/22/2022

import linklist1

def main():
    # Singly Linked List with insertion and print methods
    LL = linklist1.LinkedList()   #<=== create the object
    print("============================================")
    print("Test 1: Check if the linked list is empty")
    print(f"Is the linked list empty: {LL.is_empty()}")
    print()
    print("Test 2: Testing the insert function")
    print("==========Testing insert ===================")
    LL.insert(3)
    LL.insert(4)
    LL.insert(5)
    LL.insert(200)
    LL.display()
    print()
    print("Test 3: Testing the insert function at end of list")
    print("==========Testing insert at End ===================")
    LL.insert_end(9)
    print("Insert 9 at the end")
    LL.display()
    LL.insertsort()
    LL.display()
    print()
    print("Test 4: Testing the insert function at nth position")
    print("============Testing insert at n position ===========")
    print(f"The length method of the node is: {LL.length()}")
    print(f"The count of the count variable : {LL.get_count()}")
    print("insert 299 at position 3")
    LL.insert_at(299, 3)
    LL.display()
    print()
    print("Test 5: Testing the count and length methods")
    print("===== Testing length and get count =============")
    print(f"The length method of the node is: {LL.length()}")
    print(f"The count of the count variable : {LL.get_count()}")
    LL.display()
    print()
    print("Test 6: Testing the delete at n location ")
    print("=========== Testing Delete at ================")
    print(f"The count of the node option Before Delete: {LL.get_count()}")
    LL.delete_at(4)
    LL.display()
    print(f"The count of the node option After Delete: {LL.get_count()}")
    print()
    print("Test 7: Testing Bubble Sort ")
    print("=========== Testing Bubble Sort  ================")
    
    LL.insertsort()
    
    LL.display()
    
    print("list after reversing pointers")
    LL.reverse()
    LL.display()
    
# Call the main function.
if __name__ == '__main__':
    main()
