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

    def openAccount(self):

    def closeAccount(self):

    def balance(self):

    def deposit(self):

    def withdraw(self):

    def getInfo(self):

    # For Bank admin
    def show(self):