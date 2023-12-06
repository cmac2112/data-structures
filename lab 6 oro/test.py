#list test

import linklist1

def main():
    LL = linklist1.LinkedList()
    LL.insert(3)
    LL.insert(4)
    LL.insert(5)
    LL.insert(200)
    LL.display()
    LL.reverse_iterative()
    LL.display()

main()
