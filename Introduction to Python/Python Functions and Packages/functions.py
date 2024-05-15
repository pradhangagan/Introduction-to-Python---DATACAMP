# Functions
# Piece of reusable code
# Solves particular task
# Call function instead of writing code yourself

#  Python offers a bunch of built-in functions to make your life as a data scientist easier. 
# You already know two such functions: print() and type().
# You've also used the functions str(), int(), bool() and float() to switch between data types. 
# These are built-in functions as well.

# The general recipe for calling functions and saving the result to a variable is thus:

# output = function_name(input)

# Create variables var1 and var2
var1 = [1, 2, 3, 4]
var2 = True


# Print out type of var1
print(type(var1));

# Print out length of var1
print(len(var1));

# Convert var2 to an integer: out2
out2 = int(var2);
print(out2);

# Help!
# Maybe you already know the name of a Python function, but you still have to figure out how to use it.
# Ironically, you have to ask for information about a function with another function: help(). 
# To get help on the max() function, for example, you can use:
help(max);


# Have a look at the documentation of sorted() by typing help(sorted) in the IPython Shell.

# You'll see that sorted() takes three arguments: iterable, key, and reverse.

# key=None means that if you don't specify the key argument, it will be None.
# reverse=False means that if you don't specify the reverse argument, it will be False, by default.

# In this exercise, you'll only have to specify iterable and reverse, not key.
# The first input you pass to sorted() will be matched to the iterable argument, but what about the second input? 
# To tell Python you want to specify reverse without changing anything about key, you can use = to assign it a new value:

# sorted(____, reverse=____)


  # Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full
full = first + second


# Sort full in descending order: full_sorted
full_sorted = sorted(full,reverse = True)

# Print out full_sorted
print(full_sorted);