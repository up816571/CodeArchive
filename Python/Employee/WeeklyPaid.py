from employee import Employee

class WeeklyPaid(Employee):
    
    def __init__(self, name, DOB, DateOfEmploy, jobTitle, lineManager, hourlyRate, numberHours):
         Employee.__init__(self, name, DOB, DateOfEmploy, jobTitle, lineManager)
         self.hourlyRate = hourlyRate
         self.numberHours = numberHours
         
    def recordHours(self, hoursWorked):
        self.numberHours += hoursWorked
        
    def payWeeklyWage(self):
        print(self.hourlyRate * self.numberHours)