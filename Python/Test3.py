#josh ruffle

from graphics import *
import math

def drawCircle(win, centre, radius, colour, outColour):
    circle = Circle(centre, radius)
    circle.setFill(colour)
    circle.setOutline(outColour)
    circle.draw(win)

def circles():
    win = GraphWin("circles", 600, 600)
    for i in range(10):
        p1 = win.getMouse()
        if (p1.getY() < 300) and (p1.getX() < 300):
            drawCircle(win, p1, 30, "", "red")
        elif (p1.getY() < 300) and (p1.getX() >= 300):
            drawCircle(win, p1, 30, "red", "black")
        elif (p1.getY() >= 300) and (p1.getX() < 300):
            drawCircle(win, p1, 30, "", "blue")
        else:
            drawCircle(win, p1, 30, "blue", "black")
            
def circles2():
    win = GraphWin("circles", 600, 600)
    for vertical in range(450, 571, 60):
        for horizontal in range(30, 571, 60):
            p1 = win.getMouse()
            centers = Point(horizontal, vertical)
            if (p1.getY() < 300) and (p1.getX() < 300):
                drawCircle(win, centers, 30, "", "red")
            elif (p1.getY() < 300) and (p1.getX() >= 300):
                drawCircle(win, centers, 30, "red", "black")
            elif (p1.getY() >= 300) and (p1.getX() < 300):
                drawCircle(win, centers, 30, "", "blue")
            else:
                drawCircle(win, centers, 30, "blue", "black")