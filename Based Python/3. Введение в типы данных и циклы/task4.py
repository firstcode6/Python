ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

new_list=[]
for value in ids.values():
    for spl_value in value:
        if spl_value not in new_list:
            new_list.append(spl_value)

print(new_list)