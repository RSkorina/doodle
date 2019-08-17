from turtle import *
import math

RAD = 77
SPD = 0

hideturtle()
width = 1540
height = 820
thick = 3

setup(width,height)
penup()
goto(-770,-410 -144)
pensize(thick)
pendown()


def intrusion(radius, direc = 1):
    #If direc is not 1 then it is -1 and we go backwards
    circle(radius, 90 * direc)
    speed(0)
    right(180)
    speed(SPD)
    circle(radius, -180 * direc)
    speed(0)
    right(180)
    speed(SPD)
    circle(radius, 90 * direc)

def doRow(radius, direc = 1):
    for i in range(0,5):
        intrusion(radius, direc = direc)

def main():
    for i in range(math.floor(height/(thick*2))):

        doRow(RAD)
        speed(0)
        penup()
        left(90)
        forward(thick*2 +1)
        right(90)
        speed(SPD)
        pendown()
        doRow(RAD, direc = -1)
        penup()
        left(90)
        forward(thick*2 +1)
        right(90)
        speed(SPD)
        pendown()

    done()

if __name__ == '__main__':
    main()
