#Josh ruffle
#816571

import random
import math

def getinput():
    number = eval(input("how many times to flip the coin? "))
    return number

def simulateFlips(number):
    heads = 0
    tails = 0
    for i in range(number):
        coinSide = random.randint(1,2)
        if coinSide == 1:
            heads += 1
        else:
            tails += 1
    return heads, tails

def displayResults(heads, tails, number):
    print("Heads {0} proportion {1:0.2f}".format(heads, heads/number))
    print("Tails {0} proportion {1:0.2f}".format(tails, tails/number))


def main():
    number = getinput()
    heads, tails = simulateFlips(number)
    displayResults(heads, tails, number)
    
main()