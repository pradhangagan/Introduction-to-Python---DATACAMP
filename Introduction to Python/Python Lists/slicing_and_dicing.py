# Selecting single values from a list is just one part of the story. 
# It's also possible to slice your list, which means selecting multiple elements from your list. Use the following syntax:

# my_list[start:end]
# The start index will be included, while the end index is not.

# The code sample below shows an example. A list with "b" and "c", corresponding to indexes 1 and 2, are selected from a list x:

# x = ["a", "b", "c", "d"]
# x[1:3]
# The elements with index 1 and 2 are included, while the element with index 3 is not.

# However, it's also possible not to specify these indexes. 
# If you don't specify the begin index, Python figures out that you want to start your slice at the beginning of your list. 
# If you don't specify the end index, the slice will go all the way to the last element of your list. 
# x = ["a", "b", "c", "d"]
# x[:2]
# x[2:]
# x[:]

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Use slicing to create downstairs
downstairs = areas[0:6]
# Alternative slicing to create downstairs
# downstairs = areas[:6]


# Use slicing to create upstairs
upstairs = areas[6:]  
# Alternative slicing to create upstairs
# upstairs = areas[-4:] 

# Print out downstairs and upstairs
print(downstairs);
print(upstairs);