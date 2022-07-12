from BankingApp import Bank
class Account :
    accountId = - 1
    def __init__(self, bank , balance):
        self.bank = bank
        self.balance = balance
        self.accountId = Account.accountId

    def isAccountExists(self, ):
        return self.bank.bankAbreviation == bankAbreviation

    def displayBalance(self):
        print(self.bank.bankAbreviation, "balance", self.balance)
    def isSufficentbalance(Self,amount):
        return self.balance >= amount
    @staticmethod
    def createNewAccount(bankAbreviation):
        isBankExist, bankObject = Bank.findBank(bankAbreviation)
        if not isBankExist:
            return False,"Bank doesnt Exist"
        Account.accountId  = +1
        newAccount = Account(bankObject,1000)
        return True,"Account Created" 
