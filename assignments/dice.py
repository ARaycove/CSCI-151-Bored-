##########################################
#
# Header
# Die Roll Simulation of Probability
# Aaron Raycove
# 02/07/2025
#
##########################################
import stdarray
import stdio
import sys
import random 
# Original Code Provided
probabilities = stdarray.create1D(13, 0.0)
for i in range(1, 7):
    for j in range(1, 7):
        probabilities[i+j] += 1.0
for k in range(2, 13):
    probabilities[k] /= 36.0
# i jk, lol
# Set up emperical evidence

# Get number of attempts from command line as an argument
number_of_attempt = int(sys.argv[1])
# Initialize array for results
results = stdarray.create1D(len(probabilities), 0)

# Run the experiment that many times
for i in range(number_of_attempt):
    # Roll the dice
    die_roll_one = random.randint(1, 6)
    die_roll_two = random.randint(1, 6)
    # Get the sum
    sum_of_rolls = die_roll_one + die_roll_two
    # the sum is also the index
    # increment the number of times it summed to that amount
    results[sum_of_rolls] += 1

# Convert the values of results into the average probability, they are currently just the sum of attempts
for i in range(len(results)):
    results[i] /= number_of_attempt


# Format a table with our results
# I understand the unit test would have three charts printed
# Doing it this way makes the comparison much easier at a glance
stdio.write(f"Results                                                        {"exact":10} {"actual":10} {"difference":10}\n")
for i in range(2, len(probabilities)):
    exact = probabilities[i]
    actual = results[i]
    diff = exact - actual
    stdio.write(f"Exact/Actual/Difference Probability the sum of die is {i:2}: {exact:10.3f}|{actual:10.3f}|{diff:10.3f}|\n")


# Considered same when difference is 0.000 is or less for all values
# 10000 gets close all values < 0.00x
# 16000 all values <= 0.006x
# 30000 all values <= 0.005x
# 100,000 all values <= 0.003x
# 200,000 all values <= 0.002x
# 250,000 all values <= 0.001x
# 900,000 all values <= 0.001x #mostly 0.000x at this point
# 1,000,000 all values <= 0.001x # still not there yet
# 1,100,000 all values <= 0.000x