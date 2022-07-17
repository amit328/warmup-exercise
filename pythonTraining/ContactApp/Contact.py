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

    

