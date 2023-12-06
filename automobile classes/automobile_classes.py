from enum import auto


class Automobile:
    def __init__(self, make, model, milage, price):
        self.__make = make #initialize attribuites to the class
        self.__model = model
        self.__milage = milage
        self.__price = price

    def set_make(self, make): #defining mutators for the attributes
        self.__make = make
    
    def set_model(self, model):
        self.__model = model

    def set_milage(self, milage):
        self.__milage = milage

    def set_price(self, price):
        self.__price = price

    def get_make(self): #return values to attributes to store
        return self.__make

    def get_model(self):
        return self.__model

    def get_milage(self):
        return self.__milage

    def get_price(self):
        return self.__price

class car(Automobile): #subclass of Automobile 'car' inherits attribuites from automobile

    def __init__(self, make, model, milage, price, doors):
        
        Automobile.__init__(self, make, model, milage, price) #attributes for subclass car and superclass automobile
        self.__doors = doors
        
    def set_doors(self, doors): #mutators to set value
        self.__doors = doors
    def get_doors(self):
        return self.__doors #return what is entered

class Truck(Automobile):# subclass of Automobile 'truck'
    def __init__(self, make, model, milage, price, drive_type): #inherits automobile attributes

        Automobile.__init__(self, make, model, milage, price)#attributes from superclass automobile
        
        self.__drive_type = drive_type
   
    def set_drive_type(self, drive_type):#mutator for drive type for subclass truck under Automobile
       
       self.__drive_type = drive_type
   
    def get_drive_type(self):
        return self.__drive_type

class SUV(Automobile): #subclass for SUV under automobile inherits
    
    def __init__(self, make, model, milage, price, pass_cap):

        Automobile.__init__(self, make, model, milage, price)

        self.__pass_cap = pass_cap #attribute pass_cap for SUV and Automobile

    def set_pass_cap(self, pass_cap):
        self.__pass_cap = pass_cap      #mutator for passcap

    def get_pass_cap(self):
        return self.__pass_cap#return values
