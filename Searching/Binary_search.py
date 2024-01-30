lst=[15,16,34,7,3,6]
lst.sort()
def Binary_search(lst,num):
    mid_index=0
    low=0
    upp=len(lst)-1
    while(low<=upp):
        mid_index=(low+upp)//2
        mid_num=lst[mid_index]
        if mid_num==num:
            return True
        elif mid_num<num:
            low=mid_index+1
        else:
            upp=mid_index-1
    return False
num=int(input("Enter the number to search : "))
result=Binary_search(lst,num)
if result:
    print("Number found in list")
else:
    print("Number not in list")


#Recursively Binary Search
def Rec_Binary_Search(lst,num,low,upp):
    if low>upp:
        return False
    mid_index=(low+upp)//2
    mid_num=lst[mid_index]
    if mid_num==num:
        return True
    elif mid_num<num:
       return Rec_Binary_Search(lst,num,mid_index+1,upp)
    else:
        return Rec_Binary_Search(lst,num,low,mid_index-1)    
num=int(input("Enter the number to search : "))
result=Rec_Binary_Search(lst,num,0,len(lst)-1)
if result:
    print("Number found in list")
else:
    print("Number not in list")    



   



