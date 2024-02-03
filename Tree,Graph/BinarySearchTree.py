class BinarysearchTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def append_data(self,val):    
        if self.data==val:
            return
        if val<self.data:
            if self.left:
                self.left.append_data(val)
            else:
                self.left=BinarysearchTreeNode(val)
        else:
            if self.right:
                self.right.append_data(val)
            else:
                self.right=BinarysearchTreeNode(val)      

    def in_order_traversal(self):      
        element=[]
        if self.left:
           element+=self.left.in_order_traversal()
        element.append(self.data) 
        if self.right:
            element+=self.right.in_order_traversal()
        return element
    
    def pre_order_traversal(self):   
        element=[]
        element.append(self.data)
        if self.left:
            element+=self.left.pre_order_traversal()
        if self.right:
            element+=self.right.pre_order_traversal()  
        return element    

    def post_order_traversal(self):      
        element=[]
        if self.left:
            element+=self.left.post_order_traversal()
        if self.right:
            element+=self.right.pre_order_traversal()
        element.append(self.data)        
        return element  
   
    def search(self,val):         
        if self.data==val:
            return True
        if val<self.data:
            if self.left:
                 return self.left.serach(val)        
            else:
                return False 
        if val>self.data:
            if self.right:
                 return self.right.search(val)
            else:
                return False
            
    def min(self):         
        if self.left is None:
            return self.data
        return self.left.min()   
    
    def max(self):       
        if self.right is None:
            return self.data
        return self.right.max()
    
    def cal(self):        
        leftsum=self.left.cal() if self.left else 0
        rightsum=self.right.cal() if self.right else 0
        return self.data+leftsum+rightsum
    
    def deletedata(self,val):
        if val<self.data:
            if self.left:
                self.left.deletedata(val)
        elif val>self.data:
            if self.right:
                self.right.deletedata(val)
        else:
            if self.left is None and self.right is None:
                return None    
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            min=self.right.min()
            self.data=min
            self.right.deletedata(min)            

def build_tree(elements):        
    root=BinarysearchTreeNode(elements[0])
    for i in range(1,len(elements)):
        root.append_data(elements[i])
    return root              

numbers=[17,4,1,20,9,23,18,34]
btree=build_tree(numbers)
print(btree.in_order_traversal())
print(btree.pre_order_traversal())
print(btree.post_order_traversal())
print(btree.search(22))
print(btree.min())
print(btree.max())
print(btree.cal())
btree.deletedata(20 )
print(btree.in_order_traversal())

