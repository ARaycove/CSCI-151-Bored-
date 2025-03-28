# Then compose a program randomintseq.py that takes two command-line arguments m and n and writes n random integers between 0 and m-1.

##############################################
#
# Header 
# Aaron Raycove
# 02/14/2025
#
##############################################
import stdio
import sys
import random

# Read and convert
m = int(sys.argv[1])
n = int(sys.argv[2])

# Write n ints to standard output
for i in range(n):
    # Use f string for formatting, exclusion of space seems to break it
    stdio.write(f"{random.randint(0, (m-1))} ")