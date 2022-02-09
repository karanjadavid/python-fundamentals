#####################################################################
# FUNDAMENTALS OF PYTHON 5 - Data Field
#####################################################################

#############################
# SCOPE AND NESTED FUNCTIONS            
#############################

# TYPES OF SCOPES
# 1) GLOBAL SCOPE - defined in the main body of a script. A name that is in the global scope means its defined in main body.
# 2) LOCAL SCOPE - defined inside a function. Once the execution of the function is complete, any name inside the local scope
# ceases to exist. Which means you cannot access those names anymore outside the function definition.
# 3) BUILT IN SCOPE - names in pre defined built in modules eg, print, sum.


# scope in user defined functions. 
# not all objects that you define are usually accessible everywhere in the program
# Scope - tells you which part of a program an object or a name may be accessed
# Names refers to the variables or more generally objects such as functions that are defined in your program. 





#############################
# LOCAL SCOPE                
#############################
# example 1: new_val is under local scope
def square(value):
    '''Returns the square of a number'''
    new_val = value ** 2
    return new_val

sq = (square(3))
print(sq)
# note that you cannot access new_val because it is defined inside the function.
# print(new_val) 
# NameError: name 'new_val' is not defined





# example 2: new_val is under global scope
# what if we define the name globally before defining and calling a function?
new_val = 10 

def square(value):
    '''Returns the square of a number'''
    new_val = value ** 2
    return new_val

sq = (square(3))
print(sq)

print(new_val)
# any time we call the name in the global scope, it will access the name in the global scope.
# any time we call the name in the local scope, it will first look in the local scope.
# if python cannot find the name in the local scope, it will then and only then look in the global scope
# here, we access new_val defined globally within the function square. note the global value accessed is 
# the value at the time the function is called not the value when the function is deefined



#############################
# GLOBAL SCOPE                
#############################

print()
new_val = 10

def square(value):
    '''Returns the square of a number'''
    new_val2 = new_val ** 2
    return new_val2

sq = square(1)
print(sq)
#  note that the global value accessed is the value at the time the function is called, 
# not the value when  the function is defined. Thus, if we reassign new_val and call the function square, 
# we see that the new value of new val is accessed.
new_val = 20 
sq = square(1)
print(sq)






#############################
# global keyword                
#############################
# what if we want to alter the value of a global name within a function call?
# Within the function definition, we use the keyword global followed by the name of the global variable that we wish to access and alter
print()
new_val = 10

def square(value):
    '''Returns the square of a number'''
    global new_val
    new_val = new_val ** 2
    return new_val 
sq = square(1)
print(sq)
# the function call works as one would expect
# now, calling new_val, we see the the global value has been squared by running the function square
print(new_val)





# Create a string: team
team = "teen titans"
# Define change_team()
def change_team():
    """Change the value of the global variable team."""
    # Use team in global scope
    global team
    # Change the value of team in global: team
    team = "justice league"
# Print team
print(team)
# Call change_team()
change_team()
# Print team
print(team)
print()





##########################################################
# NESTED FUNCTIONS
##########################################################
# We have a function inner, defined within another function outer.
# We reference a name x in the inner function. Python serches the local scope of the function inner, and if it doesn't find x, 
# it searches the scope of the function outer which is called an enclosing function because it encloses the inner function
# if python can't find x in the scope of the enclosing function, it then searches the global scope and then the built in scope


# def outer( ... ):
#     '''...'''
#     x = ...
#     def inner(...):
#         '''...'''
#         y = x ** 2
#     return ...



# We use NESTED FUNCTIONS when we want to use a process a number of times within a function. 
# write a function that takes three numbers as parameters and performs the same function on each of them

def mod2plus5(x1, x2, x3):
    '''Returns the remainder plus 5 of three values'''
    new_x1 = x1 % 2 + 5
    new_x2 = x2 % 2 + 5
    new_x3 = x3 % 2 + 5
    return (new_x1, new_x2, new_x3)
print(mod2plus5(13,52,39))
# the following function gives the answer but is not scalable when you want to perform the computation several times.





