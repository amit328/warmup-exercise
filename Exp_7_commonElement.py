first_list= [1,2,3,4,6,7]
second_list= [2,3,4,5,6,9,8,7]
print("First List", first_list)
print("Second List", second_list)


# funtion with two integer as an input
def common_elemet(x,y):
    commonElemetList = []
    max_size = 0
    if (len(x) > len(y)):
        max_size = x
        for i in range(0,len(max_size),1):
            if(max_size[i] in y):
                commonElemetList.append(max_size[i])
        return commonElemetList
    else:
        max_size = y
        for i in range(0,len(max_size),1):
            if(max_size[i] in x):
                commonElemetList.append(max_size[i])
        return commonElemetList


common_elemet = common_elemet(first_list,second_list)
print("Common Element",common_elemet)