class Padlock:

    def __init__(self, combination):
        self.combination =  combination
        self.combinationNoDigits = len(combination)
        self.open = False
        
    def openLock(self, enteredCombination):
        if enteredCombination == self.combination:
            self.open = True
            
    def closeLock(self):
        if self.open == True:
            self.open = False
            
    def changeCombination(self, newCombination):
        if self.open == True:
            self.combination = newCombination
            