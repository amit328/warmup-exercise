from Contact import Contact
class User:
    userId = -1
    contacts = []
    def __init__(self,userName,firstName,lastName,isAdmin,isActive):
        self.userName =userName
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
        user,objectUser = User.userExists(firstName)
        checkAdminValue, statementAdmin= User.checkAdmin(objectUser.isAdmin)
        if not checkAdminValue:
            return print(statementAdmin)
        if user is None:
            return print("User not Exists")    
        user.isActive = False

    def updateUser(newValue,firstName,propertyUser):
        user, objectUser = User.userExists(firstName)
        checkAdminValue, statementAdmin= User.checkAdmin(objectUser.isAdmin)
        if not checkAdminValue:
            return print(statementAdmin)
        if user is None:
            return print("User not Exists")
        objectUser.propertyUser = newValue
        return "Value Updated"

    def createContacDetails(contactFirstName,contactLastName,isActive):
        checkActiveValue, statementActive = User.checkActive(isActive)
        if checkActiveValue ==True :
            newConcact = Contact(contactFirstName,contactLastName,isActive)
            Contact.contactDetails.append(newConcact)
        return statementActive

    def deleteContact(contactFirstName):
        contact,objectContact = Contact.contactExists(contactFirstName)
        checkActiveValue, statementActive = User.checkActive(objectContact.isActive)
        if not checkActiveValue:
            return print(statementActive)
        if contact is None:
            return print("Contact not Exists") 
        contact.isActive = False
    
    def readContact(contactFirstName):
        contact,objectContact = Contact.contactExists(contactFirstName)
        checkActiveValue, checkActiveValue = User.checkActive(objectContact.isActive)
        if not checkActiveValue:
            return print(checkActiveValue)
        if contact is None:
            return print("Contact not Exists")
        print("First name: ",objectContact.firstName)
        print("Last Name:" ,objectContact.lastName)
        print("Admin Status: ",objectContact.isAdmin)
        print("Active Status: ",objectContact.isActive)
        print("Contact Id: ",objectContact.contactId)
        if objectContact.phone:
            print("Phone Number: ",objectContact.phone)
        if objectContact.email:
            print("Email: ",objectContact.email)


    def updateContact(newValue,contactFirstName,propertyUser):
        contact, objectContact = Contact.contactExists(contactFirstName)
        checkActiveValue, checkActiveValue = User.checkActive(objectContact.isActive)
        if not checkActiveValue:
            return print(checkActiveValue)
        if contact is None:
            return print("Contact not Exists")
        setattr(objectContact,propertyUser,newValue )
        return "Value Updated"

    def readUser(firstName):
        user, objectUser = User.userExists(firstName)
        checkAdminValue, statementAdmin= User.checkAdmin(objectUser.isAdmin)
        if not checkAdminValue:
            return print(statementAdmin)
        if user is None:
            return print("User not Exists")
        print("First name: ",objectUser.firstName)
        print("Last Name:" ,objectUser.lastName)
        print("Admin Status: ",objectUser.isAdmin)
        print("Active Status: ",objectUser.isActive)
        print("User Id: ",objectUser.userId)

        
