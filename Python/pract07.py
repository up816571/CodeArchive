#-------------------------------------------------------------------------------
# Practical Worksheet 7: Booleans and while loops
# Josh Ruffle
# 816571
#-------------------------------------------------------------------------------

from graphics import *
import time
import math
import random

# For exercise 2
def trafficLights():
    win = GraphWin()
    red = Circle(Point(100, 50), 20)
    red.setFill("red")
    red.draw(win)
    amber = Circle(Point(100, 100), 20)
    amber.setFill("black")
    amber.draw(win)
    green = Circle(Point(100, 150), 20)
    green.setFill("black")
    green.draw(win)
    while True:
        amber.setFill("yellow")
        time.sleep(5)
        amber.setFill("black")
        red.setFill("black")
        green.setFill("green")
        time.sleep(5)
        amber.setFill("yellow")
        green.setFill("black")
        time.sleep(5)
        red.setFill("red")
        amber.setFill("black")
        time.sleep(5)


# For exercise 6
def fahrenheit2Celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def celsius2Fahrenheit(celsius):
    return 9 / 5 * celsius + 32

def tempratureConveter():
    another = "y"
    while another == "y":
        typeOfCalc = input("do you want to convert celsius or fahrenheit(c/f): ")
        value  = eval(input("what temprature do you want to convert: "))
        if typeOfCalc == "c":
            print(celsius2Fahrenheit(value))
        elif typeOfCalc == "f":
            print(fahrenheit2Celsius(value))
        another = input("another calculation? (y/n): ")


def getName():
    name = input("Write a name ")
    while name.isalpha() == False:
        name = input("Write a name")
    return name
    
def calculateGrade(mark):
    if mark > 20:
        return("X")
    elif mark >= 16:
        return("A")
    elif mark >=12:
        return("B")
    elif mark >= 8:
        return("C")
    elif mark > 0:
        return("F")
    else:
        return("X")
        
def gradeCoursework():
    marks = eval(input("enter grade "))
    while calculateGrade(marks) == "X":
        marks = eval(input("enter grade "))
    print("The mark is",calculateGrade(marks))
    
def orderPrice():
    totalOrder = 0
    while true:
        price = eval(input("enter a price" ))
        quantity = eval(input("enter amount" ))
        totalOrder = totalOrder + price * quantity
        another = input("another? (y/n) ")
        if another == "n":
            break
    print("£{0:0.2f}".format(totalOrder))
    
def clickableEye():
    win = GraphWin()
    drawColouredEye(win, Point(100, 100), 100, "brown")
    distance = 0
    label1 = Text(Point(100, 180),"")
    label1.draw(win)
    while distance <= 100:
        p1 = win.getMouse()
        distance = abs(distanceBetweenPoints(Point(100, 100), p1))
        if distance <= 25:
            label1.setText("Pupil")
        elif distance <= 50:
            label1.setText("iris")
        elif distance <= 100:
            label1.setText("sclera")


def distanceBetweenPoints(p1, p2):
    x1 = p1.getX()
    y1 = p1.getY()
    x2 = p2.getX()
    y2 = p2.getY()
    return math.sqrt((x2 - x1)**2 + (y2-y1)**2)    

def drawCircle(win, centre, radius, colour):
    circle = Circle(centre, radius)
    circle.setFill(colour)
    circle.draw(win)

def drawColouredEye(win, centre, radius, colour):
    drawCircle(win, centre, radius, "white")
    drawCircle(win, centre, radius/2, colour)
    drawCircle(win, centre, radius/4, "black")
    
def guessTheNumber():
    number = random.randint(1, 100)
    numberOfGuess = 0
    wonGame = False
    while (numberOfGuess < 7) and (wonGame == False):
        numberOfGuess = numberOfGuess + 1
        guess = eval(input("enter a number: "))
        if guess == number:
            wonGame = True
            print("you won in", numberOfGuess)
            return
        elif guess < number:
            print("too low")
        else:
            print("too high")
        print("lose, the number was ", number)
   
def scoreDif(count1,count2):
    return abs(count1 - count2)
     
def tableTennisScore():
    win = GraphWin()
    line = Line(Point(100, 0), Point(100, 200))
    player1Count = 0
    player2Count = 0
    player1 = Text(Point(50, 100),str(player1Count))
    player2 = Text(Point(150, 100),str(player2Count))
    line.draw(win)
    player1.draw(win)
    player2.draw(win)
    while player1Count < 11 and player2Count < 11 or scoreDif(player1Count,player2Count) < 2: 
        p1 = win.getMouse()
        if p1.getX() < 100:
            player1Count = player1Count + 1
            player1.setText(str(player1Count))
        else:
            player2Count = player2Count + 1
            player2.setText(str(player2Count))
    winText = Text(Point(50, 175), "win")
    winText.draw(win)
    if player2Count >= 11 and scoreDif(player1Count,player2Count) >= 2:
        winText.move(100, 0)
    
def clickableBoxOfEyes():
    rows = eval(input("enter the amount of rows: "))
    column = eval(input("Enter the amount of columns: "))
    win = GraphWin("eyes",column * 100 + 100,rows * 100 + 100)
    rectangle1 = Rectangle(Point(50, 50), Point(50 + column * 100, 50 + rows * 100))
    rectangle1.draw(win)
    for i in range(rows):
        for j in range(column):
            drawColouredEye(win, Point(100 + j * 100, 100 + i * 100), 50, "blue")
    label1 = Text(Point(50 + column * 50, 70 + rows * 100),"")
    label1.draw(win)
    p1 = win.getMouse()
    while (p1.getX() >= 50) and (p1.getY() >= 50) and (p1.getX() <= 50 + column * 100) and (p1.getY() <= 50 + rows * 100):
        isEye = False
        for i in range(rows):
            for j in range(column):
                if distanceBetweenPoints(p1, Point(100 + j * 100, 100 + i * 100)) <= 50:
                    label1.setText("eye at column {0} rows {1}".format(j + 1,i + 1))
                    isEye = True
        if isEye == False:
            label1.setText("between")
        p1 = win.getMouse()
    win.close()
    
def findTheCircle():
    win = GraphWin()
    radius = 30
    score = 0 
    label = Text(Point(100, 190),"")
    label.draw(win)
    while True:
        attempt = 0
        wonGame = False
        centre = Point(random.randint(30,170),random.randint(30,170))
        circle = Circle(centre, radius)
        distanceCount = 0
        while attempt < 10 and wonGame == False:
            attempt += 1
            p1 = win.getMouse()
            if distanceBetweenPoints(p1, centre) <= radius:
                wonGame = True
                circle.draw(win)
                label.setText("win")
                score += 11 - attempt
            else:
                if distanceBetweenPoints(p1, centre) > distanceCount:
                    label.setText("futher away")
                else:
                    label.setText("closer")
            distanceCount = distanceBetweenPoints(p1, centre)
        if attempt == 10:
            label.setText(score)
            circle.draw(win)
            time.sleep(5)
            break
        label.setText(score)
        radius *= 0.9
        time.sleep(5)
        circle.undraw()
        
