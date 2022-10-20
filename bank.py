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

    def deposit(self):

    def withdraw(self):

    def getInfo(self):

    # For Bank admin
    def show(self):