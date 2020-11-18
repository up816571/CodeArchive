#josh ruffle
#816571

def takeAWalk(numSteps):
    from random import random
    stepsForwardOfStartX = 0
    stepsForwardOfStartY = 0
    for step in range(numSteps):
        chance = random()
        if chance < 0.25:
            stepsForwardOfStartX = stepsForwardOfStartX - 1
        elif chance < 0.5:
            stepsForwardOfStartX = stepsForwardOfStartX + 1
        elif chance < 0.75:
            stepsForwardOfStartY = stepsForwardOfStartY - 1
        else:
            stepsForwardOfStartY = stepsForwardOfStartY + 1
    distance = distanceBetweenPoints(stepsForwardOfStartX, stepsForwardOfStartY)
    return abs(distance)

def distanceBetweenPoints(X, Y):
    import math
    distance = math.sqrt(X**2 + Y**2)
    return distance

def printExpectedDistance(averageSteps):
    print("The expected number of steps away from the", end=" ")
    print("start point is {0:0.02f}".format(averageSteps))

def takeWalks(numWalks, numSteps):
    totalSteps = 0
    for walk in range(numWalks):
        stepsAway = takeAWalk(numSteps)
        totalSteps = totalSteps + stepsAway
    return totalSteps / numWalks

def getInputs():
    numWalks = eval(input("How many random walks to take? "))
    numSteps = eval(input("How many steps for each walk? "))
    return numWalks, numSteps

def main():
    numWalks, numSteps = getInputs()
    averageSteps = takeWalks(numWalks, numSteps)
    printExpectedDistance(averageSteps)

main()