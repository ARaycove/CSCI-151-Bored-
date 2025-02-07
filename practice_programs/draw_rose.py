import stddraw
import stdio
import sys
import math

stddraw.setXscale(-10, 10)
stddraw.setYscale(-10, 10)

d_t = 0.01
n = int(sys.argv[1])

for theta in range(10000):
    RADIUS = 9* math.sin(n*(theta*d_t))
    x = RADIUS * math.cos(theta*d_t)
    y = RADIUS * math.sin(theta*d_t)


    stddraw.point(x, y)

stddraw.show()