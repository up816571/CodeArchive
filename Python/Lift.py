class Lift:
    
    def __init__(self, maxFloors):
        self.maxNoFloors = maxFloors
        self.currentFloor = 0
        print("Current floor is : floor", self.currentFloor)
        
    def goUp(self, targetFloor):
        if targetFloor > self.maxNoFloors:
            print("That is not a valid floor. The lift will not move.")
        elif targetFloor < self.currentFloor:
            print("You need to go down. The lift will not move.")
        else:
            floorsToMove = targetFloor - self.currentFloor
            for i in range(floorsToMove):
                print("Going up : floor number", self.currentFloor)
                self.currentFloor += 1
            print("The lift has arrived at floor", self.currentFloor)
            
    def goDown(self, targetFloor):
        if targetFloor < 0:
            print("That is not a valid floor. The lift will not move.")
        elif targetFloor > self.currentFloor:
            print("You need to go up. The lift will not move.")
        else:
            floorsToMove = self.currentFloor - targetFloor
            for i in range(floorsToMove):
                print("Going down : floor number", self.currentFloor)
                self.currentFloor -=1
            print("The lift has arrived at floor", self.currentFloor)
            
    def callLift(self, floorCalledFrom):
        if floorCalledFrom > self.currentFloor:
            self.goUp(floorCalledFrom)
        elif floorCalledFrom < self.currentFloor:
            self.goDown(floorCalledFrom)
        else:
            print("Lift already at the floor")
        
        
