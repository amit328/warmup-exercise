import uuid
class User:
    def __init__(self,userName,firstName,lastName,age,address,gender,dob,password):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.address = address
        self.gender = gender
        self. dob = dob
        self.userName = userName
        self.password = password
        self.userId = uuid.uuid4()

    def login(userName,password):
        from Admin import Admin
        valueOfFindDoctorStaff, objectOfFindDoctorStaff = Admin.findDoctorStaff(userName)
        if valueOfFindDoctorStaff:
            objectOfFindDoctorStaff.password = password
            return True
        return False






