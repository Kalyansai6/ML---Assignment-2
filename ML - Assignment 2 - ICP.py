#!/usr/bin/env python
# coding: utf-8

# In[21]:


#Question 1

rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")
    rows = 4
for i in range(rows + 1, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print(" ")


# In[22]:


#Question 2

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("The list is :", my_list)
print("The elements in odd positions are : ")
for i in range(1, len(my_list), 2):
    print(my_list[i])


# In[23]:


#Question 3

x = [23, 'Python', 23.98]
print(x)
print([type(i) for i in x])


# In[25]:


#Question 4

def unique_list(l):
    x = []
    for a in l:
        if a not in x:
            x.append(a)
    return x
sample_list=[1,2,3,3,3,3,4,5]
print("Sample List :", sample_list)
print("Unique List :",unique_list(sample_list))


# In[27]:


#Question 5

def string_test(a):
    b={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in a:
        if c.isupper():
            b["UPPER_CASE"]+=1
        elif c.islower():
            b["LOWER_CASE"]+=1
        else:
            pass
    print ("No. of Upper-case characters : ", b["UPPER_CASE"])
    print ("No. of Lower-case Characters : ", b["LOWER_CASE"])
string_test('The quick Brow Fox')


# In[ ]:




