from graphics import *

def drawCircle(win, centre, radius, colour):
    circle = Circle(centre, radius)
    circle.setFill(colour)
    circle.draw(win)
    
def clickscreen():
    win = GraphWin()
    for i in range(10):
        p1 = win.getMouse()
        if p1.getY() <= 100:
            drawCircle(win, p1, 20, "black")
        else:
            drawCircle(win, p1, 20, "white")
            
def loopeyThing():
    win = GraphWin()
    for horizontal in range(20, 181, 40):
        for vertical in range(20, 181, 40):
            p1 = win.getMouse()
            centers = Point(horizontal ,vertical)
            if p1.getY() <= 100:
                drawCircle(win, centers, 20, "black")
            else:
                drawCircle(win, centers, 20, "white")