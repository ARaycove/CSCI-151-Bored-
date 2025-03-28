import sys
import random
import stdio
import stdarray

n = int(sys.argv[1])
values = stdarray.create1D(n, 0)
for i in range(n):
    values[i] = random.randint(1, 100)

values = [i for i in values if (i <= 60)]
for i in values:
    stdio.writeln(i)

