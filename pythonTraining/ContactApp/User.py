class User:
    userId = -1
    contacts = []
    uuid = [] #list of user uuid
    def __init__(self,firstName,lastName,isAdmin,isActive):
        self.firstName = firstName
        self.lastName = lastName
        self.isAdmin = isAdmin
        self.isActive = isActive
        User.userId += 1
        self.userId = User.userId
    @staticmethod
    def checkAdmin(isAdmin):
        if isAdmin == True:
            return True
        return False
    @staticmethod
    def userExists(userId):
        for i in User.contacts:
            if i.userId == userId:
                return True,i
        return False, "User Not Exists"
    @staticmethod
    def createUser(firstName, lastName,isAdmin,isActive):
        checkadmin = User.checkAdmin(isAdmin)
        if not checkadmin:
            return False, "Not a admin can not create a user"
        newUser = User(firstName,lastName,isAdmin,isActive)
        User.contacts.append(newUser, User.uuid)
        return True, "user Added"

    def deleteUser(firstName):
        isUserExist, userObject = User.findUserToUpdate(firstName)
        if isUserExist and User.checkAdmin(userObject.isAdmin):
            userObject.isActive = False
            return True, "Deleted User"
        return False," Cant delete the User"
    @staticmethod
    def findUserToUpdate(firstName):
        for i in User.contacts:
                if i.firstName == firstName:
                    return True,i
        return False, None  

    def updateUser (firstName, lastName,isAdmin,isActive):
        isUserExist, userObject = User.findUserToUpdate(firstName)
        if isUserExist and User.checkAdmin(userObject.isAdmin):
            userObject.lastName = lastName
            userObject.isAdmin = isAdmin
            userObject.isActive = isActive
            return True, "Updated new value"
        return False, "Cant update User"

    @staticmethod
    def readUser(uuid):
        for i in User.contacts:
            if uuid == i.uuid:
                return True,i
        return False, "User  doesnot Exits" 
        


        
            
            




