import json

class Employee:
    def __init__(self, name, designation, age) -> None:
        self.name = name
        self.designation = designation
        self.age = age
        self.subordinates = []

    def addSubordinate(self, name, designation, age):
        subordinate = Employee(name, designation, age)
        self.subordinates.append(subordinate)
        return subordinate


amit = Employee('Amit Chhabria', 'CFO', 50)

jash = amit.addSubordinate('Jash Bhatiya', 'VP', 30)
jay = amit.addSubordinate('Jay Dhulera', 'VP', 30)

neel = jash.addSubordinate('Neel Bhagat', 'Regional Manager', 30)
omkar = neel.addSubordinate('Omkar Jadhav', 'Salesman', 50)
sanket = neel.addSubordinate('Sanket Chaudhary', 'Salesman', 50)

arnav = jash.addSubordinate('Arnav Bagchi', 'Regional Manger', 20)
rohan = arnav.addSubordinate('Rohan Gosalkar', 'Accountant', 30)


print('\n AS JSON \n')
data = json.dumps(amit, default=lambda o: o.__dict__, indent = 4)
print(data)



# output

#  AS JSON

# {
#     "name": "Amit Chhabria",
#     "designation": "CFO",
#     "age": 50,
#     "subordinates": [
#         {
#             "name": "Jash Bhatiya",
#             "designation": "VP",
#             "age": 30,
#             "subordinates": [
#                 {
#                     "name": "Neel Bhagat",
#                     "designation": "Regional Manager",
#                     "age": 30,
#                     "subordinates": [
#                         {
#                             "name": "Omkar Jadhav",
#                             "designation": "Salesman",
#                             "age": 50,
#                             "subordinates": []
#                         },
#                         {
#                             "name": "Sanket Chaudhary",
#                             "designation": "Salesman",
#                             "age": 50,
#                             "subordinates": []
#                         }
#                     ]
#                 },
#                 {
#                     "name": "Arnav Bagchi",
#                     "designation": "Regional Manger",
#                     "age": 20,
#                     "subordinates": [
#                         {
#                             "name": "Rohan Gosalkar",
#                             "designation": "Accountant",
#                             "age": 30,
#                             "subordinates": []
#                         }
#                     ]
#                 }
#             ]
#         },
#         {
#             "name": "Jay Dhulera",
#             "designation": "VP",
#             "age": 30,
#             "subordinates": []
#         }
#     ]
# }