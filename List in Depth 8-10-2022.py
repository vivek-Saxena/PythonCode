#!/usr/bin/env python
# coding: utf-8

# In[1]:


#What is list?
#list is a collection of hetrogenious (different data types) data elements enclosed in squre braces seprated with commas
#list is mutable(changable) sequence 


# In[2]:


#how to creat a list in python
#We can an empty list also
l = []
print(type(l))


# In[3]:


l1 = [10,10.23,True,'Hello',10,100,[100,200,300]]


# In[4]:


#By the use of range function we can create a list . Range basically provide a sequence in the manner of start stop-1 and step
# range(1,11)
#there is list function also 
lr = list(range(1,11))
print(lr)


# In[5]:


lr = list(range(1,11,2))
print(lr)


# In[6]:


#How to fetch element from the list?
#By the use indexing and slcing 
l1


# In[7]:


l1[0]


# In[8]:


l1[1]


# In[9]:


l1[3]


# In[10]:


l1[4]


# In[11]:


l1[5]


# In[12]:


l1[6]


# In[13]:


l1[7]


# In[ ]:


l1


# In[14]:


#There is negtive indexing \
l1[-1]


# In[15]:


l1[-2]


# In[16]:


l1[-3]


# In[17]:


l1[-4]


# In[18]:


l1[-5]


# In[19]:


l1[-6]


# In[20]:


l1[-7]


# In[21]:


l1[0] = l1[0]+12


# In[22]:


l1


# In[23]:


#How to fetch the elemtn of nested list


# In[24]:


l1[6]


# In[25]:


#Multi level indexing


# In[26]:


l1[6]


# In[27]:


l1[6][0]


# In[28]:


l1[6][1]


# In[29]:


l1[6][2]


# In[30]:


newl = [22, 10.23, True, 'Hello', 10, 100, [100, 200, 300,['Hello','World'],['India']]]


# In[31]:


newl[6][3][0]


# In[32]:


newl[6][3][1]


# In[33]:


newl[6][4][0]


# In[34]:


newl[-1]


# In[35]:


newl[-1][0]


# In[36]:


newl[-1][-1]


# In[37]:


newl[6][-1]


# In[38]:


#slicing


# In[39]:


#we can understand slicing by the triple S formula [start:stop-1: step]


# In[40]:


l1[0:4]


# In[41]:


lr = list(range(50,101,2))
print(lr)


# In[42]:


print(lr[1:6:2])


# In[43]:


print(lr[1:5])


# In[44]:


print(newl)


# In[45]:


newl[1:5]


# In[46]:


newl[-4]


# In[47]:


newl[-1]


# In[48]:


newl[-4:-1]


# In[49]:


print(newl)


# In[50]:


newl[-1:-4:-1]


# In[51]:


#How to reverse a list by the use of slicing
print(newl[::-1])


# In[52]:


print(l)


# In[53]:


#How to insert an element in the list 
#By the use of assignment operator 

newl[0]


# In[54]:


newl[0]='Sachin'


# In[55]:


print(newl)


# In[56]:


#But we can see that it will overwrite the element


# In[57]:


print(dir(list))


# In[58]:


print(help(list.append))


# In[59]:


get_ipython().run_line_magic('pinfo', 'newl.append')


# In[60]:


newl.append('Sachin')


# In[61]:


print(newl)


# In[62]:


#extend
get_ipython().run_line_magic('pinfo', 'newl.extend')


# In[63]:


l4 = ['Canda','USA','Australlia']
newl.extend(l4)


# In[64]:


print(newl)


# In[65]:


newl.extend('Hello')


# In[66]:


print(newl)


# In[ ]:





# In[67]:


# What is difference between append and extend?


# In[68]:


newl.append(l4)


# In[69]:


print(newl)


# In[70]:


print(newl)


# In[71]:


newl.append('Hello')


# In[72]:


print(newl)


# In[73]:


#Insert
get_ipython().run_line_magic('pinfo', 'newl.insert')


# In[74]:


newl.insert(0,'Unviverse')


# In[75]:


print(newl)


# In[76]:


newl.insert(-2,'IT')


# In[77]:


print(newl)


# In[78]:


newl.insert(-1,'IT')


# In[79]:


print(newl)


# In[80]:


newl.insert(-0,'Orange')


# In[81]:


print(newl)


# In[82]:


newl.index('Unviverse')


# In[83]:


newl.index('Hello')


# In[84]:


newl.index('Hello',6)


# In[85]:


get_ipython().run_line_magic('pinfo', 'newl.index')


# In[86]:


#remove Function


# In[87]:


