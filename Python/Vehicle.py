class Vehicle:
    
    def __init__(self, numWheel, engineSize, manual, currentGear):
        self.numWheel = numWheel
        self.engineSize = engineSize
        self.manual = manual
        self.currentGear = currentGear
        self.doorsLocked = False
        
    def Drive(self):
        print("go")
        
    def changeGear(self, newGear):
        self.currentGear = newGear
        
    def lockDoors(self):
        self.doorsLocked = True
        
    def unlockDoors(self):
        self.doorsLocked = False