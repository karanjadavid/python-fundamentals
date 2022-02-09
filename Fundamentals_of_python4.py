#####################################################################
# FUNDAMENTALS OF PYTHON 3 - Data Field
#####################################################################

# import libraries
import pandas as pd


#####################################################################
# USER DEFINED FUNCTIONS - BASIC FUNCTIONS
#####################################################################

# 1) define functions wihout parameters
# 2) define functions with one parameter
# 3) define functions that return a value
# 4) functions that have multiple arguments / return multiple values



# the first line of a function is the function header that has the keyword def, 
# the function name, followed by a set of parenthesis and colon.
# after the function header, we have docstrings which describe what the function does.
#   docstrings serve as documentation for your function
#   docstrings are placed between tripple quotation marks
# then the function body which houses the code to be executed. It should be indented 4 spaces.
# whenever the function is called, the code in the function body is run.



#####################################
# define functions wihout parameters
#####################################

# build a function that squares a number
def square():
    '''returns the square of a value'''
    new_value = 10 ** 2
    print(new_value)
# call the function=
square()



# Define the function shout
def shout():
    """Print a string with three exclamation marks"""
    # Concatenate the strings: shout_word
    shout_word = 'congratulations' + '!!!'
    # Print shout_word
    print(shout_word)
# Call shout
shout()



#####################################
# define functions with a single  parameter
#####################################

# when you define a function, you write parameters in the function header.
# when you call a function, you pass arguments into the function.

# Functions with parameters
def squared_par(value):
    '''returns the square of a value'''
    new_val = value ** 2
    print(new_val)
# call the function. Try different parameters
squared_par(5)
squared_par(8)



# Define shout with the parameter, word
def shout(word):
    """Print a string with three exclamation marks"""
    # Concatenate the strings: shout_word
    shout_word = word + '!!!'
    # Print shout_word
    print(shout_word)
# Call shout with the string 'congratulations'
shout('congratulations')





# Return values from functions
# return keyword lets you return values from functions. 
# Returning values is generally more desirable than printing them out because, 
# as you saw earlier, a print() call assigned to a variable has type NoneType

def squared(value):
    '''returns the square of a value'''
    new_value = value ** 2
    return new_value
num = squared(4)
print(num)


# Define shout with the parameter, word
def shout(word):
    """Return a string with three exclamation marks"""
    # Concatenate the strings: shout_word
    shout_word = word + '!!!'
    # Replace print with return
    return shout_word
# Pass 'congratulations' to shout: yell
yell = shout('congratulations')
# Print yell
print(yell)



#####################################
# define functions with multiple parameters
#####################################

# make note of the order of arguments

# Multiple parameters and return values
def raise_to_power(value1, value2):
    '''Raise value1 to the power of value2.'''
    new_value = value1 ** value2
    return new_value
# in the call function, number of arguments = number of parameters
raise_to = raise_to_power(12,2)
print(raise_to)



# Define shout with parameters word1 and word2
def shout(word1, word2):
    """Concatenate strings with three exclamation marks"""
    # Concatenate word1 with '!!!': shout1
    shout1 = word1 + '!!!'   
    # Concatenate word2 with '!!!': shout2
    shout2 = word2 + '!!!'    
    # Concatenate shout1 with shout2: new_shout
    new_shout = shout1 + shout2
    # Return new_shout
    return new_shout
# Pass 'congratulations' and 'you' to shout: yell
yell = shout('congratulations', 'you')
# Print yell
print(yell)



#####################################
# define functions that return multiple values
#####################################
# do this by constructing objects known as Tuples.

# a Tuple is like a list in that it can contain multiple values
# a Tuple is immutable. Meaning you can't modify values!
# a Tuple is constructed using parenthesis. use () instead of [].



# Unpacking tuples
even_nums = (2, 4, 6)
a, b , c = even_nums
print(a)
print(b)
print(c)
# Access tuple elements 
print(even_nums[1])



nums = (3, 4, 6)
# Unpack nums into num1, num2, and num3
num1, num2, num3 = nums
# Construct even_nums
even_nums = (2, num2, num3)
# note, to unpack a 2-tuple tup into two variable a, b, execute a, b = tup.





def raise_both(value1, value2):
    '''Raise value1 to the power of value2 and value2 to the power of value1'''
    new_value1 = value1 ** value2
    new_value2 = value2 ** value1
    new_tuple = (new_value1, new_value2)
    return(new_tuple)

result = (raise_both(2,3))
print(result)





# Define shout_all with parameters word1 and word2
def shout_all(word1, word2):
    """Return a tuple of strings"""
    # Concatenate word1 with '!!!': shout1
    shout1 = word1 + '!!!'    
    # Concatenate word2 with '!!!': shout2
    shout2 = word2 + '!!!'   
    # Construct a tuple with shout1 and shout2: shout_words
    shout_words = (shout1, shout2)
    # Return shout_words
    return shout_words
# Pass 'congratulations' and 'you' to shout_all(): yell1, yell2
yell1, yell2 = shout_all('congratulations', 'you')
# Print yell1 and yell2
print(yell1)
print(yell2)





# Twitter data
# The dataset contains Twitter data and you will iterate over entries in a column to build a dictionary in which 
# the keys are the names of languages and the values are the number of tweets in the given language. 


# Complete the for loop by iterating over col, the 'lang' column in the DataFrame df.
# if the key is in the dictionary langs_count, add 1 to the value corresponding to this key in the dictionary, 
# else add the key to langs_count and set the corresponding value to 1. Use the loop variable entry in your code.


# Import Twitter data as DataFrame: df
tweets = pd.read_csv('tweets.csv')
# Initialize an empty dictionary: langs_count
langs_count = {}
# Extract column from DataFrame: col
col = tweets['lang']
print(col)
# Iterate over lang column in DataFrame
for entry in col:
    # If the language is in langs_count, add 1
    if entry in langs_count.keys():
        langs_count[entry] += 1
    # Else add the language to langs_count, set the value to 1
    else:
        langs_count[entry] = 1
# Print the populated dictionary
print(langs_count)





# Twitter data 2
# Define the function count_entries(), which has two parameters. 
# The first parameter is df for the DataFrame and the second is col_name for the column name.
# Complete the bodies of the if-else statements in the for loop: if the key is in the dictionary langs_count, 
# add 1 to its current value, else add the key to langs_count and set its value to 1. Use the loop variable entry in your code.
# Return the langs_count dictionary from inside the count_entries() function.
# Call the count_entries() function by passing to it tweets_df and the name of the column, 'lang'. 
# Assign the result of the call to the variable result.


# Define count_entries()
def count_entries(df, col_name):
    """Return a dictionary with counts of 
    occurrences as value for each key."""
    # Initialize an empty dictionary: langs_count
    langs_count = {}    
    # Extract column from DataFrame: col
    col = tweets['lang']
    # Iterate over lang column in DataFrame
    for entry in col:
        # If the language is in langs_count, add 1
        if entry in langs_count.keys():
            langs_count[entry] += 1
        # Else add the language to langs_count, set the value to 1
        else:
            langs_count[entry] = 1
    # Return the langs_count dictionary
    return langs_count
# Call count_entries(): result
result = count_entries(tweets, 'lang')
# Print the result
print(result)



