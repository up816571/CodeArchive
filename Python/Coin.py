import random 

class Coin:
    
    def __init__(self, value):
        self.value = value
        
    def flipCoin(self):
        coinSide = random.randint(1,2)
        if coinSide == 1:
            return("Heads")
        else:
            return("Tails")