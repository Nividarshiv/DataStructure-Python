#Weather analysis
dic={}
arr=[]
with open("DS_textweather.txt","r") as files:
    for i in files:
        i=i.strip()
        data=i.split(",")
        dic.update({data[0]:data[1]})
        arr.append(int(data[1]))
        
print(dic) 
print(max(arr[:5]))  #maximum temperature between Jan 1 and Jan 15
print(sum(arr[:8])//7)    #The average temperature in first week of Jan
print(dic["Jan 7"])     #The temperature on Jan 7
print(dic["Jan 4"]) 


#Word count in paragraph
st=""
with open("DS_textwordcount.txt","r") as files:
    st=files.read()
lis=st.split()
dic={}.fromkeys(lis,0)
#print(lis)
#print(dic)
for i in lis:
    if i in lis:
        dic[i]+=1
print(dic)        
