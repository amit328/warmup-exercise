from re import X
import pytest
from board import Board
newBoard = Board()

def testDrawwithEmpty():
    flag,value= newBoard.resultAnalyzer()
    assert flag == False and value == None

def testDrawWithFullFirst():
    newBoard.cells[0].mark = "X" 
    newBoard.cells[1].mark = "O" 
    newBoard.cells[2].mark = "X" 
    newBoard.cells[3].mark = "X" 
    newBoard.cells[4].mark = "O" 
    newBoard.cells[5].mark = "X" 
    newBoard.cells[6].mark = "O" 
    newBoard.cells[7].mark = "X" 
    newBoard.cells[8].mark = "O"
    flag,value= newBoard.resultAnalyzer()
    assert flag == False 

def testDrawWithFullSecond():
    newBoard.cells[0].mark = "X"  
    newBoard.cells[1].mark = "O"  
    newBoard.cells[2].mark = "O"  
    newBoard.cells[3].mark = "O" 
    newBoard.cells[4].mark = "O" 
    newBoard.cells[5].mark = "X" 
    newBoard.cells[6].mark = "X" 
    newBoard.cells[7].mark = "X" 
    newBoard.cells[8].mark = "O"
    flag,value= newBoard.resultAnalyzer()
    assert flag == False

def testDrawWithFullThird():
    newBoard.cells[0].mark = "X" 
    newBoard.cells[1].mark = "O"
    newBoard.cells[2].mark = "X" 
    newBoard.cells[3].mark = "X" 
    newBoard.cells[4].mark = "O" 
    newBoard.cells[5].mark = "X" 
    newBoard.cells[6].mark = "O" 
    newBoard.cells[7].mark = "X" 
    newBoard.cells[8].mark = "O"
    flag,value= newBoard.resultAnalyzer()
    assert flag == False    
def testWinnerFirst():
    newBoard.cells[0].mark = "X"  
    newBoard.cells[1].mark = "X" 
    newBoard.cells[2].mark = "X" 
    newBoard.cells[3].mark = "O" 
    newBoard.cells[4].mark = "O" 
    newBoard.cells[5].mark = "X" 
    newBoard.cells[6].mark = "O" 
    newBoard.cells[7].mark = "X" 
    newBoard.cells[8].mark = "O"
    flag,value=newBoard.resultAnalyzer()
    assert flag == True and value == "X"

def testWinnerSecond():
    newBoard.cells[0].mark = "O" 
    newBoard.cells[1].mark = "O"
    newBoard.cells[2].mark = "O" 
    newBoard.cells[3].mark = "X" 
    newBoard.cells[4].mark = "O" 
    newBoard.cells[5].mark = "X" 
    newBoard.cells[6].mark = "O" 
    newBoard.cells[7].mark = "X" 
    newBoard.cells[8].mark = "O"
    flag,value=newBoard.resultAnalyzer()
    assert flag == True,value == "O"
