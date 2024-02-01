from collections import deque

class stack:
    def __init__(self):
        self.container=deque()
    def push(self,data):
        self.container.append(data)
    def pop(self):
        return self.container.pop()
    def peek(self):
        return self.container[-1]
    def length(self):
        return len(self.container)
    def  isempty(self):
        return len(self.container)==0

#Reverse the string 
def reversestring(st):
    stk=stack()
    print(st)
    for ch in st:
        stk.push(ch)
    rstr=''
    while stk.length()!=0:
        rstr+=stk.pop()
    print(rstr)       

s=stack()
s.push(75)
s.push(55)
s.push(1)
print(s.isempty())  
print(s.length())
print(s.pop()) 
print(s.peek()) 
print(s.container)    
reversestring("Welcome to this new world")

#2 paranthesis match
from collections import deque
class stack:
    def __init__(self):
        self.container=deque()
    def push(self,data):
        self.container.append(data)
    def pop(self):
        return self.container.pop()
    def peek(self):
        return self.container[-1]
    def length(self):
        return len(self.container)
    def  isempty(self):
        return len(self.container)==0
    
def match(ch,ch1):
    md = {
        ")":"(",
        "]":"[",
        "}":"{"
    }   
    return md[ch]==ch1 

def Tocheck(s):
    st=stack()
    for i in s:
       if i=='(' or i=='{' or i == '[':
           st.push(i)
       if i==')' or i=='}' or i == ']':    
           if st.length()==0:
               return False
           if not match(i,st.pop()):
               return False         
    return st.length()==0    

val=Tocheck("({a+b})")   
print(val)
print(Tocheck("))"))
print(Tocheck("((a+b))"))
