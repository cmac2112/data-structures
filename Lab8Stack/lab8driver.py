#lab 8 driver
import lab8class

def main():
    bruh = lab8class.Stack()
    print(lab8class.Stack.pop(bruh)) #no elements to pop
    print(lab8class.Stack.size(bruh)) #determine size
    print(lab8class.Stack.peek(bruh)) #peek at top element 'none'
    print(lab8class.Stack.isempty(bruh)) #checks if empty
    bruh.push('12')
    bruh.push('1') #push elements to stack
    bruh.push('122')
    print(lab8class.Stack.peek(bruh)) #redo above
    print(lab8class.Stack.size(bruh))
    print(lab8class.Stack.isempty(bruh))
    
main()
