from BankingApp import Bank
class Customer:
    customerId = -1
    allCustomers = []

    def __init__(self,firstName, lastName,userName):
        self.firstName = firstName
        self.lastName = lastName
        self.totalBalance = 0
        self.accounts = []
        self.customerId = Customer.customerId
        # Hook userName
        self.userName = userName

    @staticmethod
    def findCustomer(userName):
        for i in Customer.allCustomers:
            if i.userName == userName:
                return True , i
        return False,None

    @staticmethod
    def createNewCustomer (firstname, lastName,userName):
        isCustomerExit, customer  = Customer.findCustomer(userName)
        if isCustomerExit:
            return False, "Username already Exits"
        Customer.customerId +=1
        newCustomer = Customer(firstname, lastName,userName) 
        Customer.allCustomers.append(newCustomer)
        return True,"Customer Created"
    def deposit(self,amount,bankAbreviation):
        isAccountExits, account =self.findAccount(bankAbreviation)
        if not isAccountExists:
            return False,"Acount not Exists"
        account.balance += amount
        self.__updateTotalBalance()
        self.displayBalance()
        return  True,"Amount deposited"
    def withdraw(Self, amount, bankAbreviation):
        isAccountExists , account = self.findAccount(bankAbreviation)
        if not isAccountExists:
            return False,"Acount not Exists"
        #  check balance is sufficent 
        if not account.isSufficentbalance(amount):
            return False, "Low balance"
        account.balance -= amount
        self.__updateTotalBalance()
        self.displayBalance()
        return  True,"Money Debited"

    def transferAmount(self,creditCustomerUsername, creditBankAbbrivation, debitAbbrivation,amount):
        isCreditCustomerExits, creditCustomer = Customer.findCustomer(creditCustomerUsername)
        if not isCreditCustomerExits:
            return False, "Crediter account dose not exists"
        self.withdraw()
        creditCustomer.deposit()
        self.deposit()
    def selfTrasfer(self,creditBankAbbrivation,amount,debitAbbrivation):
        self.transferAmount(self.userName,creditBankAbbrivation,debitAbbrivation,amount)
        return True,"Money Debited  "


    def findAccount(self,bankAbreviation ):
        if len(self.accounts == 0):
            return False,"NO account found"
        for a in self.account:
            if a.isAccountExists(bankAbreviation):
                return True,a
            else:
                return False, None

    def __updateTotalBalance():
        self.totalBalance = 0
        for a in self.accounts:
            self.totalBalance += a.balance
    def displayBalance(self):
        print(self.firstName,"Total Balanceis :" , self.totalBalance)
        for a in self.accounts:
            a.displayBalance()
    def createNewAccount(self, bankAbreviation):
        # check customer cannot have multiple account in same bank
        isAccountExists,account=self.findAccount()
        if isAccountExists:
            return False, "Your Account alredy Exsits"
        isAccountCreated, account = Account.createNewAccount(bankAbreviation)
        if not isAccountCreated:
            return False, "Account not created Retry"
        self.accounts.append(account)
        self.__updateTotalBalance
        return True,"Account Created"
    

