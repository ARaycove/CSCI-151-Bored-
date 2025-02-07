import stdio
import stdarray
import sys
import random

num = int(sys.argv[1])
a = stdarray.create1D(num, "Johnny")
for i in range(num):
    a[i] = random.randint(1, 2)

heads = a.count(1)
tails = a.count(2)

stdio.write(f"Total Flips {len(a)}\nTotal Heads {heads}\nTotal Tails {tails}\n")