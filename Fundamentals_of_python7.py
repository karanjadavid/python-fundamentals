#####################################################################
# FUNDAMENTALS OF PYTHON 7 - Data Field
#####################################################################

####################################################
# LAMBDA FUNCTIONS AND ERROR HANDLING
####################################################

# import libraries
import pandas as pd



##########################
# LAMBDA FUNCTIONS
###########################
# There is a quicker way to write functions on the fly
# we use lambda functions that use the keyword lambda

# after the keyyword lambda, we specify the names of the arguments, 
# then a colon followed by an expression of what we expect the function to return
# lambda allows you to write functions in a quick and dirty way
raise_to_power = lambda x, y: x ** y
print(raise_to_power(2, 3))



#######################
# ANONYMOUS FUNCTIONS
#######################
# situations where lambda comes in handy
# map() function takes in two argumnents, map(func, seq) a function and a sequence 
# such as a list and applies to the function over all elements of the sequence
# we can pass lambda functions to map without even naming them and in this case, we refer to them as anonymous functions 

nums = [48, 6, 9, 21, 1]
square_all = map(lambda num: num ** 2, nums)
print(square_all)
print(list(square_all))




# write a lambda function add_bangs that adds three exclamation points '!!!' to the end of a string a
# call add_bangs with the argument 'hello'

add_bangs = (lambda a: a + '!!!')
print(add_bangs('Hello'))





#######################
# CONVERT TO LAMBDA FUNCTIONS
#######################
# Convert this function to  lambda function
def echo_word(word1, echo):
    """Concatenate echo copies of word1."""
    words = word1 * echo
    return words
print(echo_word("David", 3))




# Define echo_word as a lambda function: echo_word
echo_word = (lambda word1, echo: word1 * echo)
# Call echo_word: result
result = echo_word('David', 3)
# Print result
print(result)



#########################################
# map and lambda functions
#########################################

# map() applies a function over an object, such as a list. 
# Here, you can use lambda functions to define the function that map()

# You can see here that a lambda function, which raises a value a to the power of 2, 
# is passed to map() alongside a list of numbers, nums. 
# The map object that results from the call to map() is stored in result

nums = [2, 4, 6, 8, 10]
result = map(lambda a: a ** 2, nums)
print(result)
print(list(result))







# In the map() call, pass a lambda function that concatenates the string '!!!' to a string item; 
# also pass the list of strings, spells. Assign the resulting map object to shout_spells.
# Convert shout_spells to a list and print out the list.

# Create a list of strings: spells
spells = ['protego', 'accio', 'expecto patronum', 'legilimens']
# Use map() to apply a lambda function over spells: shout_spells
shout_spells = map(lambda item: item + '!!!', spells)
# Convert shout_spells to a list: shout_spells_list
shout_spells_list = list(shout_spells)
# Print the result
print(shout_spells_list)








############################################
# Filter() and lambda functions
############################################
# The function filter() offers a way to filter out elements from a list that don't satisfy certain criteria
# In the filter() call, pass a lambda function and the list of strings, fellowship. 
# The lambda function should check if the number of characters in a string member is greater than 6; 
# use the len() function to do this. Assign the resulting filter object to result.

# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'pippin', 'aragorn', 'boromir', 'legolas', 'gimli', 'gandalf']
# Use filter() to apply a lambda function over fellowship: result
result = filter(lambda member: len(member) > 6, fellowship)
# Convert result to a list: result_list
result_list = list(result)
# Print result_list
print(result_list)




##########################################
# Reduce() and Lambda functions
##########################################

#  The reduce() function is useful for performing some computation on a list and, 
# unlike map() and filter(), returns a single value as a result. 
# To use reduce(), you must import it from the functools module.


# gibberish() simply takes a list of strings as an argument and returns, as a single-value result, 
# the concatenation of all of these strings. Replicate this functionality by using reduce() and a lambda function 
# that concatenates strings together.

# Define gibberish
def gibberish(*args):
    hodgepodge = ''
    for word in args:
        hodgepodge += word
    return hodgepodge

