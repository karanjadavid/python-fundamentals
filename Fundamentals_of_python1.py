#####################################################################
# FUNDAMENTALS OF PYTHON - Data Field
#####################################################################
# Documentation by David Karanja on 28th January 2022

# Examples of When can you use python.
# 1. To do quick calculations
# 2. Develop a database driven website
# 3. Clean and analyze a survey's database

# Save the scripts as .py 
# Use a single hash tag # to comment code



# PYTHON AS A CALCULATOR. Addition, subtraction, division, modulus
print("Addition")
print(5 + 5)
print("Power")
print(4**2)


# VARIABLES AND TYPES

# A variable is specific, case_sensitive
# we use = as the assignment operator
# helps in reproducibility
# Suppose you have a height of 1.79m and a weight of 68.7kg
height = 1.79
weight = 68.7
print(height)
print(weight)

#calculate Body Mass Index BM1 = weight / height**2
bmi = weight/(height**2)
print(bmi)

# PYTHON DATA TYPES - integers, floats, strings, booleans
# int - whole numbers, float - decimal numbers, str - text, bool - True / False
# to find out the type, simply use the type function
print(type(bmi))
print(type(10))
print(type(True))
print(type("Dave"))


# TYPE CONVERSION 
# when adding text to numbers, you'll need to convert the integers or floats into strings
# functions to help you convert data types: int(), str(), bool(), float()
savings = 100
result = 100 * 1.10 * 7

print("I started with $" + str(savings) + " and now have $" + str(result) + ". Awesome!")









#####################################################################
# PYTHON LISTS
#####################################################################
# lets look at python data types
# 1. float - real numbers
# 2. int - integer numbers
# 3. str - strings/ text
# 4. bool - True / False

# List - a way to give a single name to a collection of values. 
# It is a compound data type, you can group values together.
# Lists are used to store information of differnt data types enclosed within brackets. [a,b,c,d]
fam = [1.73, 1.68, 1.71, 1.89]
print(fam)

# Lists can contain lists within them
fam2 = [["Liz, 1.73"], ["Emma", 1.68], ["mom", 1.71], ["dad", 1.89]]
print(fam2)

# look for the type of list - list
print(type(fam2))


# Creating a list from variables
hall = 11.25
kit = "Nike"
liv = 20.0
bed = True
bath = 9.50

# Create list areas
areas = [hall, kit, liv, bed, bath]

# Print areas
print(areas)







# SUBSETTING LISTS

# You can access information on your list. 
# the first element is of index 0, the second element index 1 ....etc. (Zero indexing)
# to access the last element of the list use -1 index
friends = ["Tom", "Mark", "Eric", "Mason", "Gillian", "Joe", "Raphael", "Oscar"]
print(friends[0])
print(friends[-1])


# LIST SLICING
# my_list[start:end] The start index will be included, while the end index is not.
# specify the range using a colon.
print(friends[2:5])
print(friends[3:])
print(friends[:5])

# Subset and calculate
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]
# Sum of kitchen and bedroom area: eat_sleep_area
eat_sleep_area = (areas[3] + areas[-3])
print(eat_sleep_area)



# Subset list of lists
# first list in the list is 0. We use two square brackets to access elements in the list below
alp = [["a","b","c"], ["d","e","f"],["g", "h","i"]]
# subset the second list
print(alp[1])
# from the third list, access the second element
print(alp[2][1])










# MANIPULATING LISTS
# this are ways to change elements in lists, to add elements and remove elements

# changing list elements
# Simply subset the list and assign new values to the subset. 
girls = ["Ann", 1.78, "Rose", 1.58, "Maureen", 1.70, "Rahab", 1.66, "Lucy", 1.70]
# change Maureen's height to 1.68
girls[5] = 1.68
print(girls)
# chage the first two elements to Joan who has a height of 1.60
girls[:2]= ["Joan", 1.60]
print(girls)

# Add elements to a list.
# use the addition sign, new elements are appended at the back of the list.
girls_extended = girls + ["Mercy", 1.77]
print(girls_extended)

# Delete elements from a list
# use del function to delete an element from a list 
# as soon as you remove an element from a list, the indexes of the elements
# that come after the deleted element all change!
animals = ["dog", "cat", "donkey", "cow", "sheep", "goat"]
del(animals[2])
print(animals)

# Delete poolhouse and its area 24.5 from the area_sizes list
# The ; sign is used to place commands on the same line.
area_sizes = ["hallway", 11.25, "kitchen", 18.0,
        "chill zone", 20.0, "bedroom", 10.75,
         "bathroom", 10.50, "poolhouse", 24.5,
         "garage", 15.45]
         
