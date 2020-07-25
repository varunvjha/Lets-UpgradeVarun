#!/usr/bin/env python
# coding: utf-8

# In[2]:


n=int(input("Enter a number to check prime "))
c = 0
i = 1
while i<=n:
    if n%i==0:
        c=c+1
    i=i+1
if c==2:
    print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")


# In[3]:


n=int(input("Enter a number to check prime "))
c = 0
i = 1
while i<=n:
    if n%i==0:
        c=c+1
    i=i+1
if c==2:
    print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")


# In[ ]:




