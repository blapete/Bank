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

    action = input('What do you want to do? ')
    action = action.lower()
    action = action[0]   # get first letter
    print()

    try:
        if action == 'b':
            oBank.balance()
        elif action == 'c':
            oBank.closeAccount()
        elif action == 'd':
            oBank.deposit()
        elif action == 'i':
            oBank.getInfo()
        elif action == 'o':
            oBank.openAccount()
        elif action == 'q':
            break
        elif action == 's':
            oBank.show()
        elif action == 'w':
            oBank.withdraw()
    except AbortTransaction as error:
        print(error)   # Print error message
        
print('Done')

'''
=> Top-level menu presented to the user
'''