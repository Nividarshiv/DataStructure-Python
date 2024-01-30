def swap(a,b,arr):
    if a!=b:
        arr[a],arr[b]=arr[b],arr[a]
    
def partition(element,start,end):
    pivot_index=start
    pivot_number=element[pivot_index]

    while start<end:
        while start<len(element) and element[start]<=pivot_number:
            start+=1
        while element[end]>pivot_number:
            end-=1           
        if start<end:     
             swap(start,end,element)      

    swap(pivot_index,end,element)   
    return end

def quicksort(element,start,end):
    if start<end:                   
        pi=partition(element,start,end)
        quicksort(element,start,pi-1)
        quicksort(element,pi+1,end)

element=[11,4,7,22,15,13]   
quicksort(element,0,len(element)-1)
print(element)
elements = ["mona", "dhaval", "aamir", "tina", "chang"]
quicksort(elements,0,len(elements)-1)
print(elements)



