# Compose a program that reads in a sequence of integers and writes both the integer that appears in a longest consecutive run and the length of the run. 

# Unit Test
#> python longestrun.py 
# 1 2 2 1 5 1 1 7 7 7 7 1 1
# Longest run:  4 consecutive 7s  

# > python longestrun.py 
# 6 6 6 2 4 4 4 1 1 2 5 8 8 8 8 8 8
# Longest run:  6 consecutive 8s  

###################################################
#
# Header
# Aaron Raycove
# 02/14/2025
#
###################################################
import stdio
# Initialize dictionary and other runtime variables
results = {}
previous_value = ""
current_run = 1

# While stuff is in there!
while not stdio.isEmpty():
    value = stdio.readInt()
    # If value is the same as the previous value then we are in a consecutive run
    if value == previous_value:
        # current run defaults to a run of 1
        current_run += 1
        # Get value of current longest run for given integer
        old_run = results.get(str(value))
        # old_run is a .get method and could return none,
        if old_run == None:
            results[str(value)] = current_run
        # If the old run is less than the current run, update our values
        elif old_run < current_run:
            results[str(value)] = current_run
    # If the value is not equal to our previous value the current run is broken, reset it to one
    elif value != previous_value:
        current_run = 1
    # On each iteration update the previous value
    previous_value = value

# Fetch the key with highest run
maximum_value = max(results, key=results.get)
# Write the results to the command line
stdio.writeln(f"Longest run: {results.get(maximum_value)} consecutive {maximum_value}s")

