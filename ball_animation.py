import stddraw
import math
import random
import sys
stddraw.setXscale(-1, 1)
stddraw.setYscale(-1, 1)

DT = 20.0
RADIUS = 0.05
vx = 0.015
vy = 0.023

balls = []
how_many_balls = int(sys.argv[1])

for i in range(how_many_balls):
    rx = random.uniform(-.9, .9)
    ry = random.uniform(-.9, .9)
    speed_multiplier = random.uniform(1, 2)
    balls.append([rx, ry, vx, vy, speed_multiplier])



# # ball_one
# rx = 0.480
# ry = 0.860
# vx = 0.015
# vy = 0.023
# # ball_two
# rx_2 = 0.12
# ry_2 = 0.12
# vx_2 = 0.015
# vy_2 = 0.023

d_t = 0.01
occ_vec = -1
theta = 0
while True:
    occ_vec = (math.sin(theta))+1
    theta += d_t
    print(occ_vec, theta)
    # # Ball One
    # if abs(rx + vx) + RADIUS > 1.0: vx = -vx
    # if abs(ry + vy) + RADIUS > 1.0: vy = -vy
    # rx = rx + vx * occ_vec
    # ry = ry + vy * occ_vec
    # # Ball Two
    # if abs(rx_2 + vx_2) + RADIUS > 1.0: vx_2 = -vx_2
    # if abs(ry_2 + vy_2) + RADIUS > 1.0: vy_2 = -vy_2
    # rx_2 = rx_2 + vx_2 * occ_vec
    # ry_2 = ry_2 + vy_2 * occ_vec   
    stddraw.clear(stddraw.GRAY)
    for ball in balls:
        if abs(ball[0]+ball[2]) + RADIUS > 1.0: ball[2] = -ball[2]
        if abs(ball[1]+ball[3]) + RADIUS > 1.0: ball[3] = -ball[3]
        ball[0] = ball[0]+ball[2]*ball[4]
        ball[1] = ball[1]+ball[3]*ball[4]
        stddraw.filledCircle(ball[0],ball[1],RADIUS) 


    # stddraw.clear(stddraw.GRAY)
    # stddraw.filledCircle(rx, ry, RADIUS)
    # stddraw.filledCircle(rx_2, ry_2, RADIUS)
    stddraw.show(DT)