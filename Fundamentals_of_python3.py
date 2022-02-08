#####################################################################
# FUNDAMENTALS OF PYTHON 3 - Data Field
#####################################################################

# 1) LOGIC CONTROL FLOW AND FILTERING
# 2) LOOPS

# import libraries
import numpy as np
import pandas as pd

#####################################################################
# LOGIC CONTROL FLOW AND FILTERING
#####################################################################

#####################################
# comparison operators
#####################################

# comparison operators - operators that can tell how two python values relate and result into a boolean
# comparators ( <,  <=,  >,  >=, ==, != )

# numeric comparisons 
print(2<3)
print(2 == 3)
print(2 <= 3)

# Comparison of booleans
print(True == False)

# Comparison of integers
print(-5 * 15 != 75)

# Comparison of strings
print("pyscript" == "PyScript")

# Compare a boolean with a numeric
print(True == 1)

# other comparisons . Always make comparisons between objects of the same type
print("carl" < "chris")





# compare arrays
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])
# my_house greater than or equal to 18
print(my_house >= 18)
# my_house less than your_house
print(my_house < your_house)





#####################################
# boolean operators
#####################################
# and
#  or
#  not

#################
# and operator / logical_and()
#################
# takes two booleans and returns True only if both booleans themselves are True

# False and False = False
# False and True = False
# True and False = False
# True and True = True

x = 12
print(x > 5 and x < 15)


#################
# or / logical_or()
#################
# only one of the booleans it uses should be True for it to return True
# False and False = False
# False and True = True
# True and False = True
# True and True = True

y = 5 
print(y < 7 or y > 13)


#################
# not / logical_not()
#################
# it negates the value you use on it. 
# not True = False 
# not False = True 


# Numpy arrays operate abit different
height = [1.45,1.58,1.85,1.63,1.77,1.80,1.62,1.88,1.90,1.90]
weight = [56.5,70.68,80.00,67.30,78.62,55.20,62.47,69.50,74.84,80.64]
np_height = np.array(height)
np_weight = np.array(weight)
bmi = np_weight / np_height ** 2
print(bmi)
# show the bmi greater than 21
print(bmi[bmi > 21])
# show bmi greater than 21 and less than 25
print(bmi[np.logical_and(bmi > 21, bmi < 25)])





# Create arrays
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])
# my_house greater than 18.5 or smaller than 10
print(np.logical_or(my_house > 18.5, my_house < 10))
# Both my_house and your_house smaller than 11
print(np.logical_and(my_house < 11, your_house < 11))





#####################################
# if elif, else
#####################################
# these are conditional statements
z = 4
if z % 2 ==0:
    print('checking ' + str(z))
    print('z is even')


y = 5
if y % 2 ==0:
    print('z is even')
else:
    print('y is odd')


w = 3
if w % 2 == 0:
    print('w is divisible by 2')
elif w % 3 ==0:
    print('w is divisible by 3')
else:
    print('w is neither divisible by 2 nor 3')



# Define variables
room = "bed"
area = 14.0

# if-elif-else construct for room
if room == "kit" :
    print("looking around in the kitchen.")
elif room == "bed":
    print("looking around in the bedroom.")
else :
    print("looking around elsewhere.")

# if-elif-else construct for area
if area > 15 :
    print("big place!")
elif area > 10:
    print("medium size, nice!")
else :
    print("pretty small.")






#####################################
# filtering pandas dataframes
#####################################
# import brics data
brics = pd.read_csv('brics.csv', index_col=0)
print(brics)


# keep countries whose area is greater than 8 million square kilometers
# steps to follow
# 1) select the area column. Pandas series
# 2) perform the comparison on the area column and store the result
# 3) use this result to do the appropriate selection on the dataframe



#####################################
# filter brics area > 8sq km
#####################################
# 1) select the area column. Pandas series
print(brics['area'])
# 2) perform the comparison on the area column and store the result
is_huge = (brics['area'] > 8)
print(is_huge)
# 3) use this result to do the appropriate selection on the dataframe
print(brics[is_huge])

