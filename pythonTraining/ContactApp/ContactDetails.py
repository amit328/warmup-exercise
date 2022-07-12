from ContactApp import Contact
class ContactDetails:
    uuid = [] #list of customer uuid
    def __init__(self,email,phone):
        self.email = email
        self.phone = phone
    def createContactDetails(email,phone):
        isContactIsActive, contactStatus = Contact.checkConatctIsActive(ContactDetails.uuid)
        if isContactIsActive == True:
            newContactDetails = ContactDetails(email,phone)
            Contact.contactsDetails.append(newContactDetails)
            return "Updated"
        return "Not Updated"
    """Contact Detils update, delete and read will be done through Contact Page only"""
