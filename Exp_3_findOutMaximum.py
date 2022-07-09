given_list =  [1,3,1,2,4]
print("Given listg" ,given_list)
def greter_number(a):
    for i in range (0,len(a)-1,1):
        if (a[i] > a[i+1]):
            b = a[i]
            if(b < a[len(a)-1]):
                b = a[len(a)-1]
                return b
            return b

firstNumber = greter_number(given_list)
if(firstNumber == None):
    firstNumber = (given_list[len(given_list)-1])


newList = []
for i in range (0,len(given_list),1):
    if (given_list[i] != firstNumber):
        newList.append(given_list[i])

secondNumber = greter_number(newList)
if(newList == []):
    secondNumber=firstNumber
if(secondNumber == None):
    secondNumber = (c[len(newList)-1])


print("First greatest number is : " + str(firstNumber) + " \nSecond greatest number is : " + str(secondNumber))