# one line of code
print(brics[brics['area'] > 8])





#####################################
# filter brics area between 8 and 10sq km
#####################################
# keep observations that have an area between 8 and 10 million square kilometers
np.logical_and(brics['area'] > 8 , brics['area'] < 10)
print(brics[np.logical_and(brics['area'] > 8 , brics['area'] < 10)])





#####################################
# filter cars that drive right
#####################################
# cars dataset
# the dataframe contains cars per 1000 people, countries and whether drivers drive right or not. 
# Filter drivers who drive_right == True

# import the  cars data
cars = pd.read_csv('cars.csv', index_col=0)
print(cars)
# Extract drives_right column as Series: dr
dr = cars['drives_right']
# Use dr to subset cars: sel
sel = cars[dr]
# Print sel
print(sel)

# one line of code
sel1 = cars[cars['drives_right'] == True]
print(sel1)
sel2 = cars[cars['drives_right']]
print(sel2)





#####################################
# filter cars where cars per cap > 500
#####################################
# filter cars per cap that is greater than 500
print(cars[cars['cars_per_cap'] > 500])

# Create car_maniac: observations that have a cars_per_cap over 500
cpc = cars['cars_per_cap']
many_cars = cpc > 500
car_maniac = cars[many_cars]
# Print car_maniac
print(car_maniac)


#####################################
# filter cars where car per cap is between 100 and 500
#####################################
ans = cars[np.logical_and(cars['cars_per_cap'] > 100 , cars['cars_per_cap'] < 500)]
print(ans)

# Create medium: observations with cars_per_cap between 100 and 500
cpc = cars['cars_per_cap']
between = np.logical_and(cpc > 100, cpc < 500)
medium = cars[between]
# Print medium
print(medium)
print()









#####################################################################
# LOOPS
#####################################################################
# 1) While loop
# 2) For loop





#####################################
# while loop
#####################################
# it executes the code if the condition is true. However, the while loop continues executing the code over and over againn 
# as long as the condition is true

# the syntax is        while condition:
#                              expression

# a while loop is used when you want to repeat action until a condition is met


# write a while loop that divides a number by 4. condition is that the number is greater than 1
error = 50.0
while error > 1 :
    error = error / 4
    print(error)


# write a while loop that adds 1 with the condition that it doesen't exceed 4 
x = 1
while x < 4 :
    print(x)
    x = x + 1
    




 #####################################
# basic while loop
#####################################   
# Create the variable offset with an initial value of 8.
# Code a while loop that keeps running as long as offset is not equal to 0. Inside the while loop:
# Print out the sentence "correcting...".
# Next, decrease the value of offset by 1. You can do this with offset = offset - 1.
# Finally, still within your loop, print out offset so you can see how it changes.

offset = 8
while offset != 0:
    print('correcting....')
    offset = offset - 1
    print(offset)

#####################################
# conditionals in a  while loop
##################################### 

# Inside the while loop, complete the if-else statement:
# If offset is greater than zero, you should decrease offset by 1.
# Else, you should increase offset by 1.

# Initialize offset
offset = -6
# Code the while loop
while offset != 0 :
    print("correcting...")
    if offset > 0:
        offset = offset - 1
    else:
        offset = offset + 1
    print(offset)


#####################################
# for loop
#####################################
# the syntax is       for var in seq:
#                          expression  

# for each variable in the sequence, execute expression.
# this process continues until all variables in sequence have been iterated over

fam = [1.73, 1.68, 1.71, 1.89]
for height in fam:
    print(height)


#####################################
# for loop with an index: use enumerate
#####################################
for index, height in enumerate(fam):
    print(index, height)

for index, height in enumerate(fam):
    print('index ' + str(index) + ": " +  str(height))

for index, height in enumerate(fam):
    print('index ' + str(index + 1) + ": " +  str(height))


#####################################
# loop over a list
#####################################
# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
# Code the for loop
for area in areas :
    print(area)