print(gibberish("Angela", "Lucy"))





# Import the reduce function from the functools module.
#In the reduce() call, pass a lambda function that takes two string arguments item1 and item2 and concatenates them; 
# also pass the list of strings, stark. Assign the result to result. 
# The first argument to reduce() should be the lambda function and the second argument is the list stark.

# Import reduce from functools
from functools import reduce
# Create a list of strings: stark
stark = ['robb', 'sansa', 'arya', 'brandon', 'rickon']
# Use reduce() to apply a lambda function over stark: result
result = reduce(lambda item1, item2: item1 + item2, stark)
# Print the result
print(result)




#################################################
# INTRODUCTION TO ERROR HANDLING
#################################################
# when you use a function incorrectly, it should throw you an error


# passing an incorrect aargument
print(float(2))

# if i pass in a string hello, python will throw an error, saying it couldn't convert a string to a float
##############  print(float('hello'))    #######################
# ValueError: could not convert string to float: 'hello'


# when we write our own functions, we may wish to catch specific problems and write specific error messages

def sqrt(x):
    '''Returns the square root of a number'''
    return x ** (0.5)

print(sqrt(16))

# what if we pass a string such as hello
##################   print(sqrt('hello'))    ########################
# TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'float'





# ERRORS AND EXCEPTIONS
# the error above is a type caught during execution called EXCEPTIONS.
# the main way to catch such exceptions is the try-except clause in which python tries to run the 
# code following try and if it can, all is well. If it cannot, due to an exception, it runs the code following except


def sqrt(y):
    '''Returns the square root of a number'''
    try:
        return y ** 0.5
    except:
        print('y must be an int or a float')

print(sqrt(144))
print(sqrt('House'))



print()



# We may want to catch type errors and let others errors pass through
def sqrt(y):
    '''Returns the square root of a number'''
    try:
        return y ** 0.5
    except TypeError:
        print('y must be an int or a float')

print(sqrt(400))
print(sqrt('Donkey'))



print()

#######################################
# raising an error
#######################################
# the square root of a negative number gives a complex number which we may not want
####print(sqrt(-9))
# lets say we don't want our function to work when it comes across a negative number




def sqrt(z):
    '''Returns the square root of a number'''
    if z < 0:
        raise ValueError("x must be non negative")
    try:
        return z ** 0.5
    except TypeError:
        print('x must be an int or a float')


print(sqrt(4))
# print(sqrt(-9)) --> value error is printed out with the message "x must be non negative"
print()





#######################################
# ERROR HANDLING WITH TRY AND EXCEPT
#######################################
# Initialize the variables echo_word and shout_words to empty strings.
# Add the keywords try and except in the appropriate locations for the exception handling block.
# Use the * operator to concatenate echo copies of word1. Assign the result to echo_word.
#Concatenate the string '!!!' to echo_word. Assign the result to shout_words.

# Define shout_echo
def shout_echo(word1, echo=1):
    """Concatenate echo copies of word1 and three
    exclamation marks at the end of the string."""
    # Initialize empty strings: echo_word, shout_words
    echo_word = ''
    shout_words = ''
    # Add exception handling with try-except
    try:
        # Concatenate echo copies of word1 using *: echo_word
        echo_word = word1 * echo
        # Concatenate '!!!' to echo_word: shout_words
        shout_words = echo_word + '!!!'
    except:
        # Print error message
        print("word1 must be a string and echo must be an integer.")
    # Return shout_words
    return shout_words
# Call shout_echo - the function throws an error here.
print(shout_echo("particle", echo="accelerator"))
# calling the function below executes
print(shout_echo("particle", echo=3))






# same exmple without commenting
def shout_echo(word1, echo=1):
    echo_word = ''
    shout_words = ''
    try:
        echo_word = word1 * echo
        shout_words = echo_word + '!!!'
    except:
        print("word1 must be a string and echo must be an integer.")
    return shout_words
shout_echo("particle", echo="accelerator")





