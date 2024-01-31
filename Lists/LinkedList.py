class Node:
    def __init__(self,data,next): 
        self.data=data
        self.next=next

class Linkedlist: 
    def __init__(self):          
        self.head=None 

    def insert_at_begining(self,data):         
        node=Node(data,self.head)
        self.head=node

    def printlist(self):                 
        if self.head==None: 
            print("The Linkedlist Empty")
            return
        llstr=""
        itr=self.head
        while itr:
            llstr+=str(itr.data)+"-->"
            itr=itr.next
        print(llstr)   

    def insert_at_end(self,data):          
        if self.head==None:
            self.head=Node(data,None)
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None)       

    def getlengthlist(self):                
        if self.head==None:  
            return 0
        else:
            count=0
            itr=self.head
            while itr:
                count+=1
                itr=itr.next        
        return count

    def CreateNew_list(self,data_list):    
        self.head=None
        for data in data_list:
            self.insert_at_end(data) 

    def append_Existinglist(self,data_list):     
        for data in data_list:
            self.insert_at_end(data)   

    def remove_at_index(self,index):           
        if index<0 or index>=self.getlengthlist():
            print("Unbounded index")          
            return    
        if index==0:
            self.head=self.head.next
            return
        count=0
        itr=self.head
        while itr:       
            if count==index-1:
                itr.next=itr.next.next
                break                
            itr=itr.next
            count+=1

    def insert_at_index(self,index,data):
        if index<0 or index>self.getlengthlist():
            print("Unbounded index")
            return
        if index==0:
            self.insert_at_begining(data)     
            return
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                node=Node(data,itr.next)
                itr.next=node
                break
            itr=itr.next
            count+=1   

    def insert_aftervalues(self,dataafter,datainsert):      
        if self.head is None:
            return       
        itr=self.head
        while itr:
            if dataafter==itr.data:
                itr.next=Node(datainsert,itr.next)
                break
            itr=itr.next       

    def remove_by_values(self,val):
        if self.head is  None:
            return      
        if self.head.data==val:
            self.head=self.head.next
            return
        itr=self.head
        while itr.next:
            if itr.next.data==val:
                itr.next=itr.next.next 
                break
            itr=itr.next      

ll=Linkedlist()
ll.insert_at_begining(25)
ll.append_Existinglist([13,17,15,37])
ll.insert_at_begining(75)
ll.insert_at_end(125)
ll.insert_aftervalues(13,45)
ll.insert_at_index(3,275)
ll.remove_at_index(3)
ll.remove_by_values(13)
ll.printlist()  
print(ll.getlengthlist())
ll.CreateNew_list([13,17,15])
ll.printlist()      

