import sys
class User:
    def __init__(self,userId,fname,lname,isAdmin,isActive,contacts):
        self.userId = userId
        self.fname = fname
        self.lname =lname
        self.isAdmin = isAdmin
        self.isActive = isActive
        self.contacts = contacts
        if(isAdmin == True):
            if(contacts == []):
                contacts.append(fname)
            callAdmin = Admin(userId,fname,lname,isAdmin,isActive,contacts)
        else:
            if(contacts == []):
                userId = userId +1
                contacts.append(fname)
            callStaff = Staff(userId,fname,lname,isAdmin,isActive,contacts)
    @staticmethod
    def contacts(userId,fname,lname,isAdmin,isActive):
        contacts = []
        contacts.append(fname)
        return User(userId,fname,lname,isAdmin,isActive,contacts)
    def showContacts(self,contacts,userId):
        print("List of all the user",contacts)
    def updateContacts(self,contacts):
        print(contacts)
        newvalue = int(input("enter the number from the list to  be updated"))
        contacts.pop(newvalue -1)
        newName = input('Enter New name')
        contacts.insert(newvalue -1, newName)
        print("updated user list", contacts)

class Admin(User):
    def __init__(self,userId,fname,lname,isAdmin,isActive,contacts):
        while(True):
            print("Hello " + fname)
            print("Press\n 1 To add new admin\n 2 To add new Staff \n 3 Read all the admin\n 4 Read all the staff\n 5 update Admin\n 6 Update Staff\n 7 Delete Admin\n 8 Delete Staff\n 9 press to exit")
            adminInput = int(input())
            if(adminInput == 1 and isAdmin==True ):
                contactFname =input("Enter Persons First name ")
                contactLname =input("Enter Persons Last name ")
                print(contactFname)
                userId = userId +1
                contacts.append(contactFname)
                callContact = Contact(userId,fname,lname,isAdmin,isActive,1,contactFname,contactLname,True)
            elif(adminInput == 2 and isAdmin==True):
                contactFname =input("Enter Persons First name ")
                contactFname =input("Enter Persons Last name ")
                addStaff = Staff(userId + 1 ,contactFname,contactFname,False,True,[])
                # invoke admin
            elif(adminInput == 3 and isAdmin==True):
                super().showContacts(contacts,userId)
                pass
            elif(adminInput == 4 and isAdmin==True):
                pass
            elif(adminInput == 5 and isAdmin==True):
                super().showContacts(contacts,userId)
                super().updateContacts(contacts)
            elif(adminInput == 6 and isAdmin==True):
                pass
            elif(adminInput == 7 and isAdmin==True):
                super().showContacts(contacts,userId)
                newvalue = int(input("enter the number from the list to  be updated "))
                contactIsActive == False
            elif(adminInput == 8 and isAdmin==True):
                pass
            elif(adminInput== 9 and isAdmin==True):
                sys.exit()
class Staff(User):
    def __init__(self,userId,fname,lname,isAdmin,isActive,contacts):
        while(True):
            print("Hello " + fname)
            print("Press\n 1 To add new User\n 2 Read all the User\n 3 update User\n 4 Delete User\n 5 press to exit\n 6 Main Menu")
            staffInput = int(input())
            if(staffInput== 1 and isAdmin==False):
                contactFname =input("Enter Persons First name ")
                contactLname =input("Enter Persons Last name ")
                userId = userId +1
                contacts.append(contactFname)
                callContact = Contact(userId,fname,lname,isAdmin,isActive,1,contactFname,contactLname,True)
            elif(staffInput == 2 and isAdmin==False):
                super().showContacts(contacts,userId)
            elif(staffInput == 3 and isAdmin == False):
                super().showContacts(contacts,userId)
                super().updateContacts(contacts)

                pass
            elif(staffInput == 4 and isAdmin ==False):
                super().showContacts(contacts,userId)
                newvalue = int(input("enter the number from the list to  be updated "))
                contactIsActive == False
            elif(staffInput == 5 and isAdmin == False):
                sys.exit()
            elif(staffInput == 6 and isAdmin == False):
                getDetails = input('Enter A for Admin, S for Staff ')
                if(getDetails == 'A'):
                    defaultAdmin = User(1,"admin","admin",True,True,[])
                elif(getDetails == 'S'):
                    defaultStaff = User(1,"staff","staff",False,True,contacts)
class Contact(Admin,Staff):
    def __init__(self,userId,fname,lname,isAdmin,isActive,contactId,contactFname,contactLname,contactIsActive):
        self.contactId = contactId
        self.contactFname =contactFname
        self.contactLname = contactLname
        self.contactIsActive = contactIsActive
        print(fname)
        if(self.contactIsActive==True):
            print("Add contact details ")
            contactNumber = input("Type Phone Number ")
            contactEmail = input("Type Email id ")
            callContactDetails = (1,contactNumber,contactEmail)
class ContactDetails():
    def __init__(self,contactDetailsid,contactNumber,contactEmail):
        self.contactDetailsid = contactDetailsid
        self.contactNumber = contactNumber
        self.contactEmail = contactEmail
        print(contactEmail)
if __name__ == "__main__":
    getDetails = input('Enter A for Admin, S for Staff ')
    if(getDetails == 'A'):
        defaultAdmin = User(1,"admin","admin",True,True,[])
    elif(getDetails == 'S'):

        defaultStaff = User.contacts(1,"staff","staff",False,True)
    else:
        print("Wrong Value Entered")
