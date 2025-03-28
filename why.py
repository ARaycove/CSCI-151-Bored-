import math
import sys
import stddraw
import stdio
import numpy as np
import stdrandom
import random

def factorial(n):
    if n == 1: 
        print(1)
        return 1
    result = n * factorial(n-1)
    print(n, result)
    return result

def harmonic(n):
    if n <= 1: return n # the base case
    result = harmonic(n-1) + 1.0/n
    print(result)
    return result

def gcd(p, q):
    if q == 0: return p
    return gcd(q, p % q)

def recursive_graphics(n, size, x, y):
    if n==0: return
    x0 = x - size/2.0
    x1 = x + size/2.0
    y0 = y - size/2.0
    y1 = y + size/2.0
    stddraw.line(x0, y, x1, y)
    stddraw.line(x0, y0, x0, y1)
    stddraw.line(x1, y0, x1, y1)
    stddraw.show(10)
    recursive_graphics(n-1, size/2.0, x0, y1)
    recursive_graphics(n-1, size/2.0, x1, y1)
    recursive_graphics(n-1, size/2.0, x0, y0)
    recursive_graphics(n-1, size/2.0, x1, y0)
    
# size = 3
# n = 5
# stddraw.setXscale(-2*size,2*size)
# stddraw.setYscale(-2*size,2*size)
# stddraw.setPenRadius(0.0)
# recursive_graphics(n, size, 0, 0)
# stddraw.show()

def calc_new_pos(x, y):
    old_point = (x, y)

def draw_triangle():
    t = math.sqrt(3.0)/2.0
    stddraw.line(0.0, 0.0, 1.0, 0.0)
    stddraw.line(1.0, 0.0, 0.5, t)
    stddraw.line(0.0, 0.0, 0.5, t)
    stddraw.point(0.5, t/3.0)
    stddraw.show()

def draw_yellow_rectangle():
    stddraw.setPenColor(stddraw.YELLOW)
    stddraw.filledRectangle(0.25, 0.25, .5, .5)
    stddraw.show()

def checkerboard(n):
    red = True
    black = False
    side_length = 1/n
    starting_point = [side_length/2, side_length/2]
    for i in range(n):
        if red == True:
            black = True
            red = False
            stddraw.setPenColor(stddraw.RED)
        elif black == True:
            black = False
            red = True
            stddraw.setPenColor(stddraw.BLACK)
        stddraw.filledSquare(starting_point[0], starting_point[1], side_length/2)
        for i in range(n):
            starting_point[1] += side_length
            if red == True:
                black = True
                red = False
                stddraw.setPenColor(stddraw.RED)
            elif black == True:
                black = False
                red = True
                stddraw.setPenColor(stddraw.BLACK)
            stddraw.filledSquare(starting_point[0], starting_point[1], side_length/2)
        starting_point[0] += side_length
        starting_point[1] = side_length/2
    stddraw.show()
    # for y in range(n):
        
    #     for x in range(n):
    #         starting_point[0] += side_length
            
    #         stddraw.show(100)
    #     starting_point[0] = 0
    #     starting_point[1] += side_length
        

def banner():

    s = sys.argv[1]
    i = 0
    while True:
        stddraw.clear()
        stddraw.text((i%1), 0.5, s)
        stddraw.show(60.0)
        i += 0.01

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
    G = 9.8 # Gravity Constant
    t = 0
    x_not = initial_height/2
    y_not = initial_height
    V_x = velocity * math.cos(math.radians(theta))
    V_y = velocity * math.sin(math.radians(theta))

    # Need to set x and y scale
    # Draw the platform
    

    # Store the current scale in two variables
    # Allow for dynamic scaling of window

    # The given equation is a parametric equation where the input is t and the output is the x,y coordinate at time t
    
    y = initial_height
    total_flight_time = (
        (
            V_y + math.sqrt(
                math.pow(V_y, 2) + 2*G*initial_height
            )
        ) / G
    )
    range_of_projectile = (
        (V_x * (V_y + math.sqrt(math.pow(V_y, 2)+ 2*G*initial_height))) / G
        )
    t = 0

    h_max = (math.pow(velocity, 2)*math.pow(math.sin(math.radians(theta)), 2))/(2*G)

    stddraw.setXscale(0, range_of_projectile+x_not+20)
    stddraw.setYscale(0, (h_max+y_not))
    stddraw.filledRectangle(0,0,x_not,initial_height)
    color = 1
    radius = 1
    trigger = False
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

def race_race():
    import stddraw
    import random
    stddraw.setXscale(0.0, 1.0)
    stddraw.setYscale(0.0, 1.0)

    #Coordinates for car 1 and 2 respectively
    x1 = 0.0
    y1 = 0.35
    x2 = 0.0
    y2 = 0.75
    rad = 0.1
    while (x1 <= 1-rad) and (x2 <= 1-rad):
        x1 += random.uniform(0, 0.01)
        x2 += random.uniform(0, 0.01)
        stddraw.clear()

        stddraw.setPenColor(stddraw.YELLOW)
        stddraw.filledCircle((x1), 0.35, rad)
        stddraw.setPenColor(stddraw.ORANGE)
        stddraw.filledCircle((x1), 0.35, random.uniform(0, rad))

        stddraw.setPenColor(stddraw.ORANGE)
        stddraw.filledCircle((x2), 0.75, rad)
        stddraw.setPenColor(stddraw.BLUE)
        stddraw.filledCircle((x2), 0.75, random.uniform(0, rad))
        stddraw.show(15)

    stddraw.setPenColor(stddraw.RED)
    if x1 > x2:
        stddraw.text(0.5, 0.5, f"Bottom Wins!")
    else:
        stddraw.text(0.5, 0.5, f"Top Wins!")

