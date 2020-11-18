class BagOfChange:
    
    def __init__(self , pence1, pence2, pence5, pence10, pence20, pence50, pound1, pound2):
        self.money = [pence1, pence2, pence5, pence10, pence20, pence50, pound1, pound2]
        self.amount = [1,2,5,10,20,50,100,200]
        
    def removeCoin(self, coin):
        index = self.amount.index(coin)
        self.money[index] -= 1
        
    def addCoin(self, coin):
        index = self.amount.index(coin)
        self.money[index] += 1
        
    def totalNoCoins(self):
        totalCoins = 0
        for i in range(len(self.money)):
            totalCoins = totalCoins + self.money[i]
        print(totalCoins)
        
    def totalValue(self):
        totalVal = 0 
        for i in range(len(self.money)):
            totalVal = totalVal + self.money[i] * self.amount[i]
        print(totalVal)