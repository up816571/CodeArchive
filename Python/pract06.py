#-------------------------------------------------------------------------------
# Practical Worksheet 6: if statements and for loops
# Josh Ruffle
# 816571
#-------------------------------------------------------------------------------

from graphics import *
import math
import random

# For exercises 8 & 11
def drawCircle(win, centre, radius, colour):
    circle = Circle(centre, radius)
    circle.setFill(colour)
    circle.setWidth(2)
    circle.draw(win)

# For exercise 8 
def drawColouredEye(win, centre, radius, colour):
    drawCircle(win, centre, radius, "white")
    drawCircle(win, centre, radius/2, colour)
    drawCircle(win, centre, radius/4, "black")

def fastFoodOrderPrice():
    cost = eval(input("enter the orders cost: "))
    if cost < 10:
        cost = cost + 1.5
    print("Total price is £" + str(cost))
    
def whatToDoToday():
    temperature = eval(input("enter the temperature: "))
    if temperature > 25:
        print("swim")
    elif temperature >= 10:
        print("shop")
    else:
        print("film")
    
def displaySquareRoots(start,end):
    for i in range(end + 1):
        if i >= start:
            print("the square root of {0} is {1:0.3f}".format(start, math.sqrt(i)))
    
def calculateGrade(mark):
    if mark > 20:
        print("X")
    elif mark >= 16:
        print("A")
    elif mark >=12:
        print("B")
    elif mark >= 8:
        print("C")
    elif mark > 0:
        print("F")
    else:
        print("X")
        
def peasInAPod():
    peas = eval(input("enter the pea amount: "))
    win = GraphWin("peas",(100 * peas), 100)
    for i in range(peas):
        pea = Circle(Point(50 + (100*i), 50), 50)
        pea.setFill("green")
        pea.draw(win)
        
def ticketPrice(distance, age):
    price = 3 + 0.15*distance
    if (age <= 15) or (age >=60):
        price = price * 0.6 
    return("£{0:0.2f}".format(price))
    
def numberedSquare(n):
    for i in range(n, 0 ,-1):
        for j in range(n):
            print("{0:2}".format(i+j), end=" ")
        print()
        
def eyePicker():
    xCo = eval(input("enter the x co-ordinate of the eye :"))
    yCo = eval(input("enter the y co-ordinate of the eye :"))   
    centre = Point(xCo, yCo)
    radius = eval(input("enter the radius of the eye :")) 
    colour = input("enter a colour (blue, green, grey, brown) :")
    if (colour == "blue") or (colour == "green") or (colour == "grey") or (colour == "brown"):
        win = GraphWin()
        drawColouredEye(win, centre, radius, colour)
    else:
        print("not a valid eye colour")
    
def drawPatchWindow():
    win = GraphWin("patch", 100, 100)
    for i in range(0, 101, 10):
        rectangle = Rectangle(Point(i, 100-i ), Point(i + 10, 90-i))
        rectangle.draw(win)
        rectangle.setFill("red")
        
def drawPatch(win, xCo, yCo, colour):
    for i in range(0, 101, 10):
        rectangle = Rectangle(Point(xCo + i, yCo + 100 - i), Point(xCo + i + 10, yCo+ 90 - i))
        rectangle.draw(win)
        rectangle.setFill(colour)
        
def drawPatchWork():
    win = GraphWin("patch", 300, 200)
    for i in range(2):
        for j in range(3):
            drawPatch(win, j*100, i*100, "blue")

def eyesAllAround():
    win = GraphWin("eyes",500,500)
    for i in range(30):
        p1 = win.getMouse()
        colours = ["blue","grey","green","brown"]
        colour = colours[i % 4]
        drawColouredEye(win, p1, 30, colour)

            
def archeryGame():
    win = GraphWin("Circle")
    centre = Point(100, 100)
    drawCircle(win, centre, 60, "blue")
    drawCircle(win, centre, 40, "red")
    drawCircle(win, centre, 20, "yellow")
    score = 0
    for i in range(5):
        p1 = win.getMouse()
        xMovement = random.randint(-10, 10)
        yMovement = random.randint(-10, 10)
        hit = Point(p1.getX() + xMovement, p1.getY() + yMovement)
        if distanceBetweenPoints(centre, hit) <= 20:
            score = score + 10
        elif distanceBetweenPoints(centre, hit) <= 40:
            score = score + 5
        elif distanceBetweenPoints(centre, hit) <= 60:
            score = score +2
        hitMarker = Circle(hit, 2)
        hitMarker.setFill("black")
        hitMarker.draw(win)
    print(score)
        
def distanceBetweenPoints(p1, p2):
    x1 = p1.getX()
    y1 = p1.getY()
    x2 = p2.getX()
    y2 = p2.getY()
    return math.sqrt((x2 - x1)**2 + (y2-y1)**2)