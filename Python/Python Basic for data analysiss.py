#!/usr/bin/env python
# coding: utf-8

# # Lets explore more functions of Python 

# Always remember Python is very vast langauage so learn that much only which is bussiness required in day to day life of data analyst.

# Understanding Tuples in Python 
# An Immutable Data Structure

# Before Stating just understand the diff between this barckets 
# 1.() = Tuple
# 
# 2.[] = List
# 
# 3.{} = dict

# 1. Tuple()

# In[1]:


t = (3,4,5,6)


# In[2]:


type(t)


# lets find is there duplicate data is allowed in Tuples or not

# In[4]:


t = (3,4,6,8,9,9,6)


# In[5]:


t


# As we see that Tuples allowed the duplicate data to store

# In[6]:


t1 = (2,3,5,6) 
t2 = (1,5,6,7)


# In[8]:


t1 + t2              # as we see that tin tuples concatenation is allowed means adding 2 different values in one output


# Lest Explorethe functions of tuples as same we seen in List

# In[11]:


test = (2,5,7,8,9,10,15,21,21)


# 1.Count Function
# 
# this function will count the elements no.of time present in data

# In[13]:


test.count(21) 


# 2.Index Function 
# 
# this function act same like reading index value as n-1

# In[15]:


test.index(21) 


# here you will get confuessed that why its showing only singel index 7 from 21, why not showing 8 comparatively because in Indexing it only take 1st occurancee of each

# 3. Append Function
# 
# this funtion will add values but at end-point of data 

# In[16]:


test.append(2,3,4)


# 4. Extend Function
# 
# The extend() function in Python is used with lists to add elements from an iterable (like another list, tuple, or set) to the end of the current list

# In[17]:


test.extend(3,5,6)


# Oops append and extend function didnt support in tuples.
# tuples is like a data structure where you choose that datatype and it remains unchange because tuples are immutable as like string
# 
# In tuples there are only two functions support 
# 1. Count
# 2. Index

# We always use tuple when there will be no changes in data and fix with given parameter.

# Now lets use tuple with basic paractice

# In[24]:


for i in range(len(t1)):
    print(t1[i])


# lets understand the code here,
# 
#     we are taking len(t1) which is 4
#     where (i) is reading the index values as (0,1,2,3)
#     where conditions meet as (t1[0] = 2, t1[1] = 3, t1[2] = 5, t1[3] = 6 ) 
#     its not value assing it just index place where data is store/located

# In[26]:


for i in t1:
    print(i)


# lets understand the code here,
# 
#     here we are taking (i) as random number
#     where (i) is cheking that in t1 there are number (2,3,5,6) is present if yes give output 

# 2. Set in Python 

# to Understand the set we need first understand dict{}

# In[28]:


a1 = {}


# In[30]:


type(a1)


# 1. When we use {} this is dict
# 2. empty curly bracket{} is called dictonery

# But one we add the data/values in this it get converted to Set.

# In[31]:


set_demo = {2,3,"asmit",23.60}


# In[32]:


type(set_demo)


# In[44]:


set_dup = {2,2,"asmit",21} # here in output duplicate removes automatically


# In[45]:


set_dup


# as you see that set didnt allowed duplicate values
# 
# this helps when ur work on business case and there is no reqiurement of duplicates & when you need to do frequent changes you will use list and when you didnt want to use opertaions like append or adding values use tuple 
# just simple way to understand

# In[47]:


set_dup[2]


# In[48]:


len(set_dup)


# In[50]:


for i in set_dup: # here in output also we can see that duplicates are removes
    print(i)


# In[51]:


set_a = {4,5,2,6,1,0,"##","aa",23.10,10.9,"asmit","cat","kite"}


# In[53]:


set_a


# as you see this set never returns the dataset sorted, yes order will be there but not sorted 

# In[54]:


for i in set_a:
    print(i)


# In[55]:


S = {1,2,3,11,22,33}


# In[56]:


S


# you can see the beauty of set it has two types of data reading homogenous and heterogenous way the output we see for S is homogenous
# 
# lets convert this data to heterogenous to understand the partten of them. 

# In[77]:


S = {1,2,3,11,22,33,10.1,22.9,"asmit","c",19}


# In[78]:


S


# as you see that the set is giving output but in the way series for each elements 
# 
# example: 
#     
#     1,10.11,11,19 and shift towards 2,22,22.9 and so on.
# Set are design to be like this because of this sets are unpredictable.

