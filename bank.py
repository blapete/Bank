from account import *   # Bank class - object manager object

class Bank():

    def __init__(self, hours, address, phone):
        self.accountsDict = {}   # Manages dictionary of Account objects
        self.nextAccountNumber = 0
        self.hours = hours
        self.address = address
        self.phone = phone

    def askForValidAccountNumber(self):

    def getUsersAccount(self):

    def askForValidPassword(self, oAccount):
    
    def createAccount(self, theName, theStartingAmount, thePassword):

    def openAccount(self):

    def closeAccount(self):

    def balance(self):

    def deposit(self):

    def withdraw(self):

    def getInfo(self):

    # For Bank admin
    def show(self):