from User import User
class Contact:
    contactId = -1
    contactDetails = []

    def __init__(self,contactFirstName,contactLastName,isActive):
        self.contactFirstName = contactFirstName
        self.contactLastName = contactLastName
        self.isActive = isActive
        Contact.contactId += 1
        self.contactId = Contact.contactId

    @staticmethod
    def contactExists(contactFirstName):
        for i in Contact.contactDetails:
            if i.contactFirstName == contactFirstName:
                return True,i
        return False,None

    def createContacDetails(contactFirstName,contactLastName,isActive):
        checkActiveValue, statementActive = User.checkActive(isActive)
        if checkActiveValue ==True :
            newConcact = Contact(contactFirstName,contactLastName,isActive)
            Contact.contactDetails.append(newConcact)
        return statementActive
    
    def deleteContact(contactFirstName):
        checkActiveValue, statementActive = User.checkActive(isActive)
        if not checkActiveValue:
            return print(statementActive)
        contact,objectContact = Contact.contactExists(firstName)
        if contact is None:
            return print("Contact not Exists") 
        contact.isActive = False

    def updateContact(newValue,contactFirstName,propertyUser):
        checkActiveValue, checkActiveValue = User.checkActive(isActive)
        if not checkActiveValue:
            return print(checkActiveValue)
        contact, objectContact = Contact.contactExists(contactFirstName)
        if contact is None:
            return print("Contact not Exists")
        objectContact.propertyUser = newValue
        return "Value Updated"
    
    def readContact(contactFirstName):
        checkActiveValue, checkActiveValue = User.checkActive(isActive)
        if not checkActiveValue:
            return print(checkActiveValue)
        contact,objectContact = Contact.contactExists(firstName)
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
