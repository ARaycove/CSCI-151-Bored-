import stddraw
import math
import sys
import random

stddraw.setXscale(-1, 1)
stddraw.setYscale(-1, 1)

probability = float(sys.argv[1])
RADIUS = 0.9
points = []
interval = (2*math.pi) / 16
for i in range(16):
    theta = interval * i
    x = RADIUS * math.cos(theta)
    y = RADIUS * math.sin(theta)
    point = [x, y]
    points.append(point)
    stddraw.point(x,y)

for focus_point in points:
    for point in points:
        if (focus_point != point) and abs(random.random()) <= probability:
            stddraw.line(focus_point[0],focus_point[1],point[0],point[1])

stddraw.show()