del(areas[-4:-2])
print('area sizes')
print(area_sizes)

#  WRONG choices below 
# a) del(areas[10]); del(areas[11]) If you first remove areas[10], all elements after index 10 move up a spot. 
# If you then do del(areas[11]), you are deleting the element that was originally at index 12.

# b)  del(areas[10:11]) will only select the element at index 10.

# c) 


# Copy without issues in a list. if you copy h = k, you copy the reference to the list, not the values themselves
# recommended copying methods are shown below

h = ["a","b","c"]
k = list(h)
print(k)

l = h[:]
print(l)







#####################################################################
# FUNCTIONS
#####################################################################

# A function is a piece of reusable code aimed at solving a particular task
# built-in function examples: max(), type(), round() - takes two variables first, a number you want to round and 
# second, the precision with which to round ie, how many digits after the decimal point you want to keep 

# Round to two decimal places
print(round(1.58945, 2))

# Round number to the nearest integer
print(round(25695.7524))


# Inside functions, the [] means that the argument is optional 
# round(number[, ndigits])- in this function, ndigits is opttional

# sorted(iterable, /, *, key=None, reverse=False).
# sorted(iterable, /, *, key=None, reverse=False) takes three arguments: iterable, key and reverse. 
# key=None means that if you don't specify the key argument, it will be None. 
# reverse=False means that if you don't specify the reverse argument, it will be False.

# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]
# Paste together first and second: full
full = first + second
# Sort full in descending order: full_sorted
full_sorted = sorted(full, reverse = True)
# Print out full_sorted
print(full_sorted)





#####################################################################
# METHODS
#####################################################################

# methods are functions that belong to python objects
# methods are called with the dot notataion on the objects.
# a python object of type string has methods such as capitalize(), replace()
# some methods can change the objects they are called on eg, append on lists



# python list / array Methods 

# append(), 
# clear(), 
# copy(), 
# count(), 
# extend(), 
# index(), 
# insert(), 
# pop(), 
# remove(), 
# reverse(), 
# sort()

# append() - adds an element to the list it is called on.
# remove() - removes the first element of a list that matches the input.
# reverse() - reverses the order of the elements in the list it is called on.





# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
# Use append twice to add poolhouse and garage size
areas.append(24.5)
areas.append(15.45)
# Print out areas
print(areas)
# Reverse the orders of the elements in areas
areas.reverse()
# Print out areas
print(areas)





# Create list hood
hood = [11.25, 18.0, 20.0, 10.75, 9.50]
# Print out the index of the element 20.0
print(hood.index(20.0))
# Print out how often 9.50 appears in areas
print(hood.count(9.50))





# python string methods 

# capitalize(), 
# casefold(), 
# center(), 
# countv(), 
# encode(), 
# endswith(), 
# expandtabs(), 
# find(), 
# format(), 
# format_map(), 
# index(), 
# upper(),
# replace() 





# string to experiment with: place
place = "poolhouse"
# Use upper() on place: place_up
place_up = place.upper()
# Print out place and place_up
print(place)
print(place_up)
# Print out the number of o's in place
print(place.count("o"))





#####################################################################
# packages 
#####################################################################

# a package is a directory of python scripts. Each script is a module. 
# These modules specify functions, methods and new python types aimed at solving particular problems.

# examples of Data science packages
# Numpy
# Matplotlib
# Scikit-learn
# Seaborn

# install packages on your system using pip, a package maintenance system for python





# Definition of radius
r = 0.43
# Import the math package
import math
# Calculate C
C = 2 * r * math.pi
# Calculate A
A = math.pi * r ** 2
# Build printout
print("Circumference: " + str(C))
print("Area: " + str(A))



#####################################################################
# Numpy
#####################################################################
# Numeric python is a package that provides an alternative to the regular python list: the numpy array
# numpy array is similar to the python list but has additional features such as ability to perform calculations over entire arrays
# it is easy and super fast
# numpy assumes your array has elements of a single type. They can be floats, booleans, etc
# numpy array comes with its own methods
# numpy arrays perform calculations elementwise 



# How are lists different from Numpy
# Lists - Insertion, deletion, appending, concatenation
# Numpy - Insertion, deleion, appending, concatenation etc + lots more

# Applications of Numpy
# 1. Mathematics (MATLAB REPLACEMENT)
# 2. plotting (Matplotlib)
# 3. Backend (Pandas, Connect4, digital photography)
# 4. Machine learning



# import the numpy package
import numpy as np
print("NUMPY")

# Example of a one dimensional array
print("1D array")
a = np.array([1,2,3])
print(a)

