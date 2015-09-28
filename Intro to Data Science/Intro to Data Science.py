
# coding: utf-8

# In[1]:

print "Hello"


# In[2]:

import pandas 


# In[3]:

2+2


# In[4]:

x = 2


# In[5]:

y = 7
x+y


# In[6]:

# setting age to my age
age = 28


# In[7]:

# setting future age to my age plus 10 years
future_age = age + 10
# printing those age variables
print age 
print future_age


# In[8]:

# declaring a list of numbers
numbers = [1, 2, 5, 7, 10]


# In[9]:

# adding things to list
numbers.append("hello")


# In[10]:

# removing hello, index of element to remove can also be specifed
numbers.pop()


# In[11]:

# access the 0th element of this list
numbers[0]


# In[13]:

# performing math operations
sum(numbers)


# In[14]:

min(numbers)


# In[15]:

numbers.append("John")
# sum(numbers), this will now throw an error b/c str and int can't be added


# In[16]:

"John" in numbers


# In[18]:

"John" < "5"


# In[21]:

# creating list of restaurants and performing some exercises
restaurants = ["Laut", "Random String", "Chipotle", "Eataly", "Sophie's Cuban", "Chop't", "Potbelly's"]

# Get the third element of the list
restaurants[2]

# Add "Ootoya" to the end of the list
restaurants.append("Ootoya")

# Use .pop() to remove "Random String" from the list
restaurants.pop(1)

# Print the list
print restaurants

# Check if 'Chipotle' is in the list
print "Chipotle" in restaurants

# Check if 'Random String' is in the list
print "Random String" in restaurants

# Get the length of the list
len(restaurants)


# In[26]:

# defining a person
person = {
    "name": "Gabby",
    "class": "Panda Pythons"
}

# accessing value from key
print person["name"]

# if I try below, it would throw and error since it does exist
# print person["location"]

# adding to list
person["location"] = "General Assembly"

# find keys in dictionary
print "location" in person

# delete a person
del person["location"]

# get all keys
print person.keys()

# get all values
print person.values()

# get all key values
person.items()


# In[27]:

# Create a dictionary called `class_data`
class_data = {
    "course_name": "Intro to Python",
    "student_count": 20,
    "instructor": {"name": "Suneel", "gender": "M", "can_program": True}
}

# get the student count from the dictionary
print class_data["student_count"]

# get the instructor name from the dictionary
class_data["instructor"]["name"]


# In[28]:

x = "John Jameson"
# Construct an if else statement according to this logic: 
# if "John" is in x, print "John is in x", otherwise print "John is not in x"
if "John" in x:
    print "John is in x"
else: 
    print "John is not in x"

# Construct an if/elif/else statement according to this logic: 
# if "roger" is in x, print "Hi Roger!", elif the length of x is greater than 20, 
# print "thats a long string", else print "Oh well!"
if "roger" in x:
    print "Hi Roger!"
elif len(x) > 20:
    print "that's a long string"
else:
    print "Oh well!"


# In[39]:

# Construct a list of numbers between 0 and 1000 that are divisible by 33
three_list = [x for x in range(1001) if x % 33 == 0]
print three_list


# In[34]:

# create function multiply that takes two variables and returns their product
def multiply(a, b):
    return a * b

print multiply(2, 3)


# In[48]:

# take a list of numbers and return a subset of numbers that are either odd or divisible by 8
# call the function on list: [1, 8, 3, 10, 9]
def divisible_checker(nums_list):
    return [x for x in nums_list if x % 2 != 0 or x % 8 == 0]

print divisible_checker([1, 8, 3, 10, 9])

# with a partner: 
# write a function that takes a list of numbers and return True if the sum of the numbers is even 
# and False otherwise.
def evens(num_list):
    print sum(num_list)
    if sum(num_list) % 2 == 0:
        return True
    else: 
        return False

print evens([2, 3, 4, 5, 6, 7])
evens([2, 2, 2, 2, 2, 2])


# In[40]:

import random
dir(random)


# In[42]:

# Find the randint function in the documentation and explain to your neighbor what it does and how to use it.
# random.randint(a, b)
# Returns a random integer N such that a <= N <= b
# this should return a different random number between 2 and 200 10 times
for i in range(10):
    print random.randint(2, 200)


# In[44]:

# with your partner, use the randint function to generate a random number between 1 and 125
random.randint(1, 125)


# In[53]:

#  solo: use the shuffle function on this list: [1, 2, 7, 5, 9, 10]. What gets returned?
shuffle_list = [1, 2, 7, 5, 9, 10]
random.shuffle(shuffle_list)
print shuffle_list


# In[50]:

# *args and **keywords
def cool_sum(*nums):
    # this  function takes an arbitrary list of inputs 
    return sum(nums)

print cool_sum()
print cool_sum(1)
print cool_sum(1, -25, 30, 8, 89)


# In[55]:

# use this to refer to random library as rd rather than random
import random as rd


# In[56]:

rd.randint(1, 125)


# In[60]:

