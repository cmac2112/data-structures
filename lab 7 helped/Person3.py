class Person:

    def __init__(self, name, address, number):
        self.__name = name
        self.set_address(address)
        self.__number = number

    #settors for name
    def set_name(self, name):
        self.__name = name

    #set for address
    def set_address(self, address):
        self.__address = address

    #set for numbers
    def set_number(self, number):
        self.__number = number

    #gettors for all
    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_number(self):
        return self.__number

    def __str__(self):
        print_p = '\nName: ' + self.get_name() + \
                  '\nAddress: ' + self.get_address() + \
                  '\nNumber: '  + self.get_number()
        return print_p


# Customer class is a subclass of the Person class
class Customer(Person):
    def __init__(self, name, address, number, cnumber, mail):
        Person.__init__(self, name, address, number)
        self.cnumber = cnumber
        self.mail = int(input("Enter 1 to be put on mail list, 2 if not:"))
        #get number from customer
    # Data attributes unique to Customer class
    # mutators/setters
    def set_cnumber(self, cnumber):
        self.cnumber = cnumber

    def set_mail(self, mail):
        self.mail = mail

    # Data attributes getters/accessors for produtionworker class
    def get_cnumber(self):
        return self.cnumber

    def get_mail(self):
        if self.mail == 1: #decides if customer is on mail list
            return True
        else:
            return False



    # format string for printing current instance
    def __str__(self):
        print_pw = '\nName: ' + self.get_name() + \
                   '\nID: ' + self.get_address() + \
                   '\nNumber: ' + self.get_number() + \
                   '\nCustomer number: ' + self.get_cnumber() + \
                   '\nOn Mail list: ' + str(self.get_mail()) + '\n'

        return print_pw
        
