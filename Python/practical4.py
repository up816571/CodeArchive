#Joshua Ruffle up816571
#Practical number 4

from graphics import *
import os 

def personalGreeting():
    name = input("What is your name? ")
    print('Hello ',name,', nice to see you!')

def formalName():
    firstname = input("What is your first name? ")
    surname = input("What is your surname? ")
    print(firstname[0],'.',surname)
    
def kilos2pounds():
    kilos = eval(input("Enter a weight in kilograms: "))
    pounds = 2.2 * kilos
    print("{0:0.2f} kilos is equal to {1:0.2f} pounds".format(kilos, pounds))
    
def generateEmail():
    firstname = input("What is your first name? ")
    surname = input("What is your surname? ")
    yearEntered = input("What year did you enter the uni? ")
    newEmail = surname[0:4] + "." + firstname[0] + "." + yearEntered[2:4] + "@myport.ac.uk"
    print(newEmail)

def gradeTest():
    grade = eval(input("please enter a grade mark btween 0 and 10: "))
    stringOfLeters = "FFFFCCBBAAA"
    print(stringOfLeters[grade])
    
def graphicsLetters():
    word = input("Enter a word: ")
    win = GraphWin("text")
    for i in range(len(word)):
        p1 = win.getMouse()
        text = Text(p1, word[i])
        text.setSize(30)
        text.draw(win)
        
def singASong():
    word = input("Enter a word: ")
    lines = eval(input("Enter how many lines it should be: "))
    repeats = eval(input("How many times should it be repeated per line: "))
    for i in range(lines):
        print((word*repeats)," ")
        
def exchangeTable():
    for euros in range(21):
        pounds = euros / 1.15
        print("{0:6.2f} | {1:6.2f}".format(euros, pounds))
        
def makeAcronym():
    sentence = input("Enter a sentence: ")
    words = sentence.split()
    for i in range (len(words)):
        print((words[i][0]).upper(), end='')
        
def nameToNumber():
    name = input("What is your name? ").lower()
    letters = "abcdefghijklmnopqrstuvwxyz"
    total = 0
    for i in range(len(name)):
        total = total + letters.find(name[i]) + 1
    print(total)
    
def fileInCaps():
    name = input("enter files name: ")
    fileLoc = open(name, "r")
    contents = fileLoc.read()
    print(contents.upper())
    
def rainfallChart():
    file = open("rainfall.txt","r")
    contents = file.read().split()
    file.close()
    for i in range(int(len(contents) / 2)):
        nameOfCity = contents[i * 2]
        rainfall = int(contents[i * 2 + 1])
        print("{0:<14}".format(nameOfCity) + "*" * rainfall)
    
def graphicalRainfallChart():
    win = GraphWin("rain")
    file = open("rainfall.txt","r")
    contents = file.read().split()
    file.close()
    for i in range(int(len(contents) / 2)):
        nameOfCity = contents[i * 2]
        label = Text(Point(50, 20 + 20 * i), "{0:>10}".format(nameOfCity))
        label.draw(win)
        rainfall = int(contents[i * 2 + 1])
        rectangle = Rectangle(Point(120, 10 + 20 * i ), Point(120 + rainfall, 30 + 20 * i))
        rectangle.draw(win)
        
def rainfallInInches():
    file = open("rainfall.txt","r")
    contents = file.read().split()
    file.close()
    writingFile = open("rainfallInInches.txt","w")
    for i in range(int(len(contents) / 2)):
        nameOfCity = contents[i * 2]
        rainfall = int(contents[i * 2 + 1]) / 25.4
        print("{0} {1:0.2f}".format(nameOfCity, rainfall), file=writingFile)
    writingFile.close
        
def wc():
    fileName = input("Enter a file's name: ")
    inputFile = open(fileName, "r")
    fileString = inputFile.read()
    print("Characters :",len(fileString))
    print("Words: ", len(fileString.split()))
    print("Lines: ", len(fileString.split("\n")))

    