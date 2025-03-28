# accepts int n from CLI, reads n floats from stdi and writes their mean(average) and standard deviation(square root of the sum of the squares of thier differences from the average, divided by n) to stdo

import stdio
import sys
import stdarray
import math
n = int(sys.argv[1])
values = stdarray.create1D(n, 0)
for i in range(n):
    values[i] = stdio.readFloat()
mean_of_values = sum(values)/len(values)
stddv = math.sqrt(sum(
    [(i-mean_of_values) for i in values])/(float(n-1))
    )

stdio.writeln(mean_of_values)
stdio.writeln(stddv)
