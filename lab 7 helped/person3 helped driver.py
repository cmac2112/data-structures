import Person3


def main():
    # defining variables to be used
    name = ""
    address = ""
    number = "" 
    c_number = ""
    mail = False
    #get info from user
    name = input("Enter your name:")
    address = input("enter your address")
    number = input("Enter your phone number")
    c_number = input("Enter your customer number")

    

    # create object with items inputted above
    c1 = Person3.Customer(name, address, number, c_number, mail)  #<== Person should be file name of the class importing.
    print(c1)
    
main()
