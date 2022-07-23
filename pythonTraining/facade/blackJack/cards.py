import random

class Cards:
    cards =[2,3,4,5,6,7,8,9,10,'J','Q','K','A']
    suites = ['H', 'C', 'S', 'D']
    def __init__(self):
        self.value = random.choice(Cards.cards)
        self.suits = random.choice(Cards.suites)
        self.total = 0
    def returnValueSuit(self):
        return self.value,self.suits




