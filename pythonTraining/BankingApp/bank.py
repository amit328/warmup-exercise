
class Bank:
    bankId = -1
    allBanks = []
    def __init__(self,fullName,bankAbreviation):
        self.fullName = fullName
        self.bankAbreviation = bankAbreviation
        Bank.bankId += 1
        self.bankId = Bank.bankId
        @staticmethod
        def findBank(bankAbreviation):
            for i in Bank.allBanks:
                if i.bankAbreviation == bankAbreviation:
                    return True,i
            return False, None  
        @staticmethod
        def createNewBank(fullName,bankAbreviation):
            isBankExist, bankObject = Bank.findBank(bankAbreviation)
            if isBankExist:
                return False,"Bank bankAbreviation alredy exits"
            if bankObject.fullName == fullName:
                return False, "Bank Full Name alredy exits"
            newBank = Bank(fullName, bankAbreviation)
            Bank.allBanks.append(newBank)
            return True, "Bank Created"

        

