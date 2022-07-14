class User:
    userId = -1
    contacts = []
    def __init__(self,firstName,lastName,isAdmin,isActive):
        self.firstName = firstName
        self.lastName = lastName
        self.isActive = isActive
        self.isAdmin = isAdmin
        User.userId += 1
        self.userId = User.userId
        self.contacts = User.contacts

    @staticmethod
    def checkAdmin(isAdmin):
        if isAdmin == True:
            return True, "User have admin rights"
        return False, " User do not have rights to add other user"
    @staticmethod
    def checkActive(isActive):
        if isActive == True:
            return True, "User is Active"
        return False, " User is not active"
    @staticmethod
    def userExists(firstName):
        for i in User.contacts:
            if i.firstName == firstName:
                return True,i
        return False,None

    def createUser(firstName,lastName,isAdmin,isActive):
        checkActiveValue, statementActive = User.checkActive(isActive)
        checkAdminValue, statementAdmin= User.checkAdmin(isAdmin)
        if checkActiveValue and checkAdminValue ==True :
            newUser = User(firstName,lastName,isAdmin,isActive)
            User.contacts.append(newUser)
        return "You are not Admin and Active User"


    def deleteUser(firstName):
        checkAdminValue, statementAdmin= User.checkAdmin(isAdmin)
        if not checkAdminValue:
            return print(statementAdmin)
        user,objectUser = User.userExists(firstName)
        if user is None:
            return print("User not Exists")    
        user.isActive = False

    def updateUser(newValue,firstName,propertyUser):
        checkAdminValue, statementAdmin= User.checkAdmin(isAdmin)
        if not checkAdminValue:
            return print(statementAdmin)
        user, objectUser = User.userExists(firstName)
        if user is None:
            return print("User not Exists")
        objectUser.propertyUser = newValue
        return "Value Updated"
    
    def readUser(firstName):
        checkAdminValue, statementAdmin= User.checkAdmin(isAdmin)
        if not checkAdminValue:
            return print(statementAdmin)
        user, objectUser = User.userExists(firstName)
        if user is None:
            return print("User not Exists")
        print("First name: ",objectUser.firstName)
        print("Last Name:" ,objectUser.lastName)
        print("Admin Status: ",objectUser.isAdmin)
        print("Active Status: ",objectUser.isActive)
        print("User Id: ",objectUser.userId)

        
