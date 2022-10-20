from account import *   # Bank class - object manager object

class Bank():

    def __init__(self, hours, address, phone):
        self.accountsDict = {}   # Manages dictionary of Account objects
        self.nextAccountNumber = 0
        self.hours = hours
        self.address = address
        self.phone = phone

    def askForValidAccountNumber(self):
        accountNumber = input('Please provide account #: ')
        try:
            accountNumber = int(accountNumber)
        except ValueError:
            raise AbortTransaction('Must be an ineteger ')
        if accountNumber not in self.accountsDict:
            raise AbortTransaction('There is no account # ' + str(accountNumber))
        return accountNumber

    def getUsersAccount(self):
        accountNumber = self.askForValidAccountNumber()
        oAccount = self.accountsDict[accountNumber]
        self.askForValidPassword(oAccount)
        return oAccount

    def askForValidPassword(self, oAccount):
        password = input('Please enter your password: ')
        oAccount.checkPasswordMatch(password)
    
    def createAccount(self, theName, theStartingAmount, thePassword):
        oAccount = Account(theName, theStartingAmount, thePassword)
        newAccountNumber = self.nextAccountNumber
        self.accountsDict[newAccountNumber] = oAccount
        self.nextAccountNumber = self.nextAccountNumber + 1   # Increment for next account created
        return newAccountNumber

    def openAccount(self):
        print('*** Open Account ***')
        userName = input('What is your username? ')
        userStartingAmount = input('How much is your initial deposit ? ')
        userPassword = input('Create a new password ')
        userAccountNumber = self.createAccount(userName, userStartingAmount, userPassword)
        print('Account created, account #: ', userAccountNumber)

    def closeAccount(self):
        print('*** Close Account ***')
        userAccountNumber = self.askForValidAccountNumber()
        oAccount = self.accountsDict[userAccountNumber]
        self.askForValidPassword(oAccount)
        theBalance = oAccount.getBalance()
        print('You had', theBalance, 'in your account, returned to you.')
        del self.accountsDict[userAccountNumber]
        print('Your account is now closed.')

    def balance(self):
        print('*** Get Balance ***')
        oAccount = self.getUsersAccount()
        theBalance = oAccount.getBalance()
        print('Total balance:', theBalance)

    def deposit(self):
        print('*** Deposit ***')
        oAccount = self.getUsersAccount()
        depositAmount = input('Amount: ')
        theBalance = oAccount.deposit(depositAmount)
        print('Deposited:', depositAmount)
        print('Your new balance is:', theBalance)

    def withdraw(self):
        print('*** Withdraw ***')
        oAccount = self.getUsersAccount()
        userAmount = input('Amount: ')
        theBalance = oAccount.withdraw(userAmount)
        print('Withdrew:', userAmount)
        print('Your new balance is:', theBalance)

    def getInfo(self):
        print('Hours:', self.hours)
        print('Address:', self.address)
        print('Phone:', self.phone)
        print(len(self.accountsDict), 'account(s) open.')

    # For Bank admin, could build this to require a password
    def show(self):
        print('*** Show ***')
        for userAccountNumber in self.accountsDict:
            oAccount = self.accountsDict[userAccountNumber]
            print('Account:', userAccountNumber)
            oAccount.show()
            print()


'''
=> no try except block in getUsersAccount() because askForValidAccountNumber() is in a lower level
'''