#-------------------------------------------------------------------------------
# house.py - a simple program to draw a house
#-------------------------------------------------------------------------------

from graphics import *

def main():
    doorColour, lightsOn, size, doorNum = getInputs()
    drawHouse(doorColour, lightsOn, size, doorNum)

def getInputs():
    doorColour = input("Enter door colour: ")
    lightsYN = input("Are the lights on (y/n): ")
    lightsOn = lightsYN[0] == "y"
    size = eval(input("Please enter the size: "))
    doorNum = eval(input("What will the door number be: "))
    return doorColour, lightsOn, size, doorNum

def drawHouse(doorColour, lightsOn, size, doorNum):
    win = GraphWin("House", size, size)
    win.setCoords(0, 2, 2, 0)

    roof = Polygon(Point(0.02, 0.6), Point(0.42, 0.02),
                   Point(1.58, 0.02), Point(1.98,0.6))
    roof.setFill("pink")
    roof.draw(win)

    # draw wall and door
    drawRectangle(win, Point(0.02, 0.6), Point(1.98, 1.98), "brown")
    drawRectangle(win, Point(0.3, 1.1), Point(0.8, 1.98), doorColour)

    #number
    drawText(win, Point(0.55, 1.3), doorNum)
    
    # draw window
    if lightsOn:
        windowColour = "yellow"
    else:
        windowColour = "black"
    drawRectangle(win, Point(110, 110), Point(170, 170), windowColour)
    
def drawRectangle(win, point1, point2, colour):
    rectangle = Rectangle(point1, point2)
    rectangle.setFill(colour)
    rectangle.setOutline(colour)
    rectangle.draw(win)
    
def drawText(win, point1, doorNum):
    number = Text(point1, doorNum)
    number.draw(win)

main()

