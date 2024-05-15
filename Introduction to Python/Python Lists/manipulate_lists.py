# Replace list elements
# Replacing list elements is pretty easy. Simply subset the list and assign new values to the subset.
# You can select single elements or you can change entire list slices at once.

x = ["a", "b", "c", "d"]
x[1] = "r"
x[2:] = ["s", "t"]
print(x);

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Correct the bathroom area
areas[9]=10.50

# Change "living room" to "chill zone"
areas[4]="chill zone"
print(areas);


# Extend a list
# If you can change elements in a list, you sure want to be able to add elements to it, right? 
# You can use the + operator:

x = ["a", "b", "c", "d"]
y = x + ["e", "f"]
print(y);

# Add poolhouse data to areas, new list is areas_1
areas_1 = areas + ["poolhouse", 24.5]
print(areas_1);

# Add garage data to areas_1, new list is areas_2
areas_2 = areas_1 + ["garage", 15.45]
print(areas_2);

# Delete list elements
# Finally, you can also remove elements from your list. You can do this with the del statement:

# x = ["a", "b", "c", "d"]
# del(x[1])

# Pay attention here: as soon as you remove an element from a list, 
# the indexes of the elements that come after the deleted element all change!

areas_copy = list(areas);
# To copy the list areas, you can use list(areas).
# If you simply use areas_copy = areas, you don't really create a copy.
# Changes made to areas_copy will also be made to areas.
# That's because areas and areas_copy point to the same list.
del(areas_copy[-4:-2]);
print(areas_copy);

# del(areas_3[-4:-2]) removes the elements with index -4 and -3 from the list areas_3.
