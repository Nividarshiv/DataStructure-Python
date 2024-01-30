#merge sort-Ascending order
def mergesort(arr1,arr2,element):
    len1=len(arr1)
    len2=len(arr2)
    i=j=k=0
    while i<len1 and j<len2:
        if arr1[i]<arr2[j]:
            element[k]=arr1[i]
            i+=1
        else:
           element[k]=arr2[j]
           j+=1
        k+=1
    while i<len1:
        element[k]=arr1[i]
        i+=1
        k+=1 
    while j<len2:
        element[k]=arr2[j]
        j+=1
        k+=1             

def merge(element):
    if len(element)<=1:
        return
    mid=len(element)//2
    left=element[:mid]
    right=element[mid:]
    merge(left)
    merge(right)
    mergesort(left,right,element)

lst=[43,57,125,15,75]    
merge(lst)
print(lst)


#merge sort-Ascending and Descending order 
elements = [
        { 'name': 'vedanth',   'age': 17, 'time_hours': 1},
        { 'name': 'rajab', 'age': 12,  'time_hours': 3},
        { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
        { 'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
    ]
def merge(arr,key,dec):
    if len(arr)<=1:
        return 1
    mid=len(arr)//2
    left=arr[:mid]
    right=arr[mid:]

    merge(left,key,dec)
    merge(right,key,dec)

    mergesort(left,right,arr,key,dec)

def mergesort(arr1,arr2,arr,key,dec):
    l1=len(arr1)
    l2=len(arr2)
    i=j=k=0
    if not dec:
     while i<l1 and j<l2:
        if arr1[i][key]<arr2[j][key]:
             arr[k]=arr1[i]  
             i+=1
        else:
            arr[k]=arr2[j]
            j+=1
        k+=1
     while i<l1:
        arr[k]=arr1[i]
        i+=1
        k+=1   
     while j<l2:
        arr[k]=arr2[j]
        j+=1
        k+=1

    else:
     while i<l1 and j<l2:
         if arr1[i][key]>arr2[j][key]:
             arr[k]=arr1[i]  
             i+=1
         else:
            arr[k]=arr2[j]
            j+=1
         k+=1
     while i<l1:
        arr[k]=arr1[i]
        i+=1
        k+=1   
     while j<l2:
        arr[k]=arr2[j]
        j+=1
        k+=1    

merge(elements,key="time_hours",dec=True)
for i in elements:
    print(i)
merge(elements,key="time_hours",dec=False)
for i in elements:
    print(i)    