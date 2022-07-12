f = open("input.txt", "a")
f.write("Now the file has more content!")
print('amit')
# f.seek(0) 
try:
    content =f.read() 
    print(content)
except io.UnsupportedOperation as error:
    print(error)
else:
    print("amit")
finally:
    f.close()

#open and read the file after the appending:
# f = open("input.txt", "r")
# print(f.read())