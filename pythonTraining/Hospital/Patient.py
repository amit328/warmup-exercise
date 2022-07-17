
from User import User

class Patient(User):
    def __init__(self,userName, firstName, lastName, age, address, gender, dob,password,patientDetails,patientProblem):
        self.patientDetails = patientDetails
        self.patientProblem = patientProblem
        self.balance = 0
        super().__init__(userName,firstName, lastName, age, address, gender, dob,password)
        pass
    @staticmethod
    def createPatient(userName,firstName, lastName, age, address, gender, dob,password,patientDetails,patientProblem):
        newUser = Patient(userName, firstName, lastName, age, address, gender, dob,password,patientDetails,patientProblem)
        return newUser

    def selectDoctor(userName):
        from DoctorStaff import DoctorStaff
        DoctorStaff.doctorPairPatient(userName)

    def getReport(userUid):
        from DoctorStaff import DoctorStaff
        for i in range (0,len(DoctorStaff.doctorOpinion),1):
            if DoctorStaff.doctorOpinion[i].userUid:
                indexOfUserId = i
        return DoctorStaff.doctorOpinion[indexOfUserId +1]
    
    def requestBed(userUid):
        from DoctorStaff import DoctorStaff
        if Patient.getReport(userUid):
            bedStatus,patientBedNo =DoctorStaff.grantBed(userUid)
            if bedStatus:
                print(patientBedNo)
            return bedStatus
        return False

    def viewPayment(self,userId):
        from DoctorStaff import DoctorStaff
        if self.balance ==0:
            return "No payment to be done"
        if userId in DoctorStaff.bedPairPatient:
            self.balance += 1000
            return self.balance
        self.balance += 500
        return self.balance 

    def makePayemnt(self,paymetbalance,userId):
        from DoctorStaff import DoctorStaff
        from Admin import Admin
        if userId in DoctorStaff.doctorPatientList:
            Admin.balance += paymetbalance
            self.balance -= paymetbalance

