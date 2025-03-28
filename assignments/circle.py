import stddraw
import math
import sys
import stdio
import random

###########################
#
# Header
# Circle generator
# By Aaron Raycove
# I did this for fun last month, so that's why it's so quick
#
###########################

# Set the scale to the same as unit circle
stddraw.setXscale(-1, 1)
stddraw.setYscale(-1, 1)

# Collect arguments and convert to appropriate data types
num_points  = int(sys.argv[1])
probability = float(sys.argv[2])
# Define a constant, 0.9 so the circle doesn't touch the edge of the screen
RADIUS = 0.9
# Initialize array of points
points = []
# Calculate our interval
interval = (2*math.pi) / num_points

# Plot our points 
for i in range(num_points):
    theta = interval * i # Python defaults to radians so just keep everything in radians
    x = RADIUS * math.cos(theta)
    y = RADIUS * math.sin(theta)
    point = [x, y]
    points.append(point)
    stddraw.point(x,y)

# Now draw lines based on probability
for focus_point in points:
    for point in points:
        # Check condition against our probability entry
        # Also do not attempt to draw a line from the point itself to itself (for efficiency I think)
        if (focus_point != point) and abs(random.random()) <= probability:
            # If the random value is <= the probability variable then draw the line
            stddraw.line(focus_point[0],focus_point[1],point[0],point[1])

# Display the circle
stddraw.show()

# Rubric says to use stdio module, but module is not neccessary, but here you
stdio.writeln("Thanks for the memories")     