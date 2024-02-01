from collections import deque
import time
import threading

class Queue:
    def __init__(self):
        self.container=deque()
    def addqueue(self,data):
        self.container.appendleft(data)
    def popdequeue(self):
          if len(self.container)==0:
            print("Queue is empty")
            return       
          return self.container.pop()        
    def popdequeueleft(self):
        if len(self.container)==0:
            print("Queue is empty")
            return       
        return self.container.popleft()     
    def size(self):
        return len(self.container)   
    
q=Queue()
def orderplace(order):
    for i in order:
        q.addqueue(i)
        time.sleep(1)
        print("order:",i)    

def orderdeliver():
    while q.size()!=0:
        time.sleep(2)
        order=q.popdequeue()
        print("Deliver",order)    

orders = ['pizza','samosa','pasta','biryani','burger']        
thread1=threading.Thread(target=orderplace,args=(orders,))  
thread2=threading.Thread(target=orderdeliver)   
thread1.start()
time.sleep(1)
thread2.start()
thread1.join()
thread2.join()      