# Class syntax
class Shape(object):
    def __init__(self, name, *args, **kwargs):
        # Save 'name in the instance of this shape
        self.name = name


# In[62]:

rect = Shape("rectangle")
rect.name


# In[66]:

import math
# create Circle that inherits from Shape
class Circle(Shape):
    def __init__(self, name, radius, *args, **kwargs):
        # this is going to execute __init__ of the parent Class
        # get the superclass of Circle and execute the constructor with these arguments
        super(Circle, self).__init__(name, *args, **kwargs)
        
        self.radius = radius
        
    def area(self):
        return math.pi * (2 * self.radius)


# In[69]:

circ = Circle("Bubbles", 3)


# In[70]:

print circ.name
circ.area()


# In[73]:

# new class take width and height
# define init and area
class Rectangle(Shape):
    def __init__(self, name, width, height, *args, **kwargs):
        super(Rectangle, self).__init__(name, *args, **kwargs)
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height


# In[76]:

Rectangle("Obtuse", 5, 5).area()


# In[86]:

# importing pandas under alias
import pandas as pd

# reading csv file from url
df = pd.read_csv('https://s3.amazonaws.com/python-level-2/sales-funnel.csv')


# In[88]:

# tells you data type
# dataframe represents datatype from other files like excel
type(df)


# In[90]:

# returns first columns 
df.columns


# In[94]:

# restrict df to certain columns
df[["Account", "Name", "Rep"]]


# In[93]:

df[:5]


# In[95]:

# with df are series (the two main classes of data in Pandas)
type(df["Account"])


# In[100]:

# sort df for data with status of pending
# like sql query: get me subset of df where df column "Status" is equal to pending 
just_pending = df[df["Status"] == "pending"]
just_pending.count()


# In[109]:

# How many accounts have a price greater than $12,000?
greater_twelve = df[df["Price"] > 12000]
len(greater_twelve)


# In[122]:

# What is the maximum account price?
# faster than using max(df["Price"])

prices = df["Price"]
prices.max()


# In[123]:

# What is the minimum account price?
print prices.min()

# What is the mean account price?
print prices.mean()

# What is the sum of all the prices?
print prices.sum()


# In[131]:

# What is the total dollar amount pending?
df["Amount"] = df["Quantity"] * df["Price"]
just_pending = df[df["Status"] == "pending"]
just_pending["Amount"].sum()


# In[132]:

# pivoting table: diff view of data
pd.pivot_table(df, index=["Name"])


# In[137]:

# some more practice with pandas pivot_table
print pd.pivot_table(df,index=["Manager","Rep"])
pd.pivot_table(df,index=["Manager","Rep"],values=["Price"])


# In[140]:

# create a pivot table that indexes on Manager and Status and displays only the column Price,
# which contains the total price of accounts for each (Manager, Status) pair.
import numpy as np
pd.pivot_table(df, index=["Manager","Status"], values=["Price"], aggfunc=np.sum)


# In[147]:

# create a pivot table indexing on Status and displays only the column Price summed up per status
pd.pivot_table(df, index=["Status"], values=["Price"], aggfunc=np.sum, columns=["Account"], fill_value=0)


# In[157]:

# importing digits data from skikit learn
from sklearn import datasets
digits_data = datasets.load_digits()


# In[158]:

real_data = digits_data["data"]
real_data


# In[159]:

new_df = pandas.DataFrame(real_data)


# In[160]:

digits_data["target"]


# In[154]:

digits_data["DESCR"]


# In[ ]:

import matplotlib.pyplot as plt
from sklearn import svm

# let's instantiate our Support Vector Classifier
classifier = svm.SVC(gamma=.0001, C=100)

# how many data points do we have?
print len(digits_data.data)

# let's createa  training set of the first 1597 of the 1797 data points
x_training, y_training = digits_data.data[:-200], digits_data.target[:-200]

# now let's train the classifier on the training data
classifier.fit(x_training, y_training)

print "Prediction {}".format(classifier.predict(digits_data.data[1600]))
print digits_data.target[1600]

# show the image
plt.imshow(
    digits_data.images[1600],
    cmap=plt.cm.gray_r,
    interpolation="nearest"
)
plt.show()

# Wow!!!! Let's see what the accuracy is
# Let's go from digits.data[-200] all the way to digits.data[-1]
correct = 0
indices = range(-200, 0)
for i in indices:
    # if we were correct
    if classifier.predict(digits_data.data[i])[0] == digits_data.target[i]:
        correct += 1
accuracy = float(correct) / len(indices)

print "SVC Accuracy: {}".format(accuracy)


# # Sample Project
# 
# - scrape Reddit or similiar (beautiful soup)
# - load that data into a django app (postgres)
# - frontend takes a url
# 
# ## Resources
# - [SkiKit](http://scikit-learn.org/stable/)
# - [Panda's Documentation](http://pandas.pydata.org/)
# - [Coursera](https://www.coursera.org/)
# - [Beautiful Soup Docs](http://www.crummy.com/software/BeautifulSoup/bs4/doc/)
# 

# In[ ]:



