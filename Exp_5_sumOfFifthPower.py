fifth_power = []
def split_number(number):
    digits = []
    while (number > 0):
        digits.append((number%10))
        number //=10
    return digits[:: -1]


for i in range(2,1000000,1):
    splitNumberValue = split_number(i)
    total = 0
    for j in range(0,len(splitNumberValue),1):
        total = total + (splitNumberValue[j]**5)
        if ( i == total ):
            fifth_power.append(i)

print(list(set(fifth_power)))


