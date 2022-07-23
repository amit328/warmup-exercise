from cell import Cell
class Board:
    def __init__(self):
        self.cells = [Cell(),Cell(),Cell(),Cell(),Cell(),Cell(),Cell(),Cell(),Cell()]

    
    def resultAnalyzer(self):
        # pass
        if((self.cells[0].mark and self.cells[1].mark and self.cells[2].mark and self.cells[3].mark  and self.cells[4].mark and self.cells[5].mark and self.cells[6].mark and self.cells[7].mark and self.cells[8].mark) == ""):
            
            return False,None
        elif ((self.cells[0].mark  == self.cells[1].mark) and (self.cells[1].mark == self.cells[2].mark) ) :
            return True,self.cells[0].mark
        elif (self.cells[3].mark  == self.cells[4].mark and self.cells[4].mark == self.cells[5].mark  ) :
            print("ghvhgvg")

            return True,self.cells[3].mark
        elif (self.cells[6].mark  == self.cells[7].mark and self.cells[7].mark == self.cells[8].mark ):
            print("ghvhgvg")

            return True,self.cells[6].mark
        elif (self.cells[0].mark  == self.cells[4].mark and self.cells[4].mark == self.cells[8].mark ):
            print("ghvhgvg")

            return True,self.cells[0].mark
        elif(self.cells[2].mark  == self.cells[4].mark and self.cells[4].mark == self.cells[6].mark ):
            print("ghvhgvg")

            return True,self.cells[2].mark
        elif(self.cells[0].mark  == self.cells[3].mark and self.cells[3].mark == self.cells[6].mark ):
            return True,self.cells[0].mark
        elif(self.cells[1].mark  == self.cells[4].mark and self.cells[4].mark == self.cells[7].mark ):
            return True,self.cells[1].mark
        elif(self.cells[2].mark  == self.cells[5].mark and self.cells[5].mark == self.cells[8].mark ):
            return True,self.cells[2].mark
        else:
            return False,None
        
    def printBoard(self):
        for i in range(9):
            if i%3 ==0:
                print("")

            print(self.cells[i].mark, " ")

            
        
