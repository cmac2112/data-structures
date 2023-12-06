#lab 7 inheritance
#caden mcarthur
#10/6/2022
import lab_3_inheritance as Person

def main():
    #enter some data for class
    name = "ba"
    address = "asd21"
    number = "12"
    cnumber = "32"
    mail = False

    #create object
    c1 = Person.Customer(name, address, number, cnumber, mail)
    print(c1)
    
    
main()
