x = ["a", "b", "c", "d"]
x[1]
x[-3] # same result!



# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Print out second element from areas
print(areas[1])

# Print out last element from areas
print(areas[-1])

# Print out the area of the living room
print(areas[5])


# After you've extracted values from a list, you can use them to perform additional calculations. 
# The strings that result are pasted together using the + operator: bd
x = ["a", "b", "c", "d"]
print(x[1] + x[3])



# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Sum of kitchen and bedroom area: eat_sleep_area
eat_sleep_area = areas[3] + areas[-3];

# Print the variable eat_sleep_area
print(eat_sleep_area);