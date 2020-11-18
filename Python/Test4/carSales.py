class Car:
    
    def __init__(self, model, value, registrationNum, serviceInterval):
        self.model = model
        self.value = value
        self.registrationNum = registrationNum
        self.serviceInterval = serviceInterval
        self.mileage = 0
        
    def drive(self, additional):
        oldMile = self.mileage
        self.mileage += additional
        print("new mileage is",self.mileage,"from", oldMile)
        
    def updateValue(self, newValue):
        oldVal = self.value
        self.value = newValue
        print("Value is now", self.value, "from", oldVal)
        
    def changeRegistration(self, newReg):
        oldReg = self.registrationNum
        self.registrationNum = newReg
        print("Reg is now",self.registrationNum,"from", oldReg)
        
    def calculateMilesToNextService(self):
        distanceLeft = self.serviceInterval - self.mileage
        print("Miles left to next service",distanceLeft) 
        return distanceLeft
        
    def printCarInformation(self):
        print("Car Information")
        print(self.model)
        print("registration :",self.registrationNum)
        print("value:", self.value)
        print("current milage: ",self.mileage)
        print("Service Interval: ", self.serviceInterval)
