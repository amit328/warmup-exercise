import random
from cards import Cards
class Player:
    def __init__(self, userName):
        # self.credits = 10
        self.userName = userName
        self.cards = []                         
        self.total = 0                          
        self.aces = 0 

    def getUserName(self):
        return self.userName
    def getTotal(self):
        return self.total

    def calculateAcePoint(self):
        if (11 + self.total > 21):
            self.aces = 1
        else: 
            self.aces = 11


    def pickCard(self):
        newPoint,symbol = Cards.returnValueSuit()
        self.cards.append(symbol)
        self.cards.append(newPoint)                  
        if newPoint == 'A':
            newPoint = self.calculateAcePoint()
            self.updateTotal(newPoint)                  
        if newPoint == 'K' or newPoint == 'J' or newPoint== 'Q':
            newPoint = 10
            self.updateTotal(newPoint)        
        self.updateTotal(newPoint)
        return newPoint,symbol

    def updateTotal(self,newPoint):
        self.total += newPoint



    
