#lab 10 coin array, sorting
#class pg 748
import random

class Coin:
    def __init__(self):
        self.sideup = 'Heads' #initializes object

    def toss(self):
        if random.randint(0, 1) == 0: #determines if heads or tails
            self.sideup = 'Heads'
        else:
            self.sideup = 'Tails'

    def __get_sideup(self):
        return self.sideup #get the result
