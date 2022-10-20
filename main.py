# Main program
# Controls a Bank made up of Accounts
from bank import *
   
# Bank instance
oBank = Bank('9 to 5', '123 Michigan Ave, Chicago, IL', '(123) 456-7890')

#Main
while True:
    print()
    print('To get an account balance, press b')
    print('To close an account, press c')
    print('To make a deposit, press d')
    print('To get bank information, press i')
    print('To open a new account, press o')
    print('To quit, press q')
    print('To show all accounts, press s')
    print('To make a withdrawal, press w ')
    print()

print('Done')