#!/usr/bin/env python
# coding: utf-8

# In[43]:


#Python HW1

import math


# In[44]:


#1(a)
mylist=list(range(1,21))
print(mylist)

#(b)
mylist2=list(range(20,0,-1))
print(mylist2)

#(c)
ls=list(range(19,0,-1))
mylist3=mylist+ls
print(mylist3)

#(d)
mylist4=[4,6,3]*10
print(mylist4)

#(e)
ls1=[4]
mylist5=mylist4+ls1
print(mylist5)


# In[46]:


#2
x = 3
while x <= 6:
    y=math.exp(x)*math.cos(x)
    x=x+0.1
    print(y)


# In[47]:


#3
x = 1
while x<= 25:
    y=(2**x)/x
    x= x+1
    print(y)


# In[54]:


#4
#(a)
ls4=[]
for i in range(20):
    j = mylist[i]-mylist[19-i]
    ls4.append(j)
print(ls4)

#(b)
ls4b=[]

for i in range(20):
    if mylist[i]//2 == 0:
        j = True
        ls4b.append(j)
        
    else:
        j=False
        ls4b.append(j)

print (ls4b)


# In[69]:


#5
#(a)

file= open("lorem.txt","r")
data = file.read()
stri = data.split()

a=0
b=0
c=0

for x in stri:
    if len(x)>=8:
        a = a+1
    elif len(x)>=4:
        b = b+1
    elif len(x)>=1:
        c = c+1
print( "The amount of words which length are greater or equal to 8 is:", a)
print( "The amount of words which length are between 4 and 7 is:", b)
print( "The amount of words which length are between 1 and 4 is:", c)

   
# question 5(b)

f = open("lorem.txt","r")
data = f.read()
stri = data.split()

#print(len(stri)) is 1000

up =0
lo =0
# for i from 0 to 999
for i in range(len(stri)):
    word_i = stri[i]
    for j in word_i:
        if j.isupper():
            up += 1
        if j.islower():
            lo += 1

print("the amount of the uppercase letters is:", up)
print("the amount of the lowercase letters is:", lo)


# In[ ]:




