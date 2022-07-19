from board import Board

class Player:
    def __init__(self , name , symbol):
        self.name = name
        self.symbol = symbol

class Game:
    def __init__(self ):
        self.player1 = Player("X")
        self.player2 = Player("O")
        self.board = Board()
        self.turn = 1

    def play(self,index):
        symbol= "X"
        for i in range(9):
            self.board.cells[index].mark = symbol
            index = input("input index")
            if symbol == "X":
                symbol ="O"
            else:
                symbol ="X"
            flag, value= self.board.resultAnalyzer()
            if flag:
                break
        

