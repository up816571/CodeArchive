# Practical Worksheet 1: Getting started with Python 
# your name Josh Ruffle, your number 816571

def sayHello():
    print("Hello world")
    
def sayHello2():
    print("hello")
    print("world")

def count():
    for i in range(10):
        print(i+1)
    
def sayname():
    print("Josh")

def kilos2pounds():
    kilos = eval(input("Enter a weight in kilograms: "))
    pounds = 2.2 * kilos
    print("The weight in pounds is", pounds)
    
def euros2pounds():
    euros = eval(input("Enter an amount of euros: "))
    pounds = euros / 1.15
    print("the ammount of pounds is", pounds)
    
def addUp():
    number1 = eval(input("Enter a number: "))
    number2 = eval(input("enter another: " ))
    print(number1 + number2)
    
def changecounter():
    onepence = eval(input("How many 1p's do you have?: "))
    twopence = eval(input("How many 2p's do you have?: "))
    fivepence = eval(input("How many 5p's do you have?: "))
    total = onepence+(twopence*2)+(fivepence*5)
    print("the total amount of pennies you have is: ", total)
    
def tenHellos():
    for i in range(10):
        print("Helloworld")
        
def weightsTable():
    kilo = 0
    print("kilos | pounds")
    while kilo <= 100:
        print(kilo," | ", 2.2 * kilo)
        kilo = kilo + 10 
        
def futureValue():
    amount = eval(input("Enter an amount of money: "))
    years = eval(input("How long would you like to store it: "))
    for i in range(years):
        #intial = amount
        amount = amount * 1.055
        #difference = amount - intial 
        #print("year ",(i+1)," intrest earnt", difference)
    print(amount)
    
    
    
    
# \[O]/
    