# in the nested function, we define an inner function within our function definition and call it where necessary
def mod2plus5(x1, x2, x3):
    '''Returnd the remainder plus 5 of three values'''
    def inner(x):
        '''Returns the remainder plus 5 of a value'''
        return x % 2 + 5
    return (inner(x1), inner(x2), inner(x3))

print(mod2plus5(13, 52, 39))





#############################
# nested function 1             
#############################
# In this exercise, inside a function three_shouts(), you will define a nested function inner()
# that concatenates a string object with !!!. three_shouts() then returns a tuple of three elements,
# each a string concatenated with !!! using inner()

# Define three_shouts
def three_shouts(word1, word2, word3):
    """Returns a tuple of strings
    concatenated with '!!!'."""
    # Define inner
    def inner(word):
        """Returns a string concatenated with '!!!'."""
        return word + '!!!'
    # Return a tuple of strings
    return (inner(word1), inner(word2), inner(word3))
# Call three_shouts() and print
print(three_shouts('a', 'b', 'c'))






#############################
# nested function 2             
#############################

# Returning functions
# we define a function raise_vals which contains an inner function called inner
# raise_vals takes an argument n and creates a function inner that returns the nth power of any number

def raise_val(n):
    '''Return the inner function'''
    def inner(x):
        '''Raise x to the power of n'''
        raised = x ** n
        return raised
    return inner
# passing the number 2 to raise_vals creates a function that squares any number 
# passing the number 3 to raise_vals creates a function that cubes any number. 
# when we call the function square, it remembers that n = 2 although the enclosing scope defined by raise_val 
# and to which n=2 is local, has finished execution.

squares = raise_val(2)
cubes = raise_val(3)
print(squares(3), cubes(4))





#############################
# nested function 3             
#############################
# closure - This means that the nested or inner function remembers the state of its enclosing scope when called. 
# Thus, anything defined locally in the enclosing scope is available to the inner function even 
# when the outer function has finished execution.



# Complete the function header of the inner function with the function name inner_echo() and a single parameter word1.
# Complete the function echo() so that it returns inner_echo.
# We have called echo(), passing 2 as an argument, and assigned the resulting function to twice. 
# Your job is to call echo(), passing 3 as an argument. Assign the resulting function to thrice.
# Hit Submit to call twice() and thrice() and print the results.

# Define echo
def echo(n):
    """Return the inner_echo function."""
    # Define inner_echo
    def inner_echo(word1):
        """Concatenate n copies of word1."""
        echo_word = word1 * n
        return echo_word
    # Return inner_echo
    return inner_echo
# Call echo: twice
twice = echo(2)
# Call echo: thrice
thrice = echo(3)
# Call twice() and thrice() then print
print(twice('hello'), thrice('hello'))







#############################
# using non local             
#############################
# in nested functions, we use non local which does a similar job to global
# in this example, we alter the value of n in the inner function; because we use the keyword non local, it also alters the value 
# of n in the enclosing scope

def outer():
    '''Prints the value of n'''
    n = 1
    def inner():
        nonlocal n
        n = 2
        print(n)
 






# Assign to echo_word the string word, concatenated with itself.
# Use the keyword nonlocal to alter the value of echo_word in the enclosing scope.
# Alter echo_word to echo_word concatenated with '!!!'.
# Call the function echo_shout(), passing it a single argument 'hello'.

# Define echo_shout()
def echo_shout(word):
    """Change the value of a nonlocal variable"""    
    # Concatenate word with itself: echo_word
    echo_word = word*2    
    # Print echo_word
    print(echo_word)   
    # Define inner function shout()
    def shout():
        """Alter a variable in the enclosing scope"""        
        # Use echo_word in nonlocal scope
        nonlocal echo_word        
        # Change echo_word to echo_word concatenated with '!!!'
        echo_word = echo_word + '!!!'    
    # Call function shout()
    shout()    
    # Print echo_word
    print(echo_word)
# Call function echo_shout() with argument 'hello'
echo_shout('hello')


























# SCOPES SEARCHED - LEGB rule
# Local 
# Enclosed functions
# Global 
# Built-in 
# assigning names will only create or change local  names, unless they are declared 
# in global or nonlocal statements using the keyword global or keyword nonlocal, respectively.






