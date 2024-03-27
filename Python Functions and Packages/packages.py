# Packages
# Directory of Python Scripts
# Each script = module
# Specify functions, methods,types
# Thousands of packages available
# NumPy
# Matplotlib
# scikit-learn

# To use the constant pi, you'll need the math package. A variable r is already coded in the script. 
# Fill in the code to calculate C and A and see how the print() functions create some nice printouts.

# Import the math package
import math

# Definition of radius
r = 0.43

# Calculate C
C = 2*math.pi*r

# Calculate A
A = math.pi*r**2

# Build printout
print("Circumference: " + str(C))
print("Area: " + str(A))

# Selective import
# General imports, like import math, make all functionality from the math package available to you. 
# However, if you decide to only use a specific part of a package, you can always make your import more selective:

# from math import pi

# Perform a selective import from the math package where you only import the radians function.

# Import radians function of math package
from math import radians

# Definition of radius
r = 192500

# Travel distance of Moon over 12 degrees. Store in dist.
phi=radians(12)
dist= r*phi

# Print out dist
print(dist)


# There are several ways to import packages and modules into Python. 
# Depending on the import call, you'll have to use different Python code.

# Suppose you want to use the function inv(), which is in the linalg subpackage of the scipy package.
# You want to be able to use this function as follows:

from scipy.linalg import inv as my_inv
inverse=my_inv([[1,2], [3,4]])
print(inverse)
