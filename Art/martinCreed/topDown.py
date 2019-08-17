from turtle import *
import math
hideturtle()
SPD = 10
def pol2cart(pol):
    #rho phi
    x = pol[0] * math.cos(math.radians(pol[1]))
    y = pol[0] * math.sin(math.radians(pol[1]))
    return(x,y)


def addPoint(radius, diff):
    #print("GIven, ", radius, diff)
    len = (radius**2 - (radius-diff)**2)**0.5 * 2
    #print("Length ", len)
    beg = (-len/2, diff)
    #print("beging coor", beg)
    return (beg, len)


def addPoints(radius, thick):
    finalPoints = []
    for i in range(0,radius, thick):
        finalPoints.append(addPoint(radius,i))
    print(finalPoints)
    return finalPoints

def graphPoints(points, thick):
    width(thick)
    for i in points:
        penup()
        speed(0)
        goto(i[0][0], i[0][1])
        speed(SPD)
        pendown()
        forward(i[1])

graphPoints(addPoints(40, 4), 4)
done()



#make a tuple of begining and of length, append that to a list