#####################################
# indexes and values
#####################################
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
for index, area in enumerate(areas) :
    print('room ' + str(index) +  ': ' + str(area))

# start the indexing from 1 for non programmers to understand
for index, area in enumerate(areas) :
    print("room " + str(index + 1) + ": " + str(area))


#####################################
# loop over list of lists
#####################################
house = [["hallway", 11.25], 
         ["kitchen", 18.0], 
         ["living room", 20.0], 
         ["bedroom", 10.75], 
         ["bathroom", 9.50]]

for x in house:
    print("the " + x[0] + " is " + str(x[1]) + " sqm")





#####################################
# loop data structures
#####################################
# 1) dictionary
# 2) numpy array
# 3) dataframe
# they use a similar loop construct, but the way you define the sequence over which you are iterating 
# will differ depending on the data structure


#####################################
# loop over dictionaries
#####################################
# loop over world dictionary
world = {
    "afghanistan" : 30.55,
    "albania" : 2.77,
    "algeria" : 39.21
}
for key, value in world.items():
    print(key + "--" + str(value))
# the names key and value are arbitrary , you can replace them with something else such as k and v

# loop over europe dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna' }
for key, value in europe.items():
    print("the capital of " + key + "is" + str(value))


#####################################
# loop over numpy arrays
#####################################
np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
bmi = np_weight / np_height ** 2
print(bmi)
for val in bmi:
    print(val)

# 2D numpy array
# use numpy function nditer(array you want to iterate over)
# first we get the first array then the second array in that order
meas = np.array([np_height, np_weight])
print(meas)

for val in np.nditer(meas):
    print(val)


#####################################
# loop over dataframes
#####################################
brics = pd.read_csv('brics.csv', index_col=0)
print(brics)

# in pandas, you have to mention explicitly that you want to iterate over the rows
# you do this by calling the iterrows method on the dataframe thus specifying another sequence
# the iterrows method looks at the dataframe and on each iteration generates two pieces of data
#                    1) the label of the row
#                    2) the actual data in the row as a pandas series

# store brics row label as lab, and row data as row
for lab, row in brics.iterrows():
    print(lab)
    print(row)


# print only the  capital. selective print
for lab, row in brics.iterrows():
    print(lab + ': ' + row['capital'])

# Write a for loop that iterates over the rows of cars and on each iteration perform two print() calls: 
# one to print out the row label and one to print out all of the rows contents.
cars = pd.read_csv('cars.csv', index_col=0)
print(cars)

for lab, row in cars.iterrows():
    print(lab)
    print(row)

# The row data that's generated by iterrows() on every run is a Pandas Series. This format is not very convenient to print out. 
# Luckily, you can easily select variables from the Pandas Series using square brackets:
# loop over the label and cars_per_cap 
for lab, row in cars.iterrows() :
    print(lab + ": " + str(row['cars_per_cap']))



#####################################
# add columns to dataframes
#####################################
# add a new column that has the length of country names
# we need the row label and row data
# we calculate the length of each country column by selecting the country column from row and then passing it to the len() function
# then we add this new information to a new column name_length at the appropriate location. Use loc which is label based
for lab, row in brics.iterrows():
    '''create series on each iteration'''
    brics.loc[lab, 'name_length'] = len(row['country'])
print(brics)



# Use a for loop to add a new column, named COUNTRY, that contains a uppercase version of the country names in the "country" column. 
# You can use the string method upper() for this.
# Code for loop that adds COUNTRY column
for lab, row in cars.iterrows():
    cars.loc[lab, 'COUNTRY'] = row['country'].upper()

# Print cars
print(cars)


# Use .apply(str.upper)
cars['COUNTRY'] = cars['country'].apply(str.upper)


# apply is efficient. If you want to calculate an entire dataframe column by applying a function on a particular column 
# in an element-wise fashion. you don't even need a for loop.
# you select the country column from brics dataframe, and then on this column we apply the len function 
# apply calls the len function with each country name as input and produces a new array that you can easily store as a new column, "name_length"

brics['name_length'] = brics['country'].apply(len)
print(brics)
















