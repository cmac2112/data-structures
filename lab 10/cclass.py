#coin class page 749
import random
class Coin:
    def __init__(self):
        self.side = 1
#1 heads
#0 tails
    def toss(self):
        if random.randint(0 , 1) == 0:
            self.side = 1
        else:
            self.side = 0
            
    def get_side(self):
        return self.side
