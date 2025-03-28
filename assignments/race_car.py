import stddraw
import random
def race_race():
    stddraw.setXscale(0.0, 1.0)
    stddraw.setYscale(0.0, 1.0)
    for i in range(10):
        stddraw.setFontSize(12)
        stddraw.text(0.5, 0.5, f"Epilepsy Warning! {10-i}")
        stddraw.show(1000)
        stddraw.clear()

    #Coordinates for car 1 and 2 respectively
    x1 = 0.0
    x2 = 0.0
    rad = 0.1
    while (x1 <= 1-rad) and (x2 <= 1-rad):
        x1 += random.uniform(0, 0.005)
        x2 += random.uniform(0, 0.005)
        stddraw.clear()

        stddraw.setPenColor(stddraw.YELLOW)
        stddraw.filledCircle((x1), 0.35, rad)
        stddraw.setPenColor(stddraw.ORANGE)
        stddraw.filledCircle((x1), 0.35, random.uniform(0, rad))

        stddraw.setPenColor(stddraw.ORANGE)
        stddraw.filledCircle((x2), 0.75, rad)
        stddraw.setPenColor(stddraw.BLUE)
        stddraw.filledCircle((x2), 0.75, random.uniform(0, rad))
        stddraw.show(35)

    stddraw.setPenColor(stddraw.RED)
    if x1 > x2:
        stddraw.text(0.5, 0.5, f"Bottom Wins!")
    else:
        stddraw.text(0.5, 0.5, f"Top Wins!")

race_race()
stddraw.show()