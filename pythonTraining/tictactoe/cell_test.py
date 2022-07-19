import pytest
from cell import Cell


newCell = Cell()

# class TestCell:
def test_first_test():
    flag= newCell.isMarked()
    assert flag == False
    
def test_second_test():
    newCell.mark = "X"
    flag = newCell.isMarked()
    assert flag == True
def test_third_test():
    newCell.mark = "O"
    flag = newCell.isMarked()
    assert flag == True
    
def test_fourth_test():
    newCell.mark = "arbitary"
    flag = newCell.isMarked()
    assert flag == False
