#this program creates and instance of the SavingsAccount classs and an instance of the CD account

import accounts 

def main():
    #get account number, intrest rate, and account balance for a savings account
    print('Enter the following data for a savings account.')
    acct_num = input('Account number: ')
    int_rate = float(input('Intrest rate: '))
    balance = float(input('Balance:'))

    #create savingsaccount object
    savings = accounts.SavingsAccount(acct_num, int_rate, balance) #accesses the savings account class under accounts.py using
    #values from above

    #get the account number, intrest rate, account balance, amd ,aturity date for a cd

    print('Enter the following data for a CD.')
    acct_num = input('Account number:')
    int_rate = float(input('Intrest rate:'))
    balance = float(input('Balance:'))
    maturity = input('Maturity date:')

    #create CD object
    cd = accounts.CD(acct_num, int_rate, balance, maturity)
    #accesses cd class in accounts.py using variable inputs from above

    #display entered data above

    print('Data entered:')
    print()
    print('Savings Account')
    print('---------------')
    print(f'Account number: {savings.get_account_num()}') #gets account number from accounts.py using the savings object created above
    print(f'Intrest rate: {savings.get_intrest_rate()}')#gets intrest rate using object created
    print(f'Balance: ${savings.get_balance():,.2f}')# same
    print()
    print('CD')
    print('---------')
    print(f'Account number: {cd.get_account_num()}')#gets account number using cd object created from superclass in accounts.py
    print(f'Intrest rate: {cd.get_intrest_rate()}')#same
    print(f'Balance: ${cd.get_balance():,.2f}')#same
    print(f'Maturity date: {cd.get_maturity_date()}')#same


if __name__ == '__main__':
    main()
