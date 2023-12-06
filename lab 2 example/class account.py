
# The SavingsAccount class represents a savings accound

class SavingsAccount: #Superclass class of the functions
    #init method accepts arguments for the account number, intrest rate, and balance

    def __init__(self, account_num, int_rate, bal):
        #attributes
        self.__account_num = account_num
        self.__intrest_rate = int_rate
        self.__balance = bal

    #mutators for the attributes above

    def set_account_num(self, account_num):
        self.__account_num = account_num

    def set_intrest_rate(self, int_rate):
        self.__intrest_rate = int_rate

    def set_balance(self, bal):
        self.__balance = bal

    #accessors for attributes

    def get_account_num(self):
        return self.__account_num

    def get_intrest_rate(self):
        return self.__intrest_rate

    def get_balance(self):
        return self.__balance

#the cd account represents a certificate of deposit (cd) account. it is a subclass of the savings account class
class CD(SavingsAccount): #subclass cd extends class Savings account

    #init method accepts arguments for account number, intrest rate, balance, and maturity date
    def __init__(self, account_num, int_rate, bal, mat_date): #super and subclass attributes
        SavingsAccount.__init__(self, account_num, int_rate, bal)# calling super class savings account
        #init maturity date
        self.__maturity_date = mat_date
    
    def set_maturity_date(self,mat_date):
        self.__maturity_date = mat_date
    #get the maturity date method as an accessor for the __maturity date attribuite
    def get_maturity_date(self):
        return self.__maturity_date
