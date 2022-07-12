
from ContactApp import User
from ContactApp import ContactDetails
class Contact:
    contactId = -1
    contactsDetails = []
    uuid = [] #list of customer uuid
    def __init__(self,contactFirstname,isActivte,contactLastName):
        self.contactFirstname = contactFirstname
        self.contactLastName = contactLastName
        self.isActivte = isActivte
        Contact.contactId += 1

    @staticmethod
    def checkConatctIsActive(uuid):
        for i in Contact.contactsDetails:
            if uuid == i.uuid and i.contactsDetails.isActive == True:
                return True, "Staff is active"
        return False, "Staff is not active"         
    @staticmethod
    def checkConatctIsAvailable(uuid):
        for i in Contact.contactsDetails:
            if uuid == i.uuid and i.contactsDetails.isActive == True:
                return True,i
        return False, "Staff is not Available"  

    @staticmethod
    def createContact(contactFirstname,contactLastName,isActive):
        userExits,object = User.userExists(Contact.uuid)
        """Here uuid will check with User asuming it will be given"""
        if userExits:
            if isActive == True:
                newContact = Contact(contactFirstname,contactLastName,isActive)
                Contact.contactsDetails.append(newContact,Contact.uuid)
                return True, "Contact Added"
            else:
                return False, "Dosent Have staff Permission"
        else:
            return False, "User Dossend Exists"
    @staticmethod
    def findContactToUpdate(contactFirstname):
        for i in Contact.contactsDetails:
                if i.contactFirstname == contactFirstname:
                    return True,(i,i.contactsDetails)
        return False, None  
    @staticmethod
    def checkConatctIsActiveInContact(isActive):
        if isActive == True:
            return True, "Can delete"
        return False, "Cant Delete"

    def deleteContact(contactFirstname):
        isContactExist, contactObject = Contact.findContactToUpdate(contactFirstname)
        if isContactExist and Contact.checkConatctIsActiveInContact(contactObject[0].isActive):
            contactObject[0].isActive = False
            return True, "Deleted User"
        return False," Cant delete the User"

    def updateContact(contactFirstname,isActive,contactLastName,email,phone):
        isUserExist, userObject = Contact.findContactToUpdate(contactFirstname)
        if isUserExist and User.checkConatctIsActiveInContact(userObject[0].isAdmin):
            userObject[0].contactLastName = contactLastName
            userObject[0].isActive = isActive
            userObject[1].email = email
            userObject[1].phone = phone

        
            return True, "Updated new value"
        return False, "Cant update Contact"
    def ContactDetailsAvailable(uuid):
        if ContactDetails.uuid in Contact.uuid:
            return True,"Exists Contact Details"
        return False, "Not Exits Contact Details"

    def readContact(uuid):
        isAvailable, statement = Contact.ContactDetailsAvailable(uuid)
        for i in Contact.contactsDetails:
            if uuid == i.uuid:
                return True,(i, i.ContactDetails)
        return False, "User  doesnot Exits" 