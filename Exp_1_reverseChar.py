input_string = "amit"
char_array = []


for x in input_string:
    char_array.extend(x)
count = 0


print("Before reversed")
print(char_array)


for i in char_array:
    count+=1


for i in range(0, int(count/2), 1):
    temp = char_array[i]
    char_array[i] = char_array[count -1]
    char_array[count -1] = temp
    count =  count - 1
print("After reversed")

print(char_array) 

# shortcut method using sclicing
# print(char_array[::-1])