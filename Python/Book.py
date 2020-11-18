class Book:
    
    def __init__(self, title, author, noPages, isbn, price):
        self.title = title
        self.author = author
        self.numberOfPages = noPages
        self.ISBN = isbn
        self.price = price
        self.copies = 0
        
    def changePrice(self, newPrice):
        self.price = newPrice
        
    def sellCopy(self):
        if self.copies > 0:
            self.copies -= 1
    
    def restock(self, newCopies):
        self.copies = self.copies + newCopies
        
    def retrieveBookInformation(self):
        print(self.title)
        print(self.author)
        print(self.numberOfPages)
        print(self.ISBN)
        print(self.price)
        print(self.copies)