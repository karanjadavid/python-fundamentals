#####################################################################
# FUNDAMENTALS OF PYTHON 2 - Data Field
#####################################################################

#import libraries
import pandas as pd



# 1) DICTIONARIES AND PANDAS




#####################################################################
# Dictionaries 
#####################################################################
# A dictionary is a python type that is intuitive and efficient
# Dictinaries are created with curly braces and have key value pairs 
# The keys are unique , no duplicates. They are immutable objects
# The key opens the door to the values



# suppose we have two lists and want to get which country corresponds to which city
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']
ind_ger = countries.index('germany')
print(ind_ger)
print(capitals[ind_ger])



# Creating a dictionary recipe   
# 
#                    
#                                 my_dict = {
#                                             "key1":"value1",
#                                             "key2":"value2",
#                                           }
  

########################################
# create a dictionary
########################################

# From the lists, create a dictionary: call it europe
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

europe = { 'spain': 'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo'}
print(europe)
print(type(europe))


########################################
# access elements in a  dictionary
########################################
europe = { 'spain': 'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo'}
# print the keys in europe
print(europe.keys())
# print out the value that belongs to key france
print(europe['france'])


########################################
# adding elements to a  dictionary
########################################
# to add elements to a dictionary, pass the key inside square brackets. make it equal the value
# add netherlands and a capital budapest to europe
europe['netherlands'] = 'budapest'
# check if its successfully added
print('netherlands' in europe)
print(europe)


########################################
# updating elements to a  dictionary
########################################
# you realize netherlands capital is not budapest but amsterdam instead. change / update europe
europe['netherlands'] = 'amsterdam'
print(europe)


########################################
# deleting elements to a  dictionary
########################################
# delete netherlands from europe
del(europe['netherlands'])
print(europe)


########################################
# dictionary of dictionaries
########################################

# Dictionary of dictionaries
europe1 = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }

# Print out the capital of France
print(europe1['france']['capital'])
# Create sub-dictionary data
data = { 'capital':'rome', 'population':59.83 }
# Add data to europe under key 'italy'
europe1['italy'] = data
# Print europe
print(europe1)






#####################################################################
#  Pandas
#####################################################################
# Pandas is a high level data manipulation tool 
# In pandas data is stored in a data frame. rows represent observations and columns the variables


########################################
# dictionaries to dataframe
########################################
# the keys are the column labels while the values have data column by column
dict_nations = {
    "country":["Brazil", "Russia", "India", "China", "South Africa"],
    "capital":["Brasilia", "Moscow", "New Delhi", "Beijing", "Pretoria"],
    "area":[8.516,17.10,3.286,9.597,1.221],
    "population":[200.4,143.5,1252,1357,52.98]}

brics_df = pd.DataFrame(dict_nations)
print(brics_df)
# pandas gives some automatic row labels which we can change
brics_df.index = ["BR","RU","IN","CH","SA"]
print(brics_df)





# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
# Create dictionary my_dict with three key:value pairs: my_dict
my_dict = { 'country':names, 'drives_right':dr, 'cars_per_cap':cpc }
# Build a DataFrame cars from my_dict: cars
cars = pd.DataFrame(my_dict)
# Definition of row_labels
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']
# Specify row labels of cars
cars.index = row_labels
# Print cars
print(cars)



########################################
# csv to dataframe
########################################

# index_col = 0 gets rid of the index column 
brics = pd.read_csv('brics.csv', index_col = 0)
print(brics)


# import cars csv file to python
cars1 = pd.read_csv('cars.csv', index_col=0)
print(cars1)




########################################
# index and select from pandas dataframe
########################################
# we can use square brackets 

# 1) COLUMN ACCESS

# select only the country column from brics dataframe
# take the dataframe, then column label inside square brackets
# single square brackets outputs a pandas series and not a dataframe
brics_country = brics['country']
print(brics_country)
print(type(brics_country))

# use double square brackets to get a dataframe 
brics_country = brics[['country']]
print(brics_country)
print(type(brics_country))

# select more than one column. sub dataframe
# we put a list with column labels inside a set of square brackets
print(brics[['country', 'capital']])

# cars1 dataframe column access
# Print out country column as Pandas Series
print()
print('cars dataframe')
print(cars1['country'])
# Print out country column as Pandas DataFrame
print(cars1[['country']])
# Print out DataFrame with country and drives_right columns
print(cars1[['country','drives_right']])







# 2) ROW ACCESS

# we slice the rows we need
# get the second, third and fourth rows of brics.
# remember, indexing starts from zero and the end of the slice is exclusive
print(brics[1:4])


# cars1 dataframe row access
# Print out first 3 observations
print(cars[0:3])
# Print out fourth, fifth and sixth observation
print(cars[3:6])




########################################
# loc and iloc 
########################################
# select rows and columns in a pandas dataframe
# loc - selects based on labels
# iloc - selection is position based 






########################################
# loc
########################################

# single brackets gives a pandas series giving all the rows info
# double brackets gives a pandas dataframe giving all the rows info

########################################
# loc to select rows
########################################
# access Russia from the brics dataframe using loc
print()
print(brics.loc["RU"])
print(brics.loc[["RU"]])

# select multiple rows, India and China
print(brics.loc[['RU', 'IN', 'CH']])

########################################
# loc to select rows and columns
########################################
# the first bracket contains the row index and the second square bracket contains the column labels
print(brics.loc[['RU', 'IN', 'CH'],['country', 'capital']])

########################################
# loc to select all rows, specific columns
########################################
# have the first list that represents rows as a colon
print(brics.loc[:,['country', 'capital']])










########################################
# iloc
########################################
# subset pandas dataframes based on the position or index

########################################
# iloc to select rows
########################################
# access Russia from the brics dataframe using iloc
# pandas series
print(brics.iloc[1])
# pandas dataframe
print(brics.iloc[[1]])

# select multiple rows, India and China
print(brics.iloc[[1,2,3]])

########################################
# iloc to select rows and columns
########################################
# the first bracket contains the row index and the second square bracket contains the column label indexes
print(brics.iloc[[1,2,3],[1,2]])

########################################
# iloc to select all rows, specific columns
########################################
# have the first list that represents rows as a colon
print(brics.iloc[:,[1,2]])


# cars dataframe 
print()
print('cars dataframe')
print(cars1)

# Print out observation for Japan pandas series
print(cars1.iloc[2])
# Print out observations for Australia and Egypt pandas dataframe
print(cars1.loc[['AUS', 'EG']])

# Print out drives_right value of Morocco
print(cars1.iloc[5, 2])
# Print sub-DataFrame
print(cars1.loc[['RU', 'MOR'], ['country', 'drives_right']])

# Print out drives_right column as Series
print(cars1.iloc[:, 2])
# Print out drives_right column as DataFrame
print(cars1.iloc[:, [2]])
# Print out cars_per_cap and drives_right as DataFrame
print(cars1.loc[:, ['cars_per_cap', 'drives_right']])