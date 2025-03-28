import stddraw
import random
stddraw.setXscale(-1,1)
stddraw.setYscale(-1,1)
stddraw.setPenRadius(0.01)
for i in range(5000):
    x = -1.0 + 2.0*random.random()
    y = -1.0 + 2.0*random.random()
    if x*x + y*y <= 1.0:
        stddraw.point(x, y)

# stddraw.circle(0,0,1)

stddraw.show(0)
stddraw.save("circle.png")
