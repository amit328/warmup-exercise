gievn_list = [1,2,3,5,8, 10,88,1,3]


count = 0
new_list = []
new_list_repeat = []
no_repet =[]
count_no_repet =[]

for i in range(0,len(gievn_list), 1):
    if(gievn_list.count(gievn_list[i]) > 1):
        new_list.append(gievn_list[i])
        new_list_repeat.append(gievn_list.count(gievn_list[i]))
    else:
        no_repet.append(gievn_list[i])
        count_no_repet.append(1)

new_list.sort()

unique_list = []
unique_list_count = []
for i in range(0, len(new_list),1):
    if new_list[i] not in unique_list:
        unique_list.append(new_list[i])
        unique_list_count.append(new_list_repeat[i])

final_list = no_repet + unique_list
count_list  = count_no_repet + unique_list_count

print("given list:\t\t\t",final_list)
print("number of time value appeared:\t",count_list)
