# Suppose, for example, that you've calculated your savings want to summarize the results in a string.

# To do this, you'll need to explicitly convert the types of your variables. 
# More specifically, you'll need str(), to convert a value into a string. str(savings), for example, will convert the integer savings to a string.

# Similar functions such as int(), float() and bool() will help you convert Python values into any type.

# Definition of savings and total_savings
savings = 100
total_savings = 150

# Fix the printout
print("I started with $" + str(savings) + " and now have $" + str(total_savings) + ". Awesome!")

# Definition of pi_string
pi_string = "3.1415926"

# Convert pi_string into float: pi_float
pi_float = float(pi_string);
print(pi_float);