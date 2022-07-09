gievn_list = [1,2,3,5,8, 10,88,1,3,8,8,8,8,3,3,3,3,7,7,7,7,7,7,7]
print("Given List", gievn_list)
count = 0

def offenFunction(a):
    new_list = []
    new_list_repeat = []
    no_repet =[]
    count_no_repet =[]
    for i in range(0,len(a), 1):
        if(a.count(a[i]) > 1):
            new_list.append(a[i])
            new_list_repeat.append(a.count(a[i]))
        else:
            no_repet.append(a[i])
            count_no_repet.append(1)
    unique_list = []
    unique_list_count = []
    for i in range(0, len(new_list),1):
        if new_list[i] not in unique_list:
            unique_list.append(new_list[i])
            unique_list_count.append(new_list_repeat[i])
    final_list =[]
    max_number = max(unique_list_count)
    for i in range(0, len(unique_list),1):
        if(max_number == unique_list_count[i]):
            final_list.append(unique_list[i])
    return final_list
final = offenFunction(gievn_list)
print(final)

