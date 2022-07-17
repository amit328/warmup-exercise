
from User import User
from Patient import Patient
from Bed import Bed
class DoctorStaff(User):
    patientList = []
    doctorPatientList = []
    doctorOpinion = []
    bedPairPatient =[]
    def __init__(self, userName, firstName, lastName, age, address, gender, dob,password,isDoctor,salary):
        self.isDoctor = isDoctor
        self.salary=salary
        super().__init__(userName,firstName, lastName, age, address, gender, dob,password)
    @staticmethod
    def createDoctorStaff(userName,firstName, lastName, age, address, gender, dob,password,isDoctor):
        newUser = DoctorStaff(userName, firstName, lastName, age, address, gender, dob,password,isDoctor,salary=0)
        return newUser

    def checkPatientUserName(userName):
        for i in DoctorStaff.patientList:
            if i.userName == userName:
                return False,"User Exits"
        return True, "User dose not Exits" 

    def createPatient(staffUserName,staffPassword,userName, firstName, lastName, age, address, gender, dob,password,patientDetails,patientProblem):
        if User.login(staffUserName,staffPassword):
            newPatient = Patient.createPatient(userName,firstName, lastName, age, address, gender, dob,password, patientDetails,patientProblem)
            DoctorStaff.patientList.append(newPatient)



    def deletePatient(staffUserName,staffPassword,userName):
        if User.login(staffUserName,staffPassword):
            valueOfcheckUserName, checkUserNameStatement = DoctorStaff.checkPatientUserName(userName)
            if not valueOfcheckUserName:
                for i in DoctorStaff.patientList:
                    if i.userName == userName:
                        DoctorStaff.patientList.remove(i)
                        return print("Deleted")
            return (checkUserNameStatement)

    def findPatientStaff(userName):
        for i in DoctorStaff.patientList:
            print(i.userName)
            if i.userName == userName:
                return True,i.userId
        return False, None  

    def updatePatient(staffUserName,staffPassword,userName, propertyName, newValue):
        if User.login(staffUserName,staffPassword):
            valueOfFindDoctorStaff, objectOfFindDoctorStaff = DoctorStaff.findPatientStaff(userName)
            if valueOfFindDoctorStaff:
                setattr(objectOfFindDoctorStaff,propertyName,newValue)
                DoctorStaff.viewPatient()            
            return valueOfFindDoctorStaff
    @staticmethod
    def viewAllPatient():
        for i in range(0,len(DoctorStaff.patientList),1):
            print(DoctorStaff.patientList[i].firstName)
    def findPatientUuid(userName):
        for i in DoctorStaff.patientList:
            if i.userName == userName:
                return True,i
        return False, None 

    def doctorPairPatient(userName):
        from Admin import Admin
        Admin.viewAllDoctorName()
        print("select one doctor with serial number")
        doctorName = input("Doctor Name: ")
        serailNumber = int(input ("Serial Number: "))
        bollValueOfDoctor, doctorUuid =Admin.findDoctorStaffWithFirstNameSerialNumber(doctorName,serailNumber)
        bollValueOfPatient, patientUuid = DoctorStaff.findPatientStaff(userName)
        print(bollValueOfDoctor)
        print(bollValueOfPatient)
        if bollValueOfDoctor and bollValueOfPatient:
            doctorPatient = []
            doctorPatient.append(doctorUuid)
            doctorPatient.append(patientUuid)
            DoctorStaff.doctorPatientList.append(doctorPatient)
            print(DoctorStaff.doctorPatientList[0][0])
        return

    def createdoctorOpinion(userNameuid,useruid):
        for i in range(0,(),len(DoctorStaff.patientList),1):
            for j in DoctorStaff.patientList[i]:
                if j in userNameuid and j in useruid:
                    doctorOpinionInBoolean = True
                    DoctorStaff.doctorOpinion.append(useruid)
                    DoctorStaff.doctorOpinion.append(doctorOpinionInBoolean)
                    return doctorOpinionInBoolean,useruid
        return False

    def dischargePatient(doctorUid,patientUid):
        for i in range(0,len(DoctorStaff.patientList),1):
            for j in DoctorStaff.patientList[i]:
                if j in doctorUid and j in patientUid:
                    dischargeStatus = True
                    return dischargeStatus
        return False

    def grantBed(patientUserId):
        bedAvailable, bedSerialNo = Bed.createBed()
        if bedAvailable:
            DoctorStaff.bedPairPatient.append(patientUserId)
            DoctorStaff.bedPairPatient.append(bedSerialNo)
            return "Created Bed",bedSerialNo
        return "Bed not Created", " "
    
    def deleteBed(patientUserId,doctorUid):
        bedStatus, bedSerialNo = Bed.deleteBed()
        dischargePatientStaus = DoctorStaff.dischargePatient(doctorUid,patientUserId)
        if bedStatus and dischargePatientStaus:
            DoctorStaff.bedPairPatient.remove(patientUserId)
            DoctorStaff.bedPairPatient.remove(bedSerialNo)
            return "Deleted Bed",bedSerialNo
        return "Could not delete", " "

