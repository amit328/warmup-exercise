from Contact import Contact
from User import User


class ContactDetails:
    contactDetailsId = -1
    def __init__(self,number,email):
        self.number = number
        self.email = email
        ContactDetails.contactDetailsId +=1
        self.contactId = ContactDetails.contactDetailsId

    def createContactDetails(number,email,contactFirstName):
        checkActiveValue, statementActive = User.checkActive(isActive)
        if checkActiveValue ==True:
            contact,objectContact = Contact.contactExists(contactFirstName)
            setattr(objectContact, 'number', number)
            setattr(objectContact, 'email', email)
            return "Value Added"
        return statementActive
