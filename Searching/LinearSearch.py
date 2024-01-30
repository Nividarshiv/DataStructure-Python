pos=-1
lst=[15,25,17,35,75]
def Linear_search(lst,num):
    global pos
    for i in range(len(lst)):
        if lst[i]==num:
            pos=i
            return
num=int(input("Enter number to search in list : "))
result=Linear_search(lst,num)
if pos!=-1:
    print("Number found in list")
else:
    print("Number not in list")     


#Recursively Linear Search     
lst=[15,25,17,35,75]
def  Rec_Linear_search(lst,curr_index,num):
    if curr_index==-1:
        return -1
    if lst[curr_index]==num:
        return curr_index   
    return Rec_Linear_search(lst,curr_index-1,num)    

num=int(input("Enter number to search in list : "))       
result=Rec_Linear_search(lst,len(lst)-1,num)
if result!=-1:
    print("Number found in list")
else:
    print("Number not in list")          




    
