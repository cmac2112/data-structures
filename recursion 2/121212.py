def recursion(base, exp):
    #base condition
    if (exp == 1):
        return(base)
    if exp != 1:
        return(base*recursion(base,exp))

base = int(input('Enter base number'))
exp = int(input("Enter exponet number:"))
 #pass base and exponet arguments to recurseive function
print(base, "^", exp, '=',recursion(base,exp))
recursion(base, exp)
