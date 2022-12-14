# custom exception
class AbortTransaction(Exception):
    pass

class Account():

    def __init__(self, name, balance, password):
        self.name = name
        self.balance = self.validateAmount(balance)
        self.password = password

    def validateAmount(self, amount):
        try:
            amount = int(amount)
        except ValueError:
            raise AbortTransaction('Amount must be an integer')
        if amount <= 0:
            raise AbortTransaction('Amount must be positive')
        return amount

    def checkPasswordMatch(self, password):
        if password != self.password:
            raise AbortTransaction('Incorrect password')

    def deposit(self, amountToDeposit):
        amountToDeposit = self.validateAmount(amountToDeposit)
        self.balance = self.balance + amountToDeposit
        return self.balance

    def getBalance(self):
        return self.balance
        
    def withdraw(self, amountToWithdraw):
        amountToWithdraw = self.validateAmount(amountToWithdraw)
        if amountToWithdraw > self.balance:
            raise AbortTransaction('Insufficient funds')

        self.balance = self.balance - amountToWithdraw
        return self.balance

    # Testing
    def show(self):
        print('       Name:', self.name)
        print('       Balance:', self.balance)
        print('       Password:', self.password)

'''
=> The AbortTransaction exception is not handled in this class, if it is raised it is passed back to the caller all the way up the stack until main.py
'''