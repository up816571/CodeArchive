from carSales import Car

class LeaseCar(Car):
    
    def __init__(self, maximumYearlyMileage, model, value, registrationNum, serviceInterval):
        Car.__init__(self, model, value, registrationNum, serviceInterval)
        self.maximumYearlyMileage = maximumYearlyMileage
        
    def calculateAdditionalCost(self):
        if self.mileage > self.maximumYearlyMileage:
            additionalCost = (self.mileage - self.maximumYearlyMileage) * 0.5
            print("Additional cost is : £", additionalCost)
        else:
            print("no additional cost")
        
    def driveLeaseCar(self, addded):
        self.mileage += addded
        print("mileage : ", self.mileage)
    