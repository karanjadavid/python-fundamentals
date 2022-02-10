#####################################################################
# FUNDAMENTALS OF PYTHON 6 - Data Field
#####################################################################

# import libraries
import pandas as pd


##########################################
# DEFAULT AND FLEXIBLE ARGS
##########################################


############################
# DEFAULT ARGS
############################

# writing functions with default arg.
# to define a function with a default arg value, in the funmction header we follow the parameter
# of interest with an equals sign and the default argument value.



# ADD A DEFAULT ARGUMENT
def power(number, pow =1):
    '''Raise number to the power of pow.'''
    new_value = number ** pow
    return new_value
# we can call the function with two arguments. However if you call with only one,
# the function call will use the default set for the second parameter
print(power(4,2))
print(power(4))



############################
# FUNCTIONS WITH ONE DEFAULT ARG
############################

# Define shout_echo
def shout_echo(word1, echo = 1):
    """Concatenate echo copies of word1 and three
     exclamation marks at the end of the string."""
    # Concatenate echo copies of word1 using *: echo_word
    echo_word = word1 * echo
    # Concatenate '!!!' to echo_word: shout_word
    shout_word = echo_word + '!!!'
    # Return shout_word
    return shout_word
# Call shout_echo() with "Hey": no_echo
no_echo = shout_echo("Hey")
# Call shout_echo() with "Hey" and echo=5: with_echo
with_echo = shout_echo("Hey", echo = 5)
# Print no_echo and with_echo
print(no_echo)
print(with_echo)





############################
# FUNCTIONS WITH MULTIPLE DEFAULT ARGS
############################
# Define shout_echo
def shout_echo(word1, echo = 1, intense = False):
    """Concatenate echo copies of word1 and three
    exclamation marks at the end of the string."""
    # Concatenate echo copies of word1 using *: echo_word
    echo_word = word1 * echo
    # Make echo_word uppercase if intense is True
    if intense is True:
        # Make uppercase and concatenate '!!!': echo_word_new
        echo_word_new = echo_word.upper() + '!!!'
    else:
        # Concatenate '!!!' to echo_word: echo_word_new
        echo_word_new = echo_word + '!!!'
    # Return echo_word_new
    return echo_word_new
# Call shout_echo() with "Hey", echo=5 and intense=True: with_big_echo
with_big_echo = shout_echo("Hey", echo = 5, intense = True)
# Call shout_echo() with "Hey" and intense=True: big_no_echo
big_no_echo = shout_echo("Hey", intense = True)
# Print values
print(with_big_echo)
print(big_no_echo)








############################
# FLEXIBLE ARGUMENTS *args(1)
############################
 
# lets assume you write a function but aren't sure how many arguments user will want to pass
# eg a function that takes floats or ints and adds them all up irrespective of how many they are
# *args - this then turns all the arguments passed to a function call into a tuple called args in the function body
# then in the function body to write our desired function, we initialize our sum_all to zero, loop over the tuple args,
# and add each element of it successively to sum_all abd then return it.
def add_all(*args):
    '''Sum all values in *args together '''
    # initialize sum
    sum_all = 0
    # accumulate the sum
    for num in args:
        sum_all += num
    return sum_all

# we can call our function add_all with any number of arguments to add them all up
print(add_all(1))
print(add_all(1,2,3))
print(add_all(100, 150, 150))


# *args help in cases where you have more arguments 
# args allow the function to take variable arguments. as many as you like
def normal(one, two):
    print(one)
    print(two)
print(normal('argument1', 'argument2'))
print()





# *args is given to the function as a list
# make a list
my_list = ['Honda', 'BMW', 'Toyota', 'Ford', 'Chevy']
def arg_one(*args):
    for stuff in args:
        print(stuff)
# call the function. 
# when calling a function name, use an astrisk
print(arg_one(*my_list))
print()

# you can also call the function by typing in elements of a list. DO NOT  use asterisks in this case
print(arg_one('Honda', 'BMW', 'Toyota', 'Ford', 'Chevy'))
print()





# Complete the function header with the function name gibberish. It accepts a single flexible argument *args.
# Initialize a variable hodgepodge to an empty string.
# Return the variable hodgepodge at the end of the function body.
# Call gibberish() with the single string, "luke". Assign the result to one_word.
# Hit the Submit button to call gibberish() with multiple arguments and to print the value to the Shell.

