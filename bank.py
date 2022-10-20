from account import *   # Bank class - object manager object

class Bank():

    def __init__(self, hours, address, phone):
        self.accountsDict = {}   # Manages dictionary of Account objects
        self.nextAccountNumber = 0
        self.hours = hours
        self.address = address
        self.phone = phone

    def askForValidAccountNumber(self):
        accountNumber = input('What is your account number? ')
        try:
            accountNumber = int(accountNumber)
        except ValueError:
            raise AbortTransaction('Account number must be an integer ')
        if accountNumber not in self.accountsDict:
            raise AbortTransaction('There is no account ' + str(accountNumber))
        return accountNumber

    def getUsersAccount(self):
        accountNumber = self.askForValidAccountNumber()
        theAccount = self.accountsDict[accountNumber]
        self.askForValidPassword(theAccount)
        return theAccount

    def askForValidPassword(self, theAccount):
        password = input('Please enter your password: ')
        theAccount.checkPasswordMatch(password)
    
    def createAccount(self, theName, theStartingAmount, thePassword):
        theAccount = Account(theName, theStartingAmount, thePassword)
        newAccountNumber = self.nextAccountNumber
        self.accountsDict[newAccountNumber] = theAccount
        self.nextAccountNumber = self.nextAccountNumber + 1   # Increment for next account created
        return newAccountNumber

    def openAccount(self):
        print('*** Open Account ***')
        userName = input('What is your username? ')
        userStartingAmount = input('How much is your initial deposit? ')
        userPassword = input('Create a new password ')
        userAccountNumber = self.createAccount(userName, userStartingAmount, userPassword)
        print('Account created, account # ', userAccountNumber)

    def closeAccount(self):
        print('*** Close Account ***')
        userAccountNumber = self.askForValidAccountNumber()
        theAccount = self.accountsDict[userAccountNumber]
        self.askForValidPassword(theAccount)
        theBalance = theAccount.getBalance()
        print('You had', theBalance, 'in your account, returned to you.')
        del self.accountsDict[userAccountNumber]
        print('Your account is now closed.')

    def balance(self):
        print('*** Get Balance ***')
        theAccount = self.getUsersAccount()
        theBalance = theAccount.getBalance()
        print('Total balance:', theBalance)

    def deposit(self):
        print('*** Deposit ***')
        theAccount = self.getUsersAccount()
        depositAmount = input('Amount: ')
        theBalance = theAccount.deposit(depositAmount)
        print('Deposited:', depositAmount)
        print('Your new balance is:', theBalance)

    def withdraw(self):
        print('*** Withdraw ***')
        theAccount = self.getUsersAccount()
        userAmount = input('Amount: ')
        theBalance = theAccount.withdraw(userAmount)
        print('Withdrew: ', userAmount)
        print('Your new balance is: ', theBalance)

    def getInfo(self):
        print('Hours:', self.hours)
        print('Address:', self.address)
        print('Phone:', self.phone)
        print(len(self.accountsDict), 'account(s) open.')

    # For Bank admin, could build this to require a password
    def show(self):
        print('*** Show ***')
        for userAccountNumber in self.accountsDict:
            theAccount = self.accountsDict[userAccountNumber]
            print('Account: ', userAccountNumber)
            theAccount.show()
            print()


'''
=> no try except block in getUsersAccount() because askForValidAccountNumber() is in a lower level
'''