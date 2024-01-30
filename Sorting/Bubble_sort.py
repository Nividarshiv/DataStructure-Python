elements = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]

#Sort by ascending order based on name
for i in range(len(elements)-1,0,-1):
    for j in range(i):
        if elements[j]["name"]>elements[j+1]["name"]:
            elements[j],elements[j+1]=elements[j+1],elements[j]
for i in range(len(elements)): 
    print(elements[i])    


#Sort by descending order based on transaction amount
for i in range(len(elements)-1,0,-1):
    for j in range(i):
        if elements[j]["transaction_amount"]<elements[j+1]["transaction_amount"]:
            elements[j],elements[j+1]=elements[j+1],elements[j]
for i in range(len(elements)): 
    print(elements[i])    
