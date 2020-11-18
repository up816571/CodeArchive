#816571
#Course work 1 
#patch windows
from graphics import *
#Size of patch's
patchConstant = 100

def main():
    windowSize, colours = getInputs()
    totalSize = windowSize * patchConstant
    win = GraphWin("PatchWorkWindow",totalSize, totalSize)
    patchWorkColours = createPatchWork(win, windowSize, colours)
    changeColours(win, windowSize, colours, patchWorkColours)
    
def getInputs():
    while True:
        windowSize = input("Please enter a size(5, 7 or 9) ")
        if windowSize == "5" or windowSize == "7" or windowSize == "9":
            break
            
    validColours = ["red", "green", "blue", "orange", "brown", "pink"] 
    colours = []
    colourCounter = 1
    print("Please enter a valid colour, valid colours are red, green, blue, orange, brown, and pink")
    print("please enter a colour only once")
    while colourCounter <= 3:
        unique = True
        colour = input("enter colour {0} ".format(colourCounter)).lower()
        if colourCounter > 1:
            for used in range(len(colours)):
                if colour == colours[used]:
                    unique = False
        if unique == True:
            for check in range(len(validColours)):
                if colour == validColours[check]:
                    colours.append(colour)
                    colourCounter += 1
    return int(windowSize), colours

def drawCircle(win, centre, colour):
    circleRadius = 5
    circle = Circle(centre, circleRadius)
    circle.setFill(colour)
    circle.setOutline("")
    circle.draw(win)
    
def drawRectangle(win, p1, p2, colour):
    rectangle = Rectangle(p1, p2)
    rectangle.setFill(colour)
    rectangle.setOutline("")
    rectangle.draw(win)
    
#Drawing original patch    
def drawPatch(win, xStart, yStart, colour):
    drawRectangle(win, Point(xStart, yStart), Point(xStart + patchConstant, yStart + patchConstant), "white")
    for square in range(0, patchConstant, 10):
        drawRectangle(win, Point(xStart + square, yStart + patchConstant - square), \
        Point(xStart + square + 10, yStart + 90 - square), colour)

#drawing new patch
def drawAlternatePatch(win, xStart, yStart, colour):
    circlesColoured = False
    drawRectangle(win, Point(xStart, yStart),Point(xStart + patchConstant, yStart + patchConstant) , "white")
    for xRange in range(0, patchConstant, 20):
        for yRange in range(0, patchConstant, 20):
            drawSegment(win, xStart + xRange, yStart + yRange, colour, circlesColoured)
            circlesColoured = not circlesColoured    

#drawing individual segment of new patch
def drawSegment(win, xStart, yStart, colour, circlesColoured):
    p1 = Point(xStart, yStart)
    p2 = Point(xStart + 20, yStart + 20)
    if circlesColoured == False:
        drawRectangle(win, p1, p2, colour)
    for xRange in range(5, 16, 10):
        for yRange in range(5, 16, 10):
            if circlesColoured == False:
                drawCircle(win, Point(xStart + xRange, yStart + yRange), "white")
            else:
                drawCircle(win, Point(xStart + xRange, yStart + yRange), colour)
                
def createPatchWork(win, windowSize, colours):
    patchWorkColours = []
    for xRange in range(windowSize):
        for yRange in range(windowSize):
            if xRange == 0 or xRange == windowSize - 1 or yRange == 0 or yRange == windowSize - 1:
                drawAlternatePatch(win, yRange * patchConstant, xRange * patchConstant, colours[0])
                patchWorkColours.append(colours[0])
            elif windowSize - xRange > yRange:
                drawPatch(win, yRange * patchConstant, xRange * patchConstant, colours[1])
                patchWorkColours.append(colours[1])
            else:
                drawPatch(win, yRange * patchConstant, xRange * patchConstant, colours[2])
                patchWorkColours.append(colours[2])
    return patchWorkColours       
    
def updatePatch(win, yRange, xRange, patchWorkColours, windowSize, position):
    if yRange == 0 or yRange == windowSize - 1 or xRange == 0 or xRange == windowSize - 1:
        drawAlternatePatch(win, yRange * patchConstant, xRange * patchConstant, patchWorkColours[position])
    else:
        drawPatch(win, yRange * patchConstant, xRange * patchConstant, patchWorkColours[position])
    
def changeColours(win, windowSize, colours, patchWorkColours):
    while True:
        p1 = win.getMouse()
        position = 0
        for xRange in range(windowSize):
            for yRange in range(windowSize):
                if p1.getX() >= yRange * patchConstant and p1.getX() < yRange * patchConstant + patchConstant and \
                p1.getY() >= xRange * patchConstant and  p1.getY() < xRange * patchConstant + patchConstant:
                    if patchWorkColours[position] == colours[0]:
                        patchWorkColours[position] = colours[1]
                    elif patchWorkColours[position] == colours[1]:
                        patchWorkColours[position] = colours[2]
                    else:
                        patchWorkColours[position] = colours[0]
                    updatePatch(win, yRange, xRange, patchWorkColours, windowSize, position)
                position += 1

main()