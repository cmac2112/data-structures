#emplyoee and production worker classes
class Employee:
    def __init__(self, name, id_num):
        self.__employ_name = name #initialize name
        self.__employ_id_num = id_num #initialize id number

    def set_employ_name(self, name): #setter for name
        self.__employ_name = name

    def set_employ_id_num(self, id_num):
        self.__employ_id_num = id_num #setter for id number

    def get_employ_name(self):
        return self.__employ_name #getter for name
        #get method is accessor for pay rate attribute
    def get_employ_id_num(self):
        return self.__employ_id_num

class ProductionWorker(Employee): #inherits employee parent class
    def __init__(self, name, id_num, shift, pay_rate):
        Employee.__init__(self, name, id_num) #call employee superclass init
        #and pass needed arguments

        #initialize shift and payrate for production worker
        self.__employ_shift = shift
        self.__employ_pay_rate = pay_rate

    #setemployshift becomes mutator for employ shift attribute
    def set_employ_shift(self, shift):
        self.__employ_shift = shift

    def get_employ_pay_rate(self):
        return self.__employ_pay_rate

class ShiftSupervisor(Employee):
    def __init__(self, name, id_num, salary, bonus):
        #call superclass init method and pass required arguments
        Employee.__init__(
    