#######################################
# ERROR HANDLING BY RAISING AN ERROR
#######################################
# Complete the if statement by checking if the value of echo is less than 0.
# In the body of the if statement, add a raise statement that raises a ValueError with message 'echo must be greater than or equal to 0' 
# when the value supplied by the user to echo is less than 0.





# Define shout_echo
def shout_echo(word1, echo=1):
    """Concatenate echo copies of word1 and three
    exclamation marks at the end of the string."""
    # Raise an error with raise
    if echo < 0:
        raise ValueError('echo must be greater than or equal to 0')
    # Concatenate echo copies of word1 using *: echo_word
    echo_word = word1 * echo
    # Concatenate '!!!' to echo_word: shout_word
    shout_word = echo_word + '!!!'
    # Return shout_word
    return shout_word
# Call shout_echo
print(shout_echo("particle", echo=5))

#   ##########   print(shout_echo("particle", echo=-1))   ###################



# Twitter data
tweets_df = pd.read_csv('tweets.csv')
print(tweets_df.info()) 



############################################
# Filter() and lambda functions in a dataframe
############################################
# In the filter() call, pass a lambda function and the sequence of tweets as strings, tweets_df['text']. 
# The lambda function should check if the first 2 characters in a tweet x are 'RT'. 
# Assign the resulting filter object to result. To get the first 2 characters in a tweet x, use x[0:2]. 
# To check equality, use a Boolean filter with ==.
# Convert result to a list and print out the list.

# Select retweets from the Twitter DataFrame: result
result = filter(lambda x: x[0:2] == 'RT', tweets_df['text'])
# Create list from filter object result: res_list
res_list = list(result)
# Print all retweets in res_list
for tweet in res_list:
    print(tweet)





############################################
# Try and Except function in a data frame
############################################
# Add a try block so that when the function is called with the correct arguments, 
# it processes the DataFrame and returns a dictionary of results.
# Add an except block so that when the function is called incorrectly, it displays the following error message: 
# 'The DataFrame does not have a ' + col_name + ' column.'.

# Define count_entries()
def count_entries(df, col_name='lang'):
    """Return a dictionary with counts of
    occurrences as value for each key."""
    # Initialize an empty dictionary: cols_count
    cols_count = {}
    # Add try block
    try: 
        # Extract column from DataFrame: col
        col = df[col_name]        
        # Iterate over the column in DataFrame
        for entry in col:    
            # If entry is in cols_count, add 1
            if entry in cols_count.keys():
                cols_count[entry] += 1
            # Else add the entry to cols_count, set the value to 1
            else:
                cols_count[entry] = 1    
        # Return the cols_count dictionary
        return cols_count
    # Add except block
    except:
        print('The DataFrame does not have a ' + col_name + ' column.')
# Call count_entries(): result1
result1 = count_entries(tweets_df, 'lang')
# Print result1
print(result1)





############################################
# Raise a value error in a data frame
############################################
# If col_name is not a column in the DataFrame df, raise a ValueError 'The DataFrame does not have a ' + col_name + ' column.'.
# Call your new function count_entries() to analyze the 'lang' column of tweets_df. Store the result in result1.

# Define count_entries()
def count_entries(df, col_name='lang'):
    """Return a dictionary with counts of
    occurrences as value for each key."""    
    # Raise a ValueError if col_name is NOT in DataFrame
    if col_name not in df.columns:
        raise ValueError('The DataFrame does not have a ' + col_name + ' column.')
    # Initialize an empty dictionary: cols_count
    cols_count = {}    
    # Extract column from DataFrame: col
    col = df[col_name]    
    # Iterate over the column in DataFrame
    for entry in col:
        # If entry is in cols_count, add 1
        if entry in cols_count.keys():
            cols_count[entry] += 1
            # Else add the entry to cols_count, set the value to 1
        else:
            cols_count[entry] = 1        
        # Return the cols_count dictionary
    return cols_count
# Call count_entries(): result1
result1 = count_entries(tweets_df, 'lang')
# Print result1
print(result1)


















