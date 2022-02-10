#####################################################################
# FUNDAMENTALS OF PYTHON 8 - Data Field
#####################################################################
# import libraries
import pandas as pd

############################################
# ITERATORS, ITERABLES
############################################
# iterators vs iterable
# an iterable is an object that can return an iterator, 
# while an iterator is an object that keeps state and produces the next value when you call next() on it



###################################
# ITERATING WITH A FOR LOOP
####################################

# LIST
employees = ['Nick', 'Lore', 'Hugo']
for employee in employees:
    print(employee)

# STRING
for letter in 'Nairobi':
    print(letter)

# SEQUENCE
for i in range(10):
    print(i)


# ITERABLE an object that has an associated iter() method
# ITERATOR an object that has an associated next() method that produces the consecutive values

# an iterable is an object that can return an iterator
# while an iterator is an object that keeps state and produces the next value when you call next()

# The reason why we can loop over such objects is that they are special objects called iterables
# Examples of Iterables - (lists, strings, dictionaries, file connections)
# An iterable is an object that has an associated iter method.
# once this iter method is applied to an iterable, an iterator object is created.
# the for loop takes an iterable, creates the associated iterator object and iterates over it.
# An iterator is defined as an object that has an associated next method that produces the consecutive values.



###################################
# iterating over iterables: next()
####################################
# To create an iterator from an iterable, use the function iter() and pass it the iterable.
# once we have the iterator defined, we pass it to the function next and this returns first value.
# calling next again on the iterator returns the next value. 
# Once it is done, an error message of stop iteration is printed.

word = 'David'
it = iter(word)

print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

# Iterate once using the star operator or splat!
# This star operator unpacks all elements of an iterator and can only be used once
school = "Technical"
it = iter(school)
print(*it)





###################################
# ITERATING OVER DICTIONATIES.
###################################
# we need to unpack them by applying the items method.
pythonistas = {'David': 'Karanja', 'Wayne': 'Kiprop'}
for key, value in pythonistas.items():
    print(key, value)





###################################
#ITERATING OVER FILE CONNECTIONS
###################################
# file = open('file.txt')
# it = iter(file)
# print(next(it))
# print(next(it))
# print(next(it))



###################################
# ITERATING OVER ITERABLES
##################################
# Create a list of strings: flash
flash = ['jay garrick', 'barry allen', 'wally west', 'bart allen']
# Print each list item in flash using a for loop
for person in flash:
    print(person)


# Create an iterator for flash: superhero
superhero = iter(flash)
# Print each item from the iterator
print(next(superhero))
print(next(superhero))
print(next(superhero))
print(next(superhero))





###################################
# ITERATING OVER ITERABLES
##################################
# Create an iterator for range(3): small_value
# use iter() function to get iterator object
small_value = iter(range(3))
# Print the values in small_value
# use next() function to retrieve values one by one from the iterator object
print(next(small_value))
print(next(small_value))
print(next(small_value))



# Loop over range(3) and print the values
for num in range(3):
    print(num)



# Create an iterator for range(10 ** 100): googol
googol = iter(range(10 ** 100))
# Print the first 5 values from googol
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))





#######################################
# Iterators as function arguments
########################################
# Create a range object: values
values = range(10, 21)
# Print the range object
print(values)
# Create a list of integers: values_list
values_list = list(values)
# Print values_list
print(values_list)
# Get the sum of values: values_sum
values_sum = sum(values)
# Print values_sum
print(values_sum)





################################
# enumerate and zip
################################
# Functions used with iterators - enumerate will allow us to add a counter to any iterable
# while zip will allow us to stitch together an abitrary number of iterables


##########################
# enumerate
#########################
# a function that takes any iterable as argument, such as a list and returns a special enumerate object
# which consists of pairs containing the elements of the original iterable 
# along with their index within the iterable

avengers = ['hawkey', 'iron man', 'thor', 'quicksilver']
e = enumerate(avengers)
print(type(e))

# we can use the function list to turn this enumerate object into a list of tuples and print it to see what it contains
e_list = list(e)
print(e_list)

# the enumerate object itself is also an iterable and we can loop over it while unpacking its elements 
# using the clause for index, 
avengers = ['hawkey', 'iron man', 'thor', 'quicksilver']
for index, value in enumerate(avengers):
    print(index, value)

# the print out will start from 0. You can alter this with a second argument start.
for index, value in enumerate(avengers, start = 1):
    print(index, value)





#####################################
# zip
#####################################
# zip accepts an arbitrary number of iterables and returns an iterator of tuples
avengers = ['hawkey', 'iron man', 'thor', 'quicksilver']
names = ['barton', 'stark', 'ordinson', 'maximoff']
# zipping them together creates a zip object which is an iterator of tuples.
# we can turn this zip into a list and print it out
z = zip(avengers, names)
print(type(z))
z_list = list(z)
print(z_list)
# the first element is a tuple containing the first element of each list that was zipped
# the second elemrnt is a tuple containing the second element of each list that was zipped




# ALTERNATIVELY, we can use a for loop to iterate over the zip object and print the tuples
for z1, z2 in zip(avengers, names):
    print(z1, z2)


# ALTERNATIVELY, we can use the splat operator to print all the elements
z = zip(avengers, names)
print(*z)





########################################
# using enumerate
#######################################
# enumerate() returns an enumerate object that produces a sequence of tuples, 
# and each of the tuples is an index-value pair.

