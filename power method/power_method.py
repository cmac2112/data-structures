

def recursion(base, exp):
    #base condition
    if (exp == 1): #if exponent is 1 
        return(base) #sends base to print function to be produced at the end
    if exp != 1: #if exponent is not equal to one, it returns the value of the base number times itself until exp == 1
        return(base*recursion(base,exp-1))  #returns values back to top minus 1 on exponent to prevent infinite recursion
    #get input from user on what numbers they want
base = int(input('Enter base number'))
exp = int(input("Enter exponet number:"))
 #pass base and exponet arguments to recurseive function
print(base, "^", exp, '=',recursion(base,exp)) #prints selected numbers and passes them as arguments to recursion function
recursion(base, exp)#call function








