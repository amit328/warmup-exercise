from DoctorStaff import DoctorStaff
class Admin:
    doctorStaffList = []
    def __init__(self):
        self.balance = 0
        pass

    @staticmethod
    def createDoctorStaff(userName,firstName, lastName, age, address, gender, dob,password,isDoctor):
        valueOfcheckUserName, checkUserNameStatement = Admin.checkUserName(userName)
        if valueOfcheckUserName:
            newDoctorStaff = DoctorStaff.createDoctorStaff(userName,firstName, lastName, age, address, gender, dob,password,isDoctor)
            Admin.doctorStaffList.append(newDoctorStaff)
            print(isDoctor)
            print(len(Admin.doctorStaffList))
            Admin.viewAllDoctorName()
            return "Added"
        return checkUserNameStatement
 
    def checkUserName(userName):
        for i in Admin.doctorStaffList:
            if i.userName == userName:
                return False,"User Exits"
        return True, "User dose not Exits" 
    
    def findDoctorStaff(userName):
        for i in Admin.doctorStaffList:
            if i.userName == userName:
                return True,i
        return False, None  
    def findDoctorStaffWithFirstNameSerialNumber(firstName,serailNumber):
        for i in range(0,len(Admin.doctorStaffList),1):
            print(Admin.doctorStaffList[i].firstName)
            if  i== serailNumber and Admin.doctorStaffList[i].firstName == firstName:
                return True,Admin.doctorStaffList[i].userId
        return False, None 

    def updateDoctorStaff(userName, propertyName, newValue):
        valueOfFindDoctorStaff, objectOfFindDoctorStaff = Admin.findDoctorStaff(userName)
        if valueOfFindDoctorStaff:
            print(propertyName)
            setattr(objectOfFindDoctorStaff,propertyName,newValue)
            Admin.viewDoctor()            
        return valueOfFindDoctorStaff
    def giveSalary(self):
        for i in Admin.doctorStaffList:
            i.salary += self.balance / len(Admin.doctorStaffList)
            return "salary Paid"
        return "Insufficent Balance "
    def deleteDoctorStaff(userName):
        valueOfcheckUserName, checkUserNameStatement = Admin.checkUserName(userName)
        if not valueOfcheckUserName:
            for i in Admin.doctorStaffList:
                if i.userName == userName:
                    Admin.doctorStaffList.remove(i)
                    return print("Deleted")
        return (checkUserNameStatement)

    @staticmethod
    def viewAllDoctorName():
        for i in range(0,len(Admin.doctorStaffList),1):
            if Admin.doctorStaffList[i].isDoctor:
                print(i," ",Admin.doctorStaffList[i].firstName)
    @staticmethod
    def viewAllStaffName():
        for i in range(0,len(Admin.doctorStaffList),1):
            if not Admin.doctorStaffList[i].isDoctor:
                print(Admin.doctorStaffList[i].firstName)
