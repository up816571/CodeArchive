from employee import Employee

class MonthlyPaid(Employee):
    
    def __init__(self, name, DOB, DateOfEmploy, jobTitle, lineManager, monthlySalary):
        Employee.__init__(self, name, DOB, DateOfEmploy, jobTitle, lineManager)
        self.monthlySalary = monthlySalary
        
    def increaseMonthlySalary(self, increase):
        self.monthlySalary += increase
        
        
Jeff = MonthlyPaid("Jeff","12/12/12", "12/12/12", "Guy", "Bob", 12)
Jeff.increaseMonthlySalary(12)
