# Problem Statement 
# A couple beginning a family decides to keep having children until they have at least one of either sex. Estimate the average number of children they will have via simulation. The number of trials is given as a command-line argument.  Also estimate the most common outcome (record the frequency counts for 2, 3, and 4 children, and also for 5 and above). Assume that the probability p of having a boy or girl is 1/2.

# Sample Output / Unit Tests
# python3 boys and girls.py 1000
# Avg # of Children: <num>
# Trials with 2 children: 490
# Trails with 3 children: 260
# Trails with 4 children: 143
# Trails with 5 or more children: 107
# > python boysandgirls.py 1000
# Avg # children: 3
# Trials with 2 children: 509
# Trials with 3 children: 245
# Trials with 4 children: 119
# Trials with 5 or more children: 127
###########################################
#
# Simulation of gender probability
# By Aaron Raycove
# 02/06/2025
#
###########################################
# These are import statements!
import sys
import stdio
import stdarray
import random

number_of_attempts = int(sys.argv[1])
# Data collection
# Initialize Array with five values
results = stdarray.create1D(5, 0)

# Assign a name to each index of the array
# Purely semantic, by doing so I can access each element by a name, or by results[int], assigning a name makes it a bit easier to debug later.
trials_with_two         = results[0]
trials_with_three       = results[1]
trials_with_four        = results[2]
trials_with_five_plus   = results[3]
grand_total_kids        = results[4]

# Simulate the experiment
# How many times to run the experiment
for i in range(number_of_attempts):
    # On each iteration (trial) reset the variables to their default
    has_male    = False
    has_female  = False
    total_kids  = 0
    # Conduct the trial
    while not (has_male and has_female):
        # 50% chance of having either boy or girl
        chance = random.randint(1, 2)
        # Increment how many kids
        total_kids += 1
        # Semantically label 1 with boy and 2 with girl, set boolean to true if condition is met
        if chance == 1:
            has_male = True
        elif chance == 2:
            has_female = True

        # Check if both genders are present
        if has_male and has_female:
            # If they are, increment the total amount of kids across all trials, and increment the appropriate statistic based on the total amount of kids it took before this condition was true
            grand_total_kids += total_kids
            if total_kids == 2:
                trials_with_two += 1
            elif total_kids == 3:
                trials_with_three += 1
            elif total_kids == 4:
                trials_with_four += 1
            elif total_kids >= 5:
                trials_with_five_plus += 1
            break # Break statement breaks only out of the while loop jumping to the next iteration of the for loop

# Sum and Print Results
# average number of kids is a float, in order to match the test case we will round this to the nearest whole number.
avg_num_of_kids = round(grand_total_kids / number_of_attempts)
stdio.write(f"Avg # of Children:              {avg_num_of_kids}\n")
stdio.write(f"Trials with 2 children:         {trials_with_two}\n")
stdio.write(f"Trials with 3 children:         {trials_with_three}\n")
stdio.write(f"Trials with 4 children:         {trials_with_four}\n")
stdio.write(f"Trials with 5 or more children: {trials_with_five_plus}\n")