lst=[
    {'First Name': 'Raj', 'Last Name': 'Nayyar'},
    {'First Name': 'Suraj', 'Last Name': 'Sharma'},
    {'First Name': 'Karan', 'Last Name': 'Kumar'},
    {'First Name': 'Jade', 'Last Name': 'Canary'},
    {'First Name': 'Raj', 'Last Name': 'Thakur'},
    {'First Name': 'Raj', 'Last Name': 'Sharma'},
    {'First Name': 'Kiran', 'Last Name': 'Kamla'},
    {'First Name': 'Armaan', 'Last Name': 'Kumar'}
]

#Ascending order based on First Name
for i in range(len(lst)):
    min=i
    for j in range(i,len(lst)):
        if lst[min]["First Name"]>lst[j]["First Name"]:
            min=j
    lst[i],lst[min]=lst[min],lst[i]        
for i in range(len(lst)):
    print(lst[i])


#Descending order based on Last Name
for i in range(len(lst)):
    min=i
    for j in range(i,len(lst)):
        if lst[min]["Last Name"]<lst[j]["Last Name"]:
            min=j
    lst[i],lst[min]=lst[min],lst[i]        
for i in range(len(lst)):
    print(lst[i])    
    