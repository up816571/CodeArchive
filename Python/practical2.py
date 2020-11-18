#Josh Ruffle 816571
import math
import time 
import random
import numpy as np

def warmup():
    x1 = 1
    y1 = 2
    x2 = 4 
    y2 = 6 
    slope = (y2 - y1)/(x2-x1)
    print(slope)
    distance  = math.sqrt((x2 - x1)**2 + (y2-y1)**2)
    print(distance)
#end of warmup
#start of questions 
def  circumferenceOfCircle():
    radius = eval(input("enter a radius: "))
    circumference = 2*math.pi*radius
    print(circumference)

def areaOfCircle():
    radius = eval(input("enter a radius: "))
    print(math.pi*radius**2)
    
def costOfPizza():
    diameter = eval(input("enter a diameter in cm: "))
    area = math.pi*(diameter/2)**2
    print("the cost of the pizza is",area*1.5,"Pence")
    
def slopeOfLine():
    x1 = eval(input("input an x coordinate: "))
    y1 = eval(input("input a y coordinate: "))
    x2 = eval(input("input a second x coordinate: "))
    y2 = eval(input("input a second y coordinate: "))
    print((y2 - y1)/(x2-x1))
    
def distanceBetweenPoints():
    x1 = eval(input("input an x coordinate: "))
    y1 = eval(input("input a y coordinate: "))
    x2 = eval(input("input a second x coordinate: "))
    y2 = eval(input("input a second y coordinate: "))
    print(math.sqrt((x2 - x1)**2 + (y2-y1)**2))
    
def travelStatistics():
    speed = eval(input("input the average speed of the car in KM/H: "))
    duration = eval(input("input the duration of the journey in hours: "))
    distance = speed * duration 
    print("the distacne traveled was ",distance,"KM")
    print("the total fuel usage was",(distance/5),"litres")
    
def sumOfNumbers():
    n = eval(input("Enter a number: "))
    total = 0
    for i in range(n+1):
        total = total + i
    print(total)
#Harder    
def averageOfNumbers():
    totalnum = eval(input("how many numbers will you enter?: "))
    total = 0
    for i in range(totalnum):
        temp = eval(input("enter a number: "))
        total = total + temp
    print(total/totalnum)
    
def selectCoins():
    pence = eval(input("how much pence do you have?: "))
    for i in [200,100,50,20,5,2,1]:
        amount = pence // i
        pence = pence % i
        print(amount,"X",i,"p")
        
def fruits():
    fruits = ["apple", "banana", "cherry"]
    for x in fruits:
        print(x)
    
def whileLoop():
    i = 1
    while i < 6:
        print(i)
        i += 1
        
def rangeTest():
    x = range(1, 10 , 3)
    for i in x:
        print(i)
        
def arrayExample():
    x = np.array([3, 6, 9, 12])
    y = random.random()
    print(x)
    print(y)