import random

class Dice:
    
    def __init__(self, sideLabels):
        self.sideLabels = sideLabels
        self.sides = len(sideLabels)
    
    def throwDice(self):
        landedSide = random.randint(0,self.sides)
        return self.sideLabels[landedSide]\
        
    