# Define gibberish
def gibberish(*args):
    """Concatenate strings in *args together."""
    # Initialize an empty string: hodgepodge
    hodgepodge = ''
    # Concatenate the strings in args
    for word in args:
        hodgepodge += word
    # Return hodgepodge
    return hodgepodge
# Call gibberish() with one string: one_word
one_word = gibberish("luke")
# Call gibberish() with five strings: many_words
many_words = gibberish("luke", "leia", "han", "obi", "darth")
# Print one_word and many_words
print(one_word)
print(many_words)






def arg_three(one, two, *args):
    print(one)
    print(two)
    for stuff in args: 
        print(stuff)
my_list = ['dog', 'cow', 'cat', 'sheep', 'horse']
print(arg_three('domestic', 'wild', *my_list)) 
print()





# Define gibberish
def gibberish(*args):
    """Concatenate strings in *args together."""
    # Initialize an empty string: hodgepodge
    hodgepodge = ""
    # Concatenate the strings in args
    for word in args:
        hodgepodge += word
    # Return hodgepodge
    return hodgepodge
# Call gibberish() with one string: one_word
one_word = gibberish("luke")
# Call gibberish() with five strings: many_words
many_words = gibberish("luke", "leia", "han", "obi", "darth")
# Print one_word and many_words
print(one_word)
print(many_words)






############################
# FLEXIBLE ARGUMENTS **kwargs
############################
# we use the parameter kwargs preceeded by a double star. This turns the identifier-keyword pairs 
# into a dictionary within the function body. 
# Then, in the function body, we print all the key-value pairs stored in the dictionary kwargs. 
# Note that it is not the names args and kwargs that are important when using flexible arguments but rather 
# they're preceeded by a single and double star respectively.





# it requires key word arguments ie, a dictionary

def kwarg_one(**kwargs):
    for key, value in kwargs.items():
        print(key)
        print(value)
# make a dictionary
d_example = {'key1':'value1', 'key2':'value2', 'key3':'value3'}
# call the function
print(kwarg_one(**d_example))
print()





# another  method of typing in keys and values of the dictionary
def kwarg_two(**kwargs):
    for key, value in kwargs.items():
        print(key)
        print(value)
# make a dictionary
d_example = {'key1':'value1e', 'key2':'value2e', 'key3':'value3e'}
# call the function
print(kwarg_one(key1 = "value1e", key2 ="value2e", key3 = "value3e"))
print()





# Define report_status
def report_status(**kwargs):
    """Print out the status of a movie character."""
    print("\nBEGIN: REPORT\n")
    # Iterate over the key-value pairs of kwargs
    for key, value in kwargs.items():
        # Print out the keys and values, separated by a colon ':'
        print(key + ": " + value)
    print("\nEND REPORT")
# First call to report_status()
print(report_status(name = "luke", affiliation = "jedi", status = "missing"))
# Second call to report_status()
print(report_status(name="anakin", affiliation="sith lord", status="deceased"))







# Twitter data
tweets_df = pd.read_csv('tweets.csv')
print(tweets_df.head())




# Complete the function header by supplying the parameter for a DataFrame df and 
# the parameter col_name with a default value of 'lang' for the DataFrame column name.
# Call count_entries() by passing the tweets_df DataFrame and the column name 'lang'. Assign the result to result1. 
# Note that since 'lang' is the default value of the col_name parameter, you don't have to specify it here.
# Call count_entries() by passing the tweets_df DataFrame and the column name 'source'. Assign the result to result2


# Define count_entries()
def count_entries(df, col_name='lang'):
    """Return a dictionary with counts of
    occurrences as value for each key."""
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
result1 = count_entries(tweets_df, col_name='lang')
# Call count_entries(): result2
result2 = count_entries(tweets_df, col_name='source')
# Print result1 and result2
print(result1)
print(result2)






# Complete the function header by supplying the parameter for the DataFrame df and the flexible argument *args.
# Complete the for loop within the function definition so that the loop occurs over the tuple args.
# Call count_entries() by passing the tweets_df DataFrame and the column name 'lang'. Assign the result to result1.
# Call count_entries() by passing the tweets_df DataFrame and the column names 'lang' and 'source'. Assign the result to result2.


# Define count_entries()
def count_entries(df, *args):
    """Return a dictionary with counts of
    occurrences as value for each key."""    
    #Initialize an empty dictionary: cols_count
    cols_count = {}    
    # Iterate over column names in args
    for col_name in args:    
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
# Call count_entries(): result2
result2 = count_entries(tweets_df, 'lang', 'source')
# Print result1 and result2
print(result1)
print(result2)

