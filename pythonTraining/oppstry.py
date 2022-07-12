
# inhericatnce with composition 
class Person:
    def __init__(self,fname,lastName,age):
        self.fname = fname
        self.lastName = lastName
        self.age = age
    def move(self):
        print(self.fname, self.lastName,self.age)


class Student():
    def __init__(self, newperson, grade, mark):
        self.grade = grade
        self.mark = mark
        self.newperson = newperson
        


if __name__ == "__main__":
    # how to access the inheritance with composition has a relationship 
    amit = Student(Person("amit", "chhabria",24),10,12)
    amit.newperson.move()