# Example of a two dimensional array
print("2D array")
b = np.array([[9.0,8.0,7.0],
              [6.0,5.0,4.0]])
print(b)

# Example of a three dimensional array
print("3D array")
d = np.array([[[1,2],
               [3,4]],[[5,6],
                       [7,8]]])
print(d)

# our case study numpy array
c = np.array([[1,2,3,4,5,6,7],
              [8,9,10,11,12,13,14]])
print(c)

# Get a specific element from the array  use the notation of [row, column] 
# remember we start indexing at 0
# Get 12
print(c[1,4])

# Get a specific element from the array  use the notation of [row, column] 
# remember we start indexing at 0 from the front.
# Starting from the back of the array, we start with -1
# Get 12
print(c[1,-3])

# Get a specific row.  
# first row. [row, column] 0 on the row notation and : colon on the column part 
print(c[0,:])

# Get a specific column
# Third column
print(c[:,2])

# Get a range. [startindex: endindex: stepssize]
# first row between 2 and 6 with a step of 2
print(c[0,1:6:2])

#####################################################################
# Modifying elements in numpy arrays
#####################################################################

# Replacing one element to another 

c = np.array([[1,2,3,4,5,6,7],
              [8,9,10,11,12,13,14]])
print(c)

#change 13 to 20
print()
print("modify element 13, change it to 20")
c[1,5] = 20
print(c)

#change the third column updating it with values 10 and 8
print()
print("Update an entire column")
c[:,2] = [10,8]
print(c)


# numpy arrays calculation
home_height = [1.45,1.58,1.85,1.63,1.77,1.80,1.62,1.88,1.90,1.90]
np_home_height = np.array(home_height)
print(np_home_height)

home_weight = [56.5,70.68,80.00,67.30,78.62,55.20,62.47,69.50,74.84,80.64]
np_home_weight = np.array(home_weight)
print(np_home_weight)

bmi_home = np_home_weight / np_home_height ** 2
print(bmi_home)





# numpy subsetting
print(bmi_home[bmi_home < 24])


# Create list baseball
baseball = [180, 215, 210, 210, 188, 176, 209, 200]
# Create a numpy array from baseball: np_baseball
np_baseball = np.array(baseball)
# Print out type of np_baseball
print(type(np_baseball))





# calculate baseball players height in meters
# import baseball players height using pandas which is stored in inches
# load package
import pandas as pd
# import csv file
height_in = pd.read_csv("baseball.csv")
print(height_in.head())
#create a numpy array
np_heights_bsb = np.array(height_in)
# Create a numpy array from height_in: np_height_in
np_height_in = np.array(height_in['Height'])
# print out np_height_in
print(np_height_in)
# Convert np_height_in to m: np_height_m
np_height_m = np_height_in * 0.0254
# Print np_height_m
print(np_height_m)






# Calculate baseball players' BMI: bmi
# find the light weight players whose bmi is below 21
np_height_m = np.array(height_in['Height']) * 0.0254
np_weight_kg = np.array(height_in['Weight']) * 0.453592
bmi = np_weight_kg / np_height_m ** 2
# Create the light array
light = np.array(bmi < 21)
# Print out light
print(light)
# Print out BMIs of all baseball players whose BMI is below 21
print(bmi[light])





# numpy subsetting
# Print out the weight at index 50
weight_baseball = np.array(height_in['Weight'])
print(weight_baseball[50])
# Print out sub-array of np_height_in: index 100 up to and including index 110
print(np_height_in[100:111])





######################################
# 2D NUMPY ARRAY
#####################################
# you can create a 2D numpy array from a regular python list of lists. 
# Each sublist in the list corresponds to a row in the two dimensional numpy array
height_weight = np.array([[1.73,1.68,1.71,1.89,1.79], [65.4,59.2,65.6,88.4,68.7]])
print(height_weight)
# the array has two rows and five columns from the shape attribute
print(height_weight.shape)

# subsetting
# select the first row and third column
print(height_weight[0][2])
print(height_weight[0,2])

# select the height and weight of second and third family member
print(height_weight[:,1:3])

# Create baseball, a list of lists
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)
# Print out the type of np_baseball
print(type(np_baseball))
# Print out the shape of np_baseball
print(np_baseball.shape)






######################################
# 2D NUMPY BASIC STATISTICS
#####################################
# numpy statistics: np.mean(), np.meadian, np.corrcoef, np.std

# average mean of baseball players height
print(np.mean(np_heights_bsb[:, 3]))


# average median of baseball players height
print(np.median(np_heights_bsb[:, 3]))