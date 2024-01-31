class Node:
    def __init__(self,data,next,prev):
        self.data=data
        self.next=next
        self.prev=prev

class Doublelinkedlist:
    def __init__(self):
        self.head=None
        self.next=None
        self.prev=None   

    def insert_at_begining(self,data):
        if self.head is None:
            self.head=Node(data,None,None)
        else:    
             node=Node(data,self.head,None)
             self.head.prev=node  
             self.head=node

    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data,None,None)  
        else:
            itr=self.head
            while itr.next:
                itr=itr.next
            itr.next=Node(data,None,itr)   

    def length_doublelist(self):
        if self.head is None:
            return 0
        else:
            count=0
            itr=self.head   
            while itr:
                count+=1
                itr=itr.next
            return count             

    def insert_at_index(self,index,data):
        if index<0 or index>self.length_doublelist():
            print("Unbounded")
            return
        if index==0:
            self.insert_at_begining(data)    
        else:
            count=0
            itr=self.head 
            while itr:
                if count==index-1:
                    node=Node(data,itr.next,itr)               
                    itr.next=node
                itr=itr.next  
                count+=1     

    def remove_at_index(self,index): 
        if index<0 or index>=self.length_doublelist():
            print("Unbonded")
        if index==0:
            self.head=self.head.next
            self.head.pre=None
        else:
            count=0
            itr=self.head
            while itr.next:
                if count==index-1:
                    itr.next=itr.next.next
                    break
                itr=itr.next 
                count+=1        

    def insert_list(self,dlist):
        for data in dlist:
            self.insert_at_end(data)   

    def remove_values(self,data):
        if self.head.data==data:
            self.head=self.head.next 
            self.head.prev=None
        else:
            itr=self.head 
            while itr.next:
                if itr.next.data==data:
                    itr.next=itr.next.next
                    break
                itr=itr.next      

    def insert_after_values(self,dataafter,data):
        if self.head.data==dataafter:
            self.head.next=Node(data,self.head.next,self.head)
        else:
            itr=self.head
            while itr:
                if itr.data==dataafter:
                    itr.next=Node(data,itr.next,itr)
                    break
                itr=itr.next    
             
    def printdoubleLinklist(self):
        itr=self.head
        dlstr=""
        while itr:    
            dlstr+=str(itr.data)+"-->"
            itr=itr.next
        print(dlstr)    

dll=Doublelinkedlist()
dll.insert_list([13,15,17])
dll.insert_at_begining(75)
dll.insert_at_end(555)
dll.insert_at_index(3,1000)
dll.insert_after_values(13,"Python")
dll.insert_at_index(7,333333)
dll.remove_values(333333)
dll.remove_at_index(6)
dll.printdoubleLinklist()
print(dll.length_doublelist())

