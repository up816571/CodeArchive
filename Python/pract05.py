#-------------------------------------------------------------------------------
# Practical Worksheet 5: Using functions
# your name Josh Ruffle
# your six-digit student number 816571
#-------------------------------------------------------------------------------

from graphics import *
import math

# For exercises 1 and 2
def areaOfCircle(radius):
    return math.pi * radius ** 2
    
def circumferenceOfCircle(radius):
    return math.pi * (radius * 2)

# For exercise 3
def drawCircle(win, centre, radius, colour):
    circle = Circle(centre, radius)
    circle.setFill(colour)
    circle.setWidth(2)
    #circle.setOutline(colour)
    circle.draw(win)

def drawBrownEyeInCentre():
    window = GraphWin()
    drawCircle(window, Point(window.getWidth() / 2, window.getHeight() / 2), 60, "white")
    drawCircle(window, Point(window.getWidth() / 2, window.getHeight() / 2), 30, "brown")
    drawCircle(window, Point(window.getWidth() / 2, window.getHeight() / 2), 15, "black")
    # Add your code here

# For exercise 5
def drawBrownEye(win, center, radius):
    drawCircle(win, center, radius, "white")
    drawCircle(win, center, radius / 2, "brown")
    drawCircle(win, center, radius / 4, "black")
    
def circleInfo():
    radius = eval(input("Enter a radius: "))
    print("the area is {0:0.3f}".format(areaOfCircle(radius)) ,"and the circumference is {0:0.3f}".format(circumferenceOfCircle(radius)))
    
def drawBlockOfStars(width, height):
    for i in range(height):
        print("*" * width)
        
def drawLetterE():
    drawBlockOfStars(8, 2)
    drawBlockOfStars(2, 2)
    drawBlockOfStars(4, 2)
    drawBlockOfStars(2, 2)
    drawBlockOfStars(8, 2)
    
def drawPairOfBrownEyes():
    win = GraphWin()
    drawBrownEye(win, Point(70,100), 30)
    drawBrownEye(win, Point(130,100), 30)
    
def distanceBetweenPoints(p1, p2):
    x1 = p1.getX()
    y1 = p1.getY()
    x2 = p2.getX()
    y2 = p2.getY()
    
    return math.sqrt((x2 - x1)**2 + (y2-y1)**2)
    
def drawBlocks(spaces1, block1, spaces2, block2, spacesEnd):
    print(" " * spaces1 + "*" * block1 + " " * spaces2 + "*" * block2 + " " * spacesEnd) 
    
def drawLetterA():
    drawBlocks(1, 8, 1, 0, 0)
    drawBlocks(1, 8, 1, 0, 0)
    drawBlocks(0, 2, 6, 2, 0)
    drawBlocks(0, 2, 6, 2, 0)
    drawBlocks(0, 10, 0, 0, 0)
    drawBlocks(0, 10, 0, 0, 0)
    drawBlocks(0, 2, 6, 2, 0)
    drawBlocks(0, 2, 6, 2, 0)
    drawBlocks(0, 2, 6, 2, 0)
    
def drawFourPairsOfBrownEyes():
    win = GraphWin()
    for i in range(4):
        p1 = win.getMouse()
        p2 = win.getMouse()
        radius = distanceBetweenPoints(p1, p2)
        drawBrownEye(win, p1, radius)
        p3 = p1.getX() + radius*2
        drawBrownEye(win, Point(p3,p1.getY()), radius)
        
def displayTextWithSpaces(string, position, size, win):
    words = ""
    for i in range(len(string)):
        words = words + string[i] + " "
    text = Text(position, words.upper())
    text.setSize(size)
    text.draw(win)
    
def constructVisionChart():
    win = GraphWin("strigs",600, 300)
    for i in range(6):
        enteredString = input("enter a string: ")
        displayTextWithSpaces(enteredString, Point(300, 50 + i * 50), 30 - i * 5, win) 
    
def drawStickFigureFamily():
    win =GraphWin("StickFigure", 800, 800) 
    drawStickFigure(win, Point(100,60), 30)
    drawStickFigure(win, Point(200,100), 20)
    drawStickFigure(win, Point(600,400), 10)
    drawStickFigure(win, Point(200,300), 40)
    
def drawStickFigure(win, position, size):
    xCo = position.getX() 
    yCo = position.getY()
    head = Circle(position, size)
    head.draw(win)
    
    bottomHead = Point(xCo, yCo + size)
    lowerBody = Point(xCo, yCo + size * 3)
    body = Line(bottomHead, lowerBody)
    body.draw(win)
    
    Arm = Line(Point(xCo - size * 1.5, bottomHead.getY() + size / 2), Point(xCo + size * 1.5, bottomHead.getY() + size / 2))
    Arm.draw(win)
    

    Leg1 = Line(lowerBody, Point((xCo + 10) + size / 2, lowerBody.getY() + size * 2))
    Leg1.draw(win)
    Leg2 = Line(lowerBody, Point((xCo - 10) - size / 2, lowerBody.getY() + size * 2))
    Leg2.draw(win)
        
