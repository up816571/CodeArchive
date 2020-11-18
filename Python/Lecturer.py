class Lecturer:
    
    def __init__(self, firstName, lastName, salary, unitsTaught):
        self.firstName = firstName
        self.lastName = lastName
        self.salary = salary
        self.unitsTaught = unitsTaught
        
    def addUnit(self, unitName):
        self.unitsTaught.append(unitName)
        
    def removeUnit(self, unitName):
        self.unitsTaught.remove(unitName)
        
    def givePayRise(self, risePercentage):
        self.salary = self.salary * risePercentage
        
    def printLecturerInformation(self):
        print(self.firstName)
        print(self.lastName)
        print(self.salary)
        print(self.unitsTaught)