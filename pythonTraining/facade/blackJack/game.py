from player import Player


class DefaultPlayer:
    def __init__(self,username):
        self.username= username
class Game:
    def __init__(self,player1 =DefaultPlayer('player1'), player2 =DefaultPlayer('player2')):
        self.player1 = player1
        self.player2 = player2
        self.turn= ''
        self.hitSkip = ''

    def createGame(self):
        self.turn= 'player1'
        countSkip = 0
        while True:
            if self.turn == 'player1':
                self.hitSkip = input("want to hit or skip ?")
                if self.hitSkip == 'skip':
                    print("Player Skiped")
                    countSkip +=1
                elif self.hitSkip == 'hit':
                    card,suitValue = self.player1.pickCard()
                    print(f"card: {card} Suit: {suitValue}")
                    countSkip = 0
                else:
                    print('Invalid input')
            elif self.turn == 'player2':
                self.hitSkip = input("want to hit or skip ?")
                if self.hitSkip == 'skip':
                    print("Player Skiped")
                    countSkip +=1
                elif self.hitSkip == 'hit':
                    card,suitValue = self.player2.pickCard()
                    print(f"card: {card} Suit: {suitValue}")
                    countSkip =0
                else:
                    print('Invalid input')
            if self.turn == "player1":
                self.turn = "player2"
            else:
                self.turn = "player1"
            if countSkip ==2:
                print("Draw")
                break
            print(f"Player 1 score={self.player1.getTotal()} player2 score={self.player2.getTotal()}")

    def winingState(self):
        if self.player1.getTotal() == 21:
            return True,self.player1.username()
        elif self.player1.getTotal() > 21:
            return True, self.player2.username()
        elif self.player2.getTotal() > 21:
            return True, self.player1.username()
        elif self.player2.getTotal() == 21:
            return True,self.player2.username()



            
