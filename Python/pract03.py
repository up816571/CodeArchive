# Practical Worksheet 3: Graphical Programming
# your name, your number

from graphics import *
import math

def drawStickFigure():
    win = GraphWin("Stick figure")
    head = Circle(Point(100, 60), 20)
    head.draw(win)
    body = Line(Point(100, 80), Point(100, 120))
    body.draw(win)
    Arm = Line(Point(80, 100), Point(120, 100))
    Arm.draw(win)
    Leg1 = Line(Point(100, 120), Point(110, 140))
    Leg1.draw(win)
    Leg2 = Line(Point(100, 120), Point(90, 140))
    Leg2.draw(win)

def drawLine():
    win = GraphWin("Line drawer")
    message = Text(Point(100,100), "Click on first point")
    message.draw(win)
    p1 = win.getMouse()
    message.setText("Click on second point")
    p2 = win.getMouse()
    line = Line(p1, p2)
    line.draw(win)
    message.setText("")
    
def drawCircle():
    win = GraphWin("Circle")
    radius = eval(input("enter a radius: "))
    circle1 = Circle(Point(100, 100), radius)
    circle1.draw(win)
    
def drawArcheryTarget():
    win = GraphWin("Circle")
    centre = Point(100, 100)
    circle1 = Circle(centre, 20)
    circle2 = Circle(centre, 40)
    circle3 = Circle(centre, 60)
    circle3.setFill("blue")
    circle2.setFill("red")
    circle1.setFill("yellow")
    circle3.draw(win)
    circle2.draw(win)
    circle1.draw(win)
    
def drawRectangle():
    win = GraphWin("Rectangle")
    width = eval(input("enter a width: "))
    height = eval(input("enter a height: "))
    XCo = (200-width)/2
    YCo = (200-height)/2
    rectangle = Rectangle(Point(XCo, YCo), Point(200-XCo, 200-YCo))
    rectangle.draw(win)
    
def blueCircle():
    win = GraphWin("Click")
    p = win.getMouse()
    circle1 = Circle(p, 50)
    circle1.setFill("blue")
    circle1.draw(win)
    
def tenLines():
    win = GraphWin("Click")
    for i in range(10):
        p1 = win.getMouse()
        p2 = win.getMouse()
        line1 = Line(p1, p2)
        line1.draw(win)
        
def tenStrings():
    win = GraphWin("String")
    inputBox = Entry(Point(100, 15), 20)
    inputBox.draw(win)
    inputBox.setFill("white")
    for i in range(10):
         p1 = win.getMouse()
         text = Text(p1, inputBox.getText())
         text.draw(win)
         
def tenColouredRectangles():
    win = GraphWin("Rectangle")
    inputBox = Entry(Point(100, 15), 20)
    inputBox.draw(win)
    inputBox.setFill("white")
    inputBox.setText("blue")
    for i in range(10):
        p1 = win.getMouse()
        p2 = win.getMouse()
        rectangle = Rectangle(p1, p2) 
        rectangle.setFill(inputBox.getText())
        rectangle.draw(win)

def fiveClickStickman():
    win = GraphWin("StickBoy")
    p1 = win.getMouse()
    p2 = win.getMouse()
    radius = math.sqrt((p2.getX() - p1.getX())**2 + (p2.getY() - p1.getY())**2)
    circle1 = Circle(p1, radius)
    circle1.draw(win)
    p3 = win.getMouse()
    line1 = Line(Point(p1.getX(), (p1.getY() + radius)), Point(p1.getX(), p3.getY()))
    line1.draw(win)
    p4 = win.getMouse()
    distance = p1.getX() - p4.getX()
    line2 = Line(p4, Point(p1.getX() + distance, p4.getY()))
    line2.draw(win)
    p5 = win.getMouse()
    leg1 = Line(p5,p3)
    distance2 = p1.getX() - p5.getX()
    leg2 = Line(Point(p1.getX() + distance2, p5.getY()), p3)
    leg1.draw(win)
    leg2.draw(win)
    
def plotRainfall():
    win = GraphWin("Rainfall",400,200)
    inputBox = Entry(Point(100,15), 20)
    inputBox.draw(win)
    inputBox.setFill("white")
    inputBox.setText("0")
    counter = 10 
    for i in range(7):
        p1 = win.getMouse()
        rectangle = Rectangle(Point(counter,180), Point(counter + 30, 180 - int(inputBox.getText())))
        text = Text(Point(counter + 15, 190), inputBox.getText())
        counter = counter + 30
        rectangle.draw(win)
        text.draw(win)
            
def NoteExtras():
    win = GraphWin("Circle")
    radius = eval(input("enter a radius: "))
    circle1 = Circle(Point(100, 100), radius)
    circle1.draw(win)
    circle1.setOutline("brown")
    circle1.setFill("blue")
    circle1.setWidth(3)
    p1 = win.getMouse()
    circle1.move(50,50)
    radius = circle1.getRadius()
    triangle = Polygon(Point(100, 20), Point(120, 80), Point(140, 20))
    triangle.draw(win)
    label1 = Text(Point(10, 150), "Hello")
    label1.setTextColor("brown")
    label1.setSize(15)
    label1.draw(win)