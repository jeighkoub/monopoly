#monopoly player why is this a separate file am i stupid
import random

class Player:
    def __init__(self, name, money):
        self.colors = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
        self.name = name
        self.money = money
        self.position = 0
        self.jail = False
        self.doubleCount = 0
        self.owns = []
    def buyProperty(self, property):
        if self.money >= property.price:
            self.money -= property.price
            property.owner = self
            self.owns.append(property)
            print("You bought", property.name)
        else:
            print("Not enough money")
    
    
    def isBankrupt(self):
        return self.money <= 0
    
class Bot(Player):
    def __init__(self, name, money):
        super().__init__(name, money)
    def buyProperty(self, property):
        if True: # it' always optimal to buy
            if self.money >= property.price:
                self.money -= property.price
                property.owner = self
                self.owns.append(property)
                print(f"bot {self.name} bought {property.name}")
        else:
            print("Not enough money")
    
    def decide(self):
        return random.randint(1,3) # if enough money buy else not, implement later
    
    def isBankrupt(self):
        return self.money <= 0
    

    
