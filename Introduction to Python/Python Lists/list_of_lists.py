# A list can contain any Python type. But a list itself is also a Python type. 
# That means that a list can also contain a list!

print([1 + 2, "a" * 5, 3])
print([[1, 2, 3], [4, 5, 7]])

# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# house information as list of lists
# Instead of creating a flat list containing strings and floats, representing the names 
# and areas of the rooms in your house, you can create a list of lists.

house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
         ["bedroom", bed],
         ["bathroom", bath]]

# Print out house
print(house);

# Print out the type of house
print(type(house));

# You saw before that a Python list can contain practically anything; even other lists! 
# To subset lists of lists, you can use the same technique as before: square brackets. 
# Try out the commands in the following code sample in the IPython Shell:

x = [["a", "b", "c"],
     ["d", "e", "f"],
     ["g", "h", "i"]]
print(x[2][0]);
print(x[2][:2]);
# x[2] results in a list, that you can subset again by adding additional square brackets.
