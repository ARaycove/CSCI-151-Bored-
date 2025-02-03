# # Problem Statement
# Compose a program that calculates and writes the amount of money you would have if you invested it at a given interest rate compounded continuously, taking the number of years t , the principal P, and the annual interest rate r as commmand-line arguments. The desired value is given by the formula  pert.

# ** You must use the booksite module stdio for standard output
# ** Use Python's built-in function round() to round output to 2 decimal places.  Click here Links to an external site. for a list of Python's built-in functions.  
# ** Use Python's math module for the mathematical constant e.  Click here Links to an external site. to view Python's math module.  

# Unit Tests
# >python compound.py 2 1500 .04
# 1624.93
# >python compound.py 10 1500 .04
# 2237.74

# Resolves the above problem statement
# takes number of years, principle, and interest rate and outputs results of annual vs continous growth
# However if interest rate r is meant to be the annual growth rate, then we need to convert it. But to achieve the unit tests, r must be inputted into the value of k in e^kx. Not sure if this is an error or not.
# Import statements
import stdio
import sys
import math

# Gather inputs
years       = float(sys.argv[1])
principle   = float(sys.argv[2])
interest    = float(sys.argv[3])

# # Calculate result if compounded annually (form ab^x) x = years
# result_annual = principle * math.pow((1+interest), years)
# result_annual = round(result_annual, 2)

# Calculate result if interest rate is k continuous growth rate
result_cont = principle * math.pow(
    math.e, (interest * years)
)
result_cont             = round(result_cont, 2)

# Send output to console
# stdio.write(f"Annual growth:        {result_annual}\n")
stdio.write(f"Continuous growth:    {result_cont}\n")