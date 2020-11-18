class Employee:
    
    def __init__(self, name, DOB, DateOfEmploy, jobTitle, lineManager):
        self.name = name
        self.DOB = DOB
        self.DateOfEmploy = DateOfEmploy
        self.jobTitle = jobTitle
        self.lineManager = lineManager
        
    def changeName(self, newName):
        self.name = newName
        
    def changeJobTitle(self, newJob):
        self.jobTitle = newJob
        
    def printEmployee(self):
        print(self.name, self.DOB, self.DateOfEmploy, self.jobTitle, self.lineManager)
        
    def changeLineManager(self, newline):
        self.lineManager = newline