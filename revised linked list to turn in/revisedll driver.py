import revisedll

def main():
    LL = revisedll.LinkedList() #create the object
    LL.append(1)
    LL.append(201)
    LL.append(31)
    LL.display()
    print("----list^")
    LL.prepend(19)
    LL.display()
    print("---prepend^")
    print(LL.head.data) #print head data
    print("---head node data^")
    LL.insert(LL.head.next.next, 4)#inserts data at next node, more next's means
    #more index's 
    LL.display()
    
    print("---insert^")
    #LL.sort()  #SORT function breaks everything with no error
    #just deletes list and even breaks the reverse function before it is ever
    #called on
    #see revisedll line 58 
    LL.display()
    print("---")
    LL.reverse()
    print("---reversal--")
    LL.display()
main()
    
#ran out of time to figure out why sort does not work