print(newl)


# In[88]:


len(newl)


# In[89]:


newl.insert(22,'Algebra')


# In[90]:


print(newl)


# In[91]:


len(newl)


# In[92]:


newl[-1]


# In[93]:


newl[22]


# In[94]:


# How to sorti of an list in ascending and descending order


# In[95]:


print(newl)


# In[96]:


get_ipython().run_line_magic('pinfo', 'newl.sort')


# In[97]:


newl.sort()


# In[98]:


'a'<0


# In[99]:


#Make numbers list


# In[100]:


nl = [10,11,99,100,3,5,23.34,9,26,34,67,23.45,0,True,False]


# In[101]:


nl.sort()


# In[102]:


nl


# In[103]:


get_ipython().run_line_magic('pinfo', 'nl.sort')


# In[104]:


nl.sort(reverse=True)


# In[105]:


nl


# In[106]:


#list of string
ls = ['Orange','Blue','Black','Red','Pink','Zblack','Green','Yellow']


# In[107]:


ls.sort()


# In[108]:


ls


# In[109]:


ls.sort(reverse=True)


# In[110]:


ls


# In[111]:


print(dir(list))


# In[112]:


print(newl)


# In[113]:


newl.reverse()


# In[114]:


print(newl)


# In[115]:


#By the use of slicing reverse
print(newl[::-1])


# In[116]:


print(newl)


# In[117]:


newl = newl[::-1]


# In[118]:


print(newl)


# In[119]:


print(newl)


# In[ ]:





# In[120]:


print(newl[::-1])


# In[ ]:


#Tuple is also a list but it is immutable
#we can create a tuple by () .Value enclosed in () braces seprated with commas
#we can also use tuple function for typecasting


# In[121]:


l = [10,11,12,13]
l = tuple(l)
print(l)


# In[122]:


t = 12,11,12


# In[123]:


print(type(t))


# In[124]:


t1 = (10,11,12,13,25,69,34,564)


# In[125]:


print(type(t1))


# In[126]:


print(help(tuple))


# In[127]:


#you can make a list inside a tuple
t = (10,12,14,35,85,[100,1200,545])


# In[128]:


#indexing slicing is same like list
t[0]


# In[129]:


t[1]


# In[130]:


t[2]


# In[131]:


t[3]


# In[132]:


t[4]


# In[134]:


t[5]


# In[135]:


#you can assign a value because it's a tuple

t[0]='Hello'


# In[136]:


#But t[5] is a list so you can perform list operation here 
print(type(t[5]))


# In[138]:


#so we can do list operation here
t[5].append(2000)


# In[139]:


print(t)


# In[140]:


t = list(t)
t.append('hello')
t = tuple(t)
print(t)


# In[141]:


print(dir(tuple))


# In[142]:


t.index('hello')


# In[143]:


t.index([100, 1200, 545, 2000])


# In[144]:


t.index(10)


# In[146]:


t.count('hello')


# In[147]:


get_ipython().run_line_magic('pinfo', 't.count')


# In[148]:


#dictionary is a sequence of key:value pair eclosed in curly braces seprated with commas. 
#dictionary is unordered sequence so there is no indexing and slicing
#dictionary is mutable sequence


# In[149]:


#How to create a dictionary


# In[150]:


#1st method
#if key is string make it string
d = {'One':1,'Two':2}


# In[151]:


print(type(d))


# In[152]:


d1 = {1:'One',2:'Two'}


# In[153]:


d2 = {'UserName':'ABCD','Password':12345}


# In[154]:


print(d2)


# In[155]:


print(type(d2))


# In[156]:


#If you want to isert multiple values
d3 = {'EmpName':'ABC','BBC','EmpId':101,102}


# In[163]:


#if you want to insert multiple values use tuple or list 
d3 = {'EmpName':['ABC','BBC'],'EmpId':[101,102]}


# In[164]:


print(d3)


# In[159]:


#Because Dictionary is unordered sequence so there is no indexing and slicing


# In[160]:


d3[0]


# In[165]:


#how to fetch element from a dictionary


# In[167]:


#by suscript pass the key which you want to fetch
d3['EmpName']


# In[168]:


d3['EmpId']


# In[169]:


#we can fetch by the use of get function . It will key as a argument and return corresponding values


# In[170]:


d3.get('EmpName')


# In[171]:


d3.get('EmpId')


# In[172]:


#Difference between subscript and get function


# In[173]:


#if key is not in the dictionary than subscrip will thrown an erro but get method not.


# In[174]:


d3['EmpMob']


# In[175]:


d3.get('EmpMob')


# In[ ]:




