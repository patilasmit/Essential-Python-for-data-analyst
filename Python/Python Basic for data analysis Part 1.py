#!/usr/bin/env python
# coding: utf-8

# Q. what is Python?
# 
# Python is a high-level, interpreted programming language known for its simplicity, readability, and versatility. It is widely used in data analysis, web development, automation, artificial intelligence, machine learning, and more.
# 
# 🔹 Key Features of Python:
# ✅ Easy to Learn – Uses simple and human-readable syntax.
# ✅ Interpreted Language – Runs code line by line, making debugging easier.
# ✅ Dynamically Typed – No need to declare variable types explicitly.
# ✅ Cross-Platform – Works on Windows, Mac, and Linux.
# ✅ Huge Community Support – Extensive libraries like NumPy, Pandas, TensorFlow, and Django.
# 
# 🔹 Example of Python Code:
#     
# print "Hello, World!"
# print("Hello, World!")
# 
# Python is beginner-friendly and powerful, making it one of the most popular programming languages today! 🚀

# # Starting with Python
# Basic Syntax and Data Types

# 1.Printing Output

# In[6]:


print("Hello, World!")


# Python provides the print() function to output data.

# 2.Variable Types

# In[12]:


a = 5
print(type(a))


# This will output the type of the variable a, which is an integer (int).

# 3.Type Checking

# In[19]:


print(type("Hello"))


# You can check the type of a variable using the type() function

# 4.Range Function

# The range() function generates a sequence of numbers.

# In[24]:


print(list(range(10)))


# The index in range function always read as n-1.

# In[26]:


print(list(range(3, 10, 2)))


# range(3, 10, 2): This creates a range starting at 3, ending before 10, with a step of 2. 
# Start at 3 (inclusive).
# Stop before 10 (exclusive).
# Increment by 2 each time.

# 5.List Operations

# Lists are ordered collections of items. You can create a list with any data types, and perform various operations on them

# In[27]:


my_list = [1, 2, 3, 4]
print(len(my_list))  
print(my_list[0])


# here we can se that len is 4 and 1st index which is 0 having the value 1.

# 6.String Manipulation

# Strings are immutable, meaning you can't change their characters directly. However, you can convert them into a list and modify them

# create the list name asmit

# In[43]:


a = "asmit"


# this is immutalbe not change to make changes convert  the string to list

# In[44]:


a[2] ='J'


# convert  the string to list

# In[45]:


str_to_list = list(a)


# Now we can make changes

# In[48]:


str_to_list[4] = 'j'


# In[ ]:


str_list


# 7.Input from User

# You can take input from the user using the input() function

# In[ ]:


name = input("Enter your name: ")
print("Hello, " + name)


# # Operations with Python

# 1.Mathematical Operations

# Create calculator  for various mathematical operations like addition, subtraction, multiplication, and division
# 

# The first given task in python for basic and best understanding

# In[50]:


num1 = float(input("enter 1st number")) #here we need to give data type or by default it will consider as string
num2 = float(input("enter 2nd number"))

sum = num1 + num2  # Addition
diff = num1 - num2 # Subtraction
mult = num1 * num2 # Multiplication
div = num1 / num2 # Division
mod = num1 % num2  # Modulo, Output: 1 (remainder of 5 divided by 2)
pwr = num1 ** num2 # Power, Output: 25 (5^2)
print(sum)
print(diff)
print(mult)
print(div)
print(mod)
print(pwr)


# # Working with Lists

# 1. List Manipulation

# Lists are mutable, so you can change their elements

# In[52]:


my_list = [1, 2, 3, 4]
my_list[1] = 10  # Modifies the second element
print(my_list) 


# 2. Appending and Inserting Elements

# You can append new elements to a list using the append() method or insert them at a specific position using insert()

# In[53]:


list_a = ["monkey",25.0,'m',"cat",23,"dog"]


# In[55]:


list_a


# here we are adding Ramya in our existing list

# In[57]:


list_a.append("ramya")


# In[59]:


list_a


# now we want to add elephant in this list with index number.

# In[60]:


list_a.insert(3,"meenu") # just remember that we are adding new parameter not replacing 3rd index


# In[62]:


list_a


# 3. Nested Lists

# You can create lists within lists (nested lists)

# In[63]:


list_b = ["ashu",25.0,'m',"cat",23,"mauu",['gautam','anand','anil']]


# In[64]:


list_b


# If we only need one specific name anil from list 

# In[68]:


list_b[-1][-1] #always read list from reverse order for best practice and it use less compute power


# 4.Making list in reverse order

# In[69]:


a = list("fortuner")


# In[73]:


a


# In[74]:


b = a[::-1] # by using colan: it covert all data in reverse order but note ur original list didnt get convert dont messup with original data


# In[75]:


b


# In[77]:


c = "hellow how are you asmit"
d = c[::-1]
d


# # Practical Exercise: based on our practice

# Given the following list

# num_list = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

# Write a Python program that separates the even numbers into one list and the odd numbers into another list.

# In[80]:


num_list = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]


# In[95]:


even_num = []
odd_num = []


# In[96]:


for i in num_list:
    if (i % 2 == 0):
        even_num.append(i)
    else:
         odd_num.append(i)
print("even_num:",even_num)
print("odd_num:",odd_num)


# In[92]:


e = []
f = []


# In[93]:


for i in range(len(num_list)):
    if (num_list[i] % 2 == 0):
        e.append(num_list[i])
    else:
        f.append(num_list[i])


# In[94]:


e,f


# Find the Squaree numbers of following
# numbers = [1,2,3,4,5,6,7,8,9,10]

# In[98]:


numbers = [1, 2, 3, 4, 5,6,7,8,9,10]
squared_numbers = [num ** 2 for num in numbers]
print(squared_numbers)


# # basic python functions

# 1.Find function 
# 
# find the word(w) from given list

# In[99]:


obj = "akhjfrfuowsndjwnefie0ekvfvjew00qodfje"


# In[100]:


obj.find('w')


# Here we can see that the word(w) was present at 9th index of list.
# 
# why it just showing only one output this might be aslo a question, because find function only occur 1st object or index of 1st occurrence from given parameters

# In[101]:


obj.find('99')


# Just see the beauty of this function if the object is not exist in list it will give output -1

# 2.Split function 
# 
# Split function splits the words from data

# In[102]:


obj.split('w') 


# In split function the parameter we splits is not part of data

# 3.Partition function
# 
# To overcome with problem of split function we have partition function which remains in output but seperate from others

# In[104]:


obj.partition('j')


# 4.Append function
# 
# This add the data in existing list but at the endpoint/end palce of data means last

# In[106]:


s = [1,2,3,4,5]


# In[107]:


s.append([3,4,5,8]) # appending the list inside the list


# In[108]:


s


# 5. Extend function
# 
# extend() is a built-in Python method that adds all elements from an iterable (such as a list, tuple, or set) to the end of an existing list.
# Unlike append(), which adds the entire iterable as a single element, extend() unpacks the iterable and adds its elements individually.

# In[109]:


g = [1,2,3,4,5]


# In[110]:


g.extend([6,8,9,'ramya'])


# In[111]:


g


# 6. Input funtion
# 
# this is just to input the data in any list 

# In[4]:


var = input ('please input your name')


# In[5]:


print("my name is " , var)


# In this post, we covered the basics of list extension in Python, explaining how extend() works and how it differs from append(). However, this is just the beginning! 🚀
# 
# There are many more fundamental concepts about lists, such as slicing, list comprehensions, built-in functions, and advanced manipulations, which we will cover in the next post. Stay tuned for Part 2, where we dive deeper into more essential list operations!