# Create a list of strings: mutants
mutants = ['charles xavier', 
            'bobby drake', 
            'kurt wagner', 
            'max eisenhardt', 
            'kitty pryde']
# Create a list of tuples: mutant_list
mutant_list = list(enumerate(mutants))
# Print the list of tuples
print(mutant_list)
# Unpack and print the tuple pairs
for index1, value1 in enumerate(mutants):
    print(index1, value1)
print()
# Change the start index
for index2, value2 in enumerate(mutants, start = 1):
    print(index2, value2)



print()



########################################
# using zip
#######################################
mutants = ['charles xavier', 'bobby drake', 'kurt wagner', 'max eisenhardt', 'kitty pryde']
aliases = ['prof x', 'iceman', 'nightcrawler', 'magneto', 'shadowcat']
powers = ['telepathy', 'thermokinesis', 'teleportation', 'magnetokinesis', 'intangibility']

# Create a list of tuples: mutant_data
mutant_data = list(zip(mutants, aliases, powers))
# Print the list of tuples
print(mutant_data)
print()
# Create a zip object using the three lists: mutant_zip
mutant_zip = zip(mutants, aliases, powers)
# Print the zip object
print(mutant_zip)
print()
# Unpack the zip object and print the tuple values
for value1, value2, value3 in mutant_zip:
    print(value1, value2, value3)



print()



##########################################
# Using * and zip to 'unzip'
##########################################
# There is no unzip function for doing the reverse of what zip() does. 
# We can, however, reverse what has been zipped together by using zip() with a little help from *! * unpacks an 
# iterable such as a list or a tuple into positional arguments in a function call.
mutants = ['charles xavier', 'bobby drake', 'kurt wagner', 'max eisenhardt', 'kitty pryde']
powers = ['telepathy', 'thermokinesis', 'teleportation', 'magnetokinesis', 'intangibility']

# Create a zip object from mutants and powers: z1
z1 = zip(mutants, powers)
# Print the tuples in z1 by unpacking with *
print(*z1)
# Re-create a zip object from mutants and powers: z1
z1 = zip(mutants, powers)
# 'Unzip' the tuples in z1 by unpacking with * and zip(): result1, result2
result1, result2 = zip(*z1)
# Check if unpacked tuples are equivalent to original tuples
print(result1 == mutants)
print(result2 == powers)




##########################################################
# Using Iterators to load large files into memory
########################################################## 
# Loading large amounts of data such that it can't be held in memory
# load the data in chunks, performm the desired operation on each chunk, store the result, discard the chunk then load the next chunk of data
# specify the chunk using the argument chunksize

# suppose we have a csv with a column x and we want to compute the sum of all the numbers in the column
# initialize an empty list result to hold the result of each iteration
# read the chunk, each chunk will be a dataframe. Within a for loop, on each iteration, we compute the sum of column of interest 
# and we append it to the list result
# taking sum of the list result gives the total sum of the column   


#           import pandas as pd
#           result = []
#           for chunk in pd.read_csv('data.csv', chunksize = 1000):
#               result.append(sum(chunk['x']))
#           total = sum(result)
#           print(total)



print()
# ALTERNATIVELY


#           import pandas as pd
#           total = 0
#           for chunnk in pd.read_csv('data.csv', chunksize =1000):
#              total += sum(chunk['x'])
#           print(total)



##########################################################
# processing large amounts of Twitter data
##########################################################
#Initialize an empty dictionary counts_dict for storing the results of processing the Twitter data.
# Iterate over the 'tweets.csv' file by using a for loop. 
# Use the loop variable chunk and iterate over the call to pd.read_csv() with a chunksize of 10.
# In the inner loop, iterate over the column 'lang' in chunk by using a for loop. Use the loop variable entry.


# # Initialize an empty dictionary: counts_dict
counts_dict = {}
# Iterate over the file chunk by chunk
for chunk in pd.read_csv('tweets.csv', chunksize=10):
    # Iterate over the column in DataFrame
    for entry in chunk['lang']:
        if entry in counts_dict.keys():
            counts_dict[entry] += 1
        else:
            counts_dict[entry] = 1
# Print the populated dictionary
print(counts_dict)





##########################################################
# Extracting information for large amounts of Twitter data
##########################################################
# Define the function count_entries(), which has 3 parameters. 
# The first parameter is csv_file for the filename, the second is c_size for the chunk size, 
# and the last is colname for the column name.
# Iterate over the file in csv_file file by using a for loop. Use the loop variable chunk and iterate over the call to pd.read_csv(),
#  passing c_size to chunksize.
# In the inner loop, iterate over the column given by colname in chunk by using a for loop. Use the loop variable entry.
# Call the count_entries() function by passing to it the filename 'tweets.csv', 
# the size of chunks 10, and the name of the column to count, 'lang'. Assign the result of the call to the variable result_counts.


# Define count_entries()
def count_entries(csv_file, c_size, colname):
    """Return a dictionary with counts of
    occurrences as value for each key."""   
    # Initialize an empty dictionary: counts_dict
    counts_dict = {}
    # Iterate over the file chunk by chunk
    for chunk in pd.read_csv(csv_file, chunksize=c_size):
        # Iterate over the column in DataFrame
        for entry in chunk[colname]:
            if entry in counts_dict.keys():
                counts_dict[entry] += 1
            else:
                counts_dict[entry] = 1
    # Return counts_dict
    return counts_dict
# Call count_entries(): result_counts
result_counts = count_entries('tweets.csv', 10, 'lang')
# Print result_counts
print(result_counts)


















