import stddraw
import sys
import math

def ball_throw():
    def rainbow(n):
        if n == 1:
            return stddraw.RED
        elif n == 2:
            return stddraw.ORANGE
        elif n == 3:
            return stddraw.YELLOW
        elif n == 4:
            return stddraw.GREEN
        elif n == 5:
            return stddraw.BLUE
        elif n == 6:
            return stddraw.MAGENTA
    initial_height  = float(sys.argv[1])
    velocity        = float(sys.argv[2])
    theta           = float(sys.argv[3])
    # Calculate initial variables and constants
    G = 9.8 # Gravity Constant
    t = 0
    x_not = initial_height/2 
    y_not = initial_height
    V_x = velocity * math.cos(math.radians(theta))
    V_y = velocity * math.sin(math.radians(theta))
    y = initial_height # since y is our loop variable, we will initialize it now to y_not


    # We are going to dynamically set the scale of the window based on user input
    # First we need to know the range of the projectile
    range_of_projectile = (
        (V_x * (V_y + math.sqrt(math.pow(V_y, 2)+ 2*G*initial_height))) / G
        )
    # Now we need to know the maximum height of our projectile
    h_max = (math.pow(velocity, 2)*math.pow(math.sin(math.radians(theta)), 2))/(2*G)
    # Set the x scale to equal our range + a little extra for the viewport
    stddraw.setXscale(0, range_of_projectile+x_not+20)
    # Same with the y scale
    stddraw.setYscale(0, (h_max+y_not))
    # Draw the firing platform
    stddraw.filledRectangle(0,0,x_not,initial_height)

    # A few loop variables to initialize
    t       = 0
    color   = 1
    radius  = 1
    trigger = False
    # ThIs Is A WhIlE lOoP. . .
    while y >= 0:
        x = (velocity*math.cos(math.radians(theta)))*t + x_not
        y = ((-1/2)*G*(t**2))+(velocity*math.sin(math.radians(theta)))*t + y_not
        t += 0.009
        if not trigger:
            stddraw.point(x, y)
            stddraw.setPenColor(rainbow(color))
            color += 1
            if color > 6:
                color = 1
        else:
            stddraw.filledCircle(x, y, radius)
            radius += 0.02
        if (h_max+y_not) <= y+0.0001:
            stddraw.setPenColor(stddraw.RED)
            trigger = True
            stddraw.text(
                (range_of_projectile+x_not+20)/2,
                (h_max+y_not)/2,
                "BOOM"
            )
        stddraw.show(10)
    stddraw.setPenColor(stddraw.YELLOW)
    stddraw.filledCircle(x, y, radius*3)
    stddraw.setPenColor(stddraw.ORANGE)
    stddraw.filledCircle(x, y, radius*2)
    stddraw.setPenColor(stddraw.RED)
    stddraw.filledCircle(x, y, radius)

ball_throw()
# Keep window open for five seconds before closing
stddraw.show(5000)