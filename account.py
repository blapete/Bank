# custom exception
class AbortTransaction(Exception):
    '''abort transaction'''
    pass

class Account():

    def __init__(self, name, balance, password):
        self.name = name
        self.balance = 
        self.password = password

    def validateAmount(self, amount):

    def checkPasswordMatch(self, password):

    def deposit(self, amountToDeposit):

    def getBalance(self):

    def withdraw(self, amountToWithdraw):

    # Testing
    def show(self):