givenNumber = 3.6
print("Given Number" , givenNumber)
count = 0
temp = givenNumber

while ( True ):
    temp = temp * 10
    count = count + 1
    temp2 = temp - int(temp)
    if(temp2 == 0):
        break
temp2 = givenNumber
temp2 = temp2 - int(temp2)


if(temp2 <= 0.5 and count == 1):
    print("Round off number is : " ,int(givenNumber))
elif (temp2 > 0.5 and  count == 1):
    print("Round off number is : " ,int(givenNumber)+1)
else:
    print("Number is more than and one decimal")

