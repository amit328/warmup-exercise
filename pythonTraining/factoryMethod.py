from datetime import date
import datetime
class Student:
    # def __init__(self,firstName,lastName,yearOfAdmission,graduationYear,dob,CGPA):
    def __init__(self,fullname,firstName,lastName,yearOfAdmission,graduationYear,dob,CGPA,age,dropOutYear,gradeinEachSem,avgCGPA,finalGrade):
        self.fullname = fullname
        self.firstName = firstName
        self.lastName = lastName
        self.yearOfAdmission = yearOfAdmission
        self.graduationYear = graduationYear
        self.dob = dob 
        self.age = age
        self.CGPA = CGPA
        self.dropOutYear = dropOutYear
        self.gradeinEachSem =gradeinEachSem
        self.avgCGPA = avgCGPA
        self.finalGrade = finalGrade

    @staticmethod
    def __gradeFunction(grade):
        if(grade >=10):
            return "O"
        elif(grade >= 8):
            return "A"
        elif(grade >= 6):
            return "B"
        else:
            return "F"

    @staticmethod
    def getDetails(firstName, lastName,yearOfAdmission,graduationYear,dob,CGPA):
        fullname = firstName + " " + lastName
        print(fullname)
        print(yearOfAdmission)
        dropOutYear = int(graduationYear) - int(yearOfAdmission)
        if dropOutYear == 4 :
            print("passed")
        else:
            print (dropOutYear)

        print(CGPA)
        dateOfBirthYear = int(dob.strftime("%Y"))
        print(dateOfBirthYear)
        currentYear = int(datetime.datetime.now().strftime("%Y"))
        print(currentYear)
        sumOfCGPA = 0
        for i in range(0, len(CGPA),1):
            sumOfCGPA = sumOfCGPA + CGPA[i]
        total = sumOfCGPA / len(CGPA)
        avgCGPA = total
        print(total)
        finalGrade = Student.__gradeFunction(total)
        print(finalGrade)
        age = currentYear - dateOfBirthYear
        print(age)
        print(CGPA)
        emptyListForGradeinEachSem= []
        for i in CGPA:
            emptyListForGradeinEachSem.append(Student.__gradeFunction(i))
        gradeinEachSem = emptyListForGradeinEachSem
        print(gradeinEachSem)
        return Student(fullname,firstName,lastName,yearOfAdmission,graduationYear,dob,CGPA,age,dropOutYear,gradeinEachSem,avgCGPA,finalGrade)
    
    def show(self, propertyName):
        print("Student - "+ self.fullname+"'s "+propertyName+" is "+str(getattr(self, propertyName)))
    
    def update(self, propertyName, newValue):
        oldValue = str(getattr(self, propertyName))
        setattr(self, propertyName, newValue)
        print("Student - "+self.fullname+"'s "+propertyName+" changed from "+oldValue
                +" to "+str(getattr(self, propertyName)))

if __name__ == "__main__":

    amit = Student.getDetails("amit","chhabria","2018","2022",date(2000,3,29),[10,10,10,10,10,10,10,10])
    action = input("Enter action (S/U) - ")

    try:
        if(action == 'S'):
            amit.show(input("Enter property name - "))
        else:
            amit.update(input("Enter property name - "), input("Enter new value - "))
    except AttributeError:
        print("This property does not exist!")