# lets play with sets with functions

# 1. Pop function 
# 
# this functions keeps removing the value from dataset but its order was not sorted and one the dataset get empty it get null

# In[80]:


S.pop()


# In[81]:


S 


# you can see that the pop function makes our dataset for S empty in simple word for pop in refer delete

# In[ ]:


S.pop(3) # to remove specific value give its index and it not its default will be last


# 3. Dictionaries {}
# 
# Creation of Dictionaries

# It can be created with curly braces.

# In[1]:


empty_dict = {}


# In[6]:


type(empty_dict)


# dict() function can also be used to create dictionary. List of tuples which actually contains the key value pairs needs to be provided as the input.
# 
# 

# In[7]:


d = dict([('A',1), ('B',2), ('C',3)])


# In[8]:


d


# as you see we create dictionary but it assign some key patterns to each value

# lets assign some key and explore basic functions

# In[9]:


my_dict = {'Jan': 31, 'Feb':28, 'March': 31, 'Apr':30} # keys are strings
my_dict


# Key can be string, numbers or tuples, basically it has to be immutable object.

# In[11]:


dict2 = {1:'Jan', 2:'Feb', 3:'March', 4:'April'}  # keys are numbers
dict2


# In[12]:


dict3 = {(1, 2019) : 'Jan', (2, 2019):'Feb'}  #keys are tuples
dict3


# In[13]:


dict4 = {[1, 2019] : 'Jan', [2, 2019]:'Feb'}  #keys cannot be list
dict4


# Accessing keys and values

# In[14]:


my_dict.keys()  # get all the keys of dictionary object


# All values can be accessed via values() method.

# In[15]:


my_dict.items()


# All key-value pairs can be accessed by items() method.

# In[16]:


my_dict['Jan']  # access number of days associated with 'Jan'


# Individual value can be found out by using the key associated with it.

# One can iterate over the entries in Dictionaries.

# In[17]:


#Dictionary with Roman numerals
letter_dict = { 'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, "M":1000}
letter_dict


# In[18]:


for key in letter_dict.keys():   # iterate over keys
    print("   " , key)


# In[20]:


for value in letter_dict.values(): # iterate over values
    print("   " , value)


# 4. Conditional Statements 
# 
# Conditional statements allow decision-making in Python programs.
# 

# 1. If-Else Condition
# 

# In[21]:


age = 18
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")


# The if statement checks if age is 18 or more. If true, it prints "Eligible to vote"; otherwise, the else block executes.

# 2.If-Elif-Else Condition
# 

# In[22]:


marks = 85
if marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
else:
    print("Grade: C")


# The elif keyword allows multiple conditions to be checked in sequence.

# 5.Loops in Python
# 
# Loops help in executing a block of code multiple times.
# 
# 

# 1.Loop

# In[26]:


for i in range(1, 6):
    print(i)  # Prints numbers 1 to 5


# The for loop iterates through a sequence (range 1 to 5), printing each number.

# 2. While Loop

# In[27]:


x = 1
while x <= 5:
    print(x)
    x += 1  # Increments x


# The while loop runs as long as x is less than or equal to 5, incrementing x in each iteration.

# 3. Looping Through a List

# In[29]:


fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)


# Iterates through each item in the fruits list and prints it.

# 6.Functions in Python
# 
# Functions allow code reuse and modular programming.

# 1. Defining and Calling Functions

# In[30]:


def greet(name):
    return f"Hello, {name}!"

print(greet("Asmit"))


# def greet(name): defines a function that takes name as an argument.
# 
# The function returns a formatted greeting string.
# 
# print(greet("Asmit")) calls the function and displays the greeting message.
# 

# 2. Function with Multiple Parameters
# 

# In[31]:


def add_numbers(a, b):
    return a + b

print(add_numbers(5, 10))


# This function takes two numbers as input and returns their sum.

# 3. Function with Default Parameters

# In[34]:


def greet(name="Guest"):
    return f"Heyy!!, {name}!"

print(greet())
print(greet("Asmit"))


# In[ ]:


If no argument is passed, the function uses the default value "Guest".


# In[ ]:


These Python basics are the foundation of any data analyst's journey.
Let me know in the comments if you want an advanced series on Python for data analysis! 🚀🔥


# In[ ]:




