#Encapsulation
from abc import ABC,abstractclassmethod

class Human(ABC):
    @abstractclassmethod
    def move(self):
        pass

    @abstractclassmethod
    def sing(self):
        pass

    @abstractclassmethod
    def breath(Self):
        pass
    

class Person(Human):
    def __init__(self,fname,lastName,age):
        self.firstName = fname
        self.lastName = lastName
        self.age = age
    @staticmethod
    def addition(a,b):
        return a+b
    def move(self):
        print(self.firstName,self.lastName)


#  inheritance
class Student(Person):
    def __init__(self,fname,lastName,age, grade,marks):
        self.grade = grade
        self.marks = marks
        super().__init__(fname,lastName,age)
    def moveForStudent(self):
        super().move() 
        # or self.move() and it might cause recursion issue so use super only


class Staff():
    def __init__(self empid,year):
        self.empid = empid
        self.year = year

# multiple inheretiance
class Teacher(Person, Staff): 
    def __init__(self,fname,lastName,age, empid,year,subject):
        Person.__init__(fname,lastName,age)
        Staff.__init__(empid,year)
        self.subject = subject


# abstract class it is done with the help of package



if __name__ == "__main":

    amit = Person("amit", "chhabria",22)
    yash = Person("yash", "xyz", 1212)
    yash = amit
    yash.age = 24

    print(amit.age)#24 
    print(yash.age)#24 point to the same

# need to do shallo copy in of class,array,list varinbale then use copy package it has to do xyz = copy.copy(amit)
#  factory function generates object and return object 
# requirement of factory function 