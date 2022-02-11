#####################################################################
# FUNDAMENTALS OF PYTHON 9 - Data Field
#####################################################################

# import libraries
import pandas as pd


###################################
# LIST COMPREHENSION
###################################
# creata a new list from an existing list by adding 1
nums = [12, 8, 21, 3, 16]
new_nums = []

for num in nums:
    new_nums.append(num + 1)
print(new_nums)
# for loops are inefficient both computationally and in terms of coding time and space.
# you can write the same code in a single line of code
# A LIST COMPREHENSION
# within square brackets, you can write the values you wish to create otherwise known as the output expression 
# followed by the for clause refewncing the origina list.
nums = [12, 8, 21, 3, 16]
new_nums = [num + 1 for num in nums]
print(new_nums)


# you can write a list comprehension over any iterable 
# List comprehension with range()
result = [num for num in range(11)]
print(result)


# summary
# list comprehensions collapse for loops for building lists into a single line and the required componnents are
# 1) iterable
# 2) an iterator variable that represents the members of the iterable
# 3) an output expression



# you can use list comprehensions in place of nested for loops
# create a list of all pairs of integers where the first integer is between 0 and 1 
# and the second between 6 and 7. 
pairs_1 = []
for num1 in range(0, 2):
    for num2 in range(6, 8):
        pairs_1.append((num1, num2))

print(pairs_1)


# ALTERNATIVELY

pairs_2 = [(num1, num2) for num1 in range(0, 2) for num2 in range(6, 8)]
print(pairs_2)




###################################
# Write a basic list comprehension
###################################
# write a list comprehension that prints the first character of each string
doctor = ['house', 'cuddy', 'chase', 'thirteen', 'wilson']
print([doc[0] for doc in doctor])



# write a list comprehension that produces a list of the squares of the numbers ranging from 0 to 9.
squares = [i ** 2 for i in range(0,10)]
print(squares)




###################################
# Nested list comprehensions
###################################
# Matrices can be represented as a list of lists in Python. 
# For example a 5 x 5 matrix with values 0 to 4 in each row can be written as:

# matrix = [[0, 1, 2, 3, 4],
#           [0, 1, 2, 3, 4],
#           [0, 1, 2, 3, 4],
#           [0, 1, 2, 3, 4],
#           [0, 1, 2, 3, 4]]

# To create the list of lists, you simply have to supply the list comprehension as the output expression 
# of the overall list comprehension:

#    [[output expression] for iterator variable in iterable]      #

# Note that here, the output expression is itself a list comprehension.




# In the inner list comprehension - that is, the output expression of the nested list comprehension 
# - create a list of values from 0 to 4 using range(). Use col as the iterator variable.
# In the iterable part of your nested list comprehension, use range() to count 5 rows - 
# that is, create a list of values from 0 to 4. Use row as the iterator variable; 
# note that you won't be needing this variable to create values in the list of lists.

# Create a 5 x 5 matrix using a list of lists: matrix
matrix = [[col for col in range(5)] for row in range(5)]
# Print the matrix
for row in matrix:
    print(row)






###################################
# Conditionals in comprehensions
###################################
# we can filter the output of a list comprehension using a conditional on the iterable




###################################
# Conditionals on the iterable
###################################
# create a list whose result is the square of the values in range 10 under the condition that the value itself is even
#    [[output expression] for iterator variable in iterable]      #
even_squares = [num **2 for num in range(10) if num % 2 == 0]
print(even_squares)


###################################
# Conditionals on the output expression
###################################
# output the square of every even integer
even_integer_squares = [num ** 2 if num % 2 == 0 else 0 for num in range(10)]
print(even_integer_squares)


###################################
# Dict comprehensions
###################################
# we can write dictionary comprehensiond to create new dictionaries from iterables
# we use {} instead of []
# the key and value are separated by a colon in the output expression

# create a dictionary with keys - positive integers and values - negative integers
pos_neg = {num: -num for num in range(9)}
print(pos_neg)






# Create a dict comprehension where the key is a string in fellowship and the value is the 
# length of the string. Remember to use the syntax <key> : <value> in the output expression 
# part of the comprehension to create the members of the dictionary. Use member as the iterator variable.

# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']
# Create dict comprehension: new_fellowship
new_fellowship = {member: len(member) for member in fellowship}
# Print the new dictionary
print(new_fellowship)





###################################
# Conditionals on the iterator variables
###################################
#  you can apply a conditional statement to test the iterator variable by adding an if statement 
# in the optional predicate expression part after the for statement in the comprehension:

#   [ output expression for iterator variable in iterable if predicate expression ] #

# Use member as the iterator variable in the list comprehension. 
# For the conditional, use len() to evaluate the iterator variable. 
# Note that you only want strings with 7 characters or more.


# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']
# Create list comprehension: new_fellowship
new_fellowship = [member for member in fellowship if len(member) >= 7]
# Print the new list
print(new_fellowship)





###################################
# Conditionals on the output expression
###################################
# In the output expression, keep the string as-is if the number of characters is >= 7, 
# else replace it with an empty string - that is, '' or "".

# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']
# Create list comprehension: new_fellowship
new_fellowship = [member if len(member) >= 7 else "" for member in fellowship]
# Print the new list
print(new_fellowship)











#########################################
# Generators
#########################################
# A generator is like a list comprehension except it does not store the list in memory.
# A generator does not construct a list but is an ob=ject we can iterate over to produce elements of the list as required.
# generators use () instead of []

result = (num for num in range(10))
for num in result:
    print(num)

# we can pass a generator to the function list to create a list
result = (num for num in range(10))
print(list(result))

# Like any other iterator, we can pass a generator to the function next in order to iterate through its elements.
result = (num for num in range(10))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))

##########################################
# conditionals on generator expressions
##########################################
even_nums = (num for num in range(10) if num % 2 == 0)
print(list(even_nums))


##########################################
# Generator functions
##########################################
# Generator functions are functions that when called produce generator objects. 
# They are written with the syntax of any other user defined functions. However, 
# instead of returning values with the keyword return, they yield sequences of values using the keyword yield.



# define a generator function that whenever called with a number n, produces a generator object that generates integers 0 through n.
# i is initialized at 0. The first time the generator function is called,it yields i = 0.  It then adds 1 to i and will then yield 1 
# on the next iteration and so on. The while loop is true until i = n then the generator ceases to yield values.

def num_sequence(n):
    '''Generate values from 0 to n.'''
    i = 0
    while i < n:
        yield i
        i += 1

result = num_sequence(5)
print(type(result))

for item in result:
    print(item)





##########################################
# write your own Generator functions
##########################################
# Create a generator object that will produce values from 0 to 30. 
# Assign the result to result and use num as the iterator variable in the generator expression.
# Print the first 5 values by using next() appropriately in print().
# Print the rest of the values by using a for loop to iterate over the generator object.

# Create generator object: result
result = (num for num in range(0, 31))
# Print the first 5 values
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
# Print the rest of the values
for value in result:
    print(value)




##########################################
# Changing the output in generator expressions
##########################################
# Write a generator expression that will generate the lengths of each string in lannister.
#  Use person as the iterator variable. Assign the result to lengths.
# Supply the correct iterable in the for loop for printing the values in the generator object.


# Create a list of strings: lannister
lannister = ['cersei', 'jaime', 'tywin', 'tyrion', 'joffrey']
# Create a generator object: lengths
lengths = (len(person) for person in lannister)
# Iterate over and print the values in lengths
for value in lengths:
    print(value)






##########################################
# Build a  Generator 
##########################################
 # Complete the function header for the function get_lengths() that has a single parameter, input_list.
# In the for loop in the function definition, yield the length of the strings in input_list.
# Complete the iterable part of the for loop for printing the values generated by the get_lengths() generator function. 
# Supply the call to get_lengths(), passing in the list lannister.


# Create a list of strings
lannister = ['cersei', 'jaime', 'tywin', 'tyrion', 'joffrey']
# Define generator function get_lengths
def get_lengths(input_list):
    """Generator function that yields the
    length of the strings in input_list."""
    # Yield the length of a string
    for person in input_list:
        yield len(person)
# Print the values generated by get_lengths()
for value in get_lengths(lannister):
    print(value)






# Twitter data
df = pd.read_csv('tweets.csv')
print(df.info())



# Extract the column 'created_at' from df and assign the result to tweet_time. 
# Fun fact: the extracted column in tweet_time here is a Series data structure!
# Create a list comprehension that extracts the time from each row in tweet_time. 
# Each row is a string that represents a timestamp, and you will access the 12th to 19th characters in the string to extract the time. 
# Use entry as the iterator variable and assign the result to tweet_clock_time. Remember that Python uses 0-based indexing!

# Extract the created_at column from df: tweet_time
tweet_time = df['created_at']
# Extract the clock time: tweet_clock_time
tweet_clock_time = [entry[11:19] for entry in tweet_time]
# Print the extracted times
print(tweet_clock_time)





# Extract the column 'created_at' from df and assign the result to tweet_time.
# Create a list comprehension that extracts the time from each row in tweet_time. 
# Each row is a string that represents a timestamp, and you will access the 12th to 19th characters in the string to extract the time. 
# Use entry as the iterator variable and assign the result to tweet_clock_time. 
# Additionally, add a conditional expression that checks whether entry[17:19] is equal to '19'.


# Extract the created_at column from df: tweet_time
tweet_time = df['created_at']
# Extract the clock time: tweet_clock_time
tweet_clock_time = [entry[11:19] for entry in tweet_time if entry[17:19] == '19']
# Print the extracted times
print(tweet_clock_time)