def rose(n = 2):
    stddraw.setXscale(-1, 1)
    stddraw.setYscale(-1, 1)
    theta = 0
    while theta <= (math.pi * 2)*3000:
        radius = math.sin(n * theta)
        x = radius * math.cos(theta)
        y = radius * math.sin(theta)
        stddraw.point(x, y)
        stddraw.show(0)
        theta += 0.005
    stddraw.show(5000)


def this_other_o1():
    dragon = stdio.readString()
    nogard = stdio.readString()
    stdio.write(dragon + "L" + nogard)
    stdio.write(" ")
    stdio.write(dragon + "R" + nogard)
    stdio.writeln()
# WE wekj;jlak ;lidsua;flkja;sldkjf;lkj;saldkjfpo3ijaflksdj ;lkwje are typing wrealll yrfast; lkajd;sofij;ns;lKdjf;oaiewjf;lkzxjc;vlkjsd;liaufpoaismd;lakdfjaspdiolnmfm;klxzkcjiuujfdfkkdjjxo;iicjk.kmjslkaedujfml;kcmz
def pink_green_spiral():
    stddraw.setCanvasSize(720, 480)
    stddraw.setXscale(-1, 1)
    stddraw.setYscale(-1, 1)
    theta = 0
    y_values = np.zeros(5, dtype=float)
    y_shift = 0.05
    green   = True
    pink    = False
    while theta <= (50 * math.pi):
        radius = theta/100
        x = radius * math.cos(theta)
        y = radius * math.sin(theta)
        for pos, y_value in enumerate(y_values):
            y_values[pos] = y + y_shift*pos
        theta += 0.005
        if green == True:
            stddraw.setPenColor(stddraw.GREEN)
            green   = False
            pink    = True
        elif pink == True:
            stddraw.setPenColor(stddraw.PINK)
            green   = True
            pink    = False
        for y_value in y_values:
            stddraw.point(x, y_value)
        stddraw.show(0)


def max3(x, y, z):
    nums = [x, y, z]
    max_num = x
    previous = None
    for i in nums:
        if previous == None:
            previous = i
        if i >= previous:
            max_num = i
        previous = i
    return max_num

def odd_bools(n, n_2, n_3):
    '''
    Are an odd number of arguments == True
    '''
    trues = 0
    falses = 0
    args = [n, n_2, n_3]
    for arg in args:
        if arg == True:
            trues += 1
    if trues == 1 or trues == 3:
        return True
    else:
        return False

from color import Color
from picture import Picture

def fade_effect():
    pass

def gaussian_random_drawing():
    trials = int(sys.argv[1])
    stddraw.setXscale(-10, 10)
    stddraw.setYscale(-10, 10)
    last_point = [0, 0]
    for i in range(trials):
        x = stdrandom.gaussian(0.5, 2)
        y = stdrandom.gaussian(0.5, 2)
        stddraw.circle(x, y, stdrandom.gaussian(0,1))
        last_point = [x, y]
        stddraw.show(10)

def sum_of_two_rolls():
    return (random.randint(1, 6) + random.randint(1, 6))

def sum_of_n(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total

def n_powers(n):
    data = []
    for i in range(1, n+1):
        data.append(2**i)
    return data

from objects.Turtle import Turtle as TTL

def koch(n, step, turtle: TTL):
    stddraw.show(0)
    if n==0:
        turtle.go_forward(step)
        return
    koch(n-1, step, turtle)
    turtle.turn_left(60.0)
    koch(n-1, step, turtle)
    turtle.turn_left(-120.0)
    koch(n-1, step, turtle)
    turtle.turn_left(60.0)
    koch(n-1, step, turtle)


def recursive_countdown(n):
    if n == 0: 
        stdio.writeln("Go!")
        return "Go!"
    stdio.writeln(n)
    return recursive_countdown(n-1)

def recursive_length(string_list: list[str], output_layer = None):
    if output_layer == None:
        output_layer = [].copy()
    string = string_list[0]
    output_layer.append(len(string))
    string_list.remove(string)
    if len(string_list) == 0: return stdio.writeln(output_layer)
    return recursive_length(string_list, output_layer)

def fibbing(n, x = None):
    '''
    Do NOT pass anything to x
    returns the nth fibonocci sequence
    '''
    if x == None: 
        x = [0, 1]
        n = n -2 # on first iteration
        if n <= 0:
            n = 0
    if n == 0: return x
    
    x.append((x[-1]+x[-2]))

    return fibbing(n-1, x)


n = 5
result = fibbing(n)
stdio.writeln(result)
stdio.writeln(f"{n} sequence is {result[-1]}")