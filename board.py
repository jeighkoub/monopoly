#monopoly board
import random
from player import Player

def payRent(landed,owner, amount):
    landed.money -= amount #if not enough i guess they create money before bankrupting idc
    owner.money += amount
    print(f"{landed.name} paid {owner.name} ${amount} in rent")

class Space:
    def __init__(self, name):
        self.name = name
    def onLand(self, player: Player):
        print(f"{player.name} landed on {self.name}. Nothing happens")
        pass

class Property(Space):
    def __init__(self, name, price, color, rent: list):
        super().__init__(name)
        self.price = price
        self.rent = rent #topay = rent[numHouses]
        self.color = color
        self.owner = None
        self.mortgaged = False
        self.houses = 0
    def onLand(self, player: Player):
        print(f"{player.name} landed on {self.name}")
        if self.owner is None:
            player.buyProperty(self)
        elif self.owner != player:
            payRent(player,self.owner, self.rent[self.houses])

class Jail(Space):
    def __init__(self):
        super().__init__("Jail")
    def onLand(self, player: Player):
        print(f"{player.name} is meeting diddy")
        player.jail = True

class Tax(Space):
    def __init__(self, name, amount):
        super().__init__(name)
        self.amount = amount
    def onLand(self, player: Player):
        print(f"{player.name} landed on {self.name} and became republican")
        player.money -= self.amount #no money checks just print money

#both chance and communmity chest spaces
# random bullshit happens and i'm ignoring the real odds and amounts
class Random(Space):
    def __init__(self, name):
        super().__init__(name)
    def onLand(self, player):
        print(f"{player.name} landed on {self.name}. Random stuff happens to diguise the lack of gameplay")
        match random.randint(1,3):
            case 1:
                player.money += random.randint(1,100)
            case 2:
                player.money -= random.randint(1,100)
            case 3:
                player.jail = True # apparently jail is an option tf


class Board:
    def __init__(self, custom_setup=None):
        if custom_setup is None:
            self.spaces = [None] * 40
            # ai generated values i'm not looking up each of 26 properties' rent array
            self.spaces[0] = Space("Go") # passing logic in game
            self.spaces[1] = Property("Mediterranean Avenue", 60, 0, [2, 10, 30, 90, 160, 250])
            self.spaces[2] = Random("Community Chest")
            self.spaces[3] = Property("Baltic Avenue", 60, 0, [4, 20, 60, 180, 320, 450])
            self.spaces[4] = Space("Income Tax")
            self.spaces[5] = Property("Reading Railroad", 200, 0, [25, 50, 100, 200, 200, 200])
            self.spaces[6] = Property("Oriental Avenue", 100, 1, [6, 30, 90, 270, 400, 550])
            self.spaces[7] = Random("Chance")
            self.spaces[8] = Property("Vermont Avenue", 100, 1, [6, 30, 90, 270, 400, 550])
            self.spaces[9] = Property("Connecticut Avenue", 120, 1, [8, 40, 100, 300, 450, 600])
            self.spaces[10] = Space("Just Visiting")
            self.spaces[11] = Property("St. Charles Place", 140, 2, [10, 50, 150, 450, 625, 750])
            self.spaces[12] = Space("Electric Company")
            self.spaces[13] = Property("States Avenue", 140, 2, [10, 50, 150, 450, 625, 750])
            self.spaces[14] = Property("Virginia Avenue", 160, 2, [12, 60, 180, 500, 700, 900])
            self.spaces[15] = Property("Pennsylvania Railroad", 200, 2, [25, 50, 100, 200, 200, 200])
            self.spaces[16] = Property("St. James Place", 180, 3, [14, 70, 200, 550, 750, 950])
            self.spaces[17] = Random("Community Chest")
            self.spaces[18] = Property("Tennessee Avenue", 180, 3, [14, 70, 200, 550, 750, 950])
            self.spaces[19] = Property("New York Avenue", 200, 3, [16, 80, 220, 600, 800, 1000])
            self.spaces[20] = Space("Free Parking")
            self.spaces[21] = Property("Kentucky Avenue", 220, 4, [18, 90, 250, 700, 875, 1050])
            self.spaces[22] = Random("Chance")
            self.spaces[23] = Property("Indiana Avenue", 220, 4, [18, 90, 250, 700, 875, 1050])
            self.spaces[24] = Property("Illinois Avenue", 240, 4, [20, 100, 300, 750, 925, 1100])
            self.spaces[25] = Property("B. & O. Railroad", 200, 4, [25, 50, 100, 200, 200, 200])
            self.spaces[26] = Property("Atlantic Avenue", 260, 5, [22, 110, 330, 800, 975, 1150])
            self.spaces[27] = Property("Ventnor Avenue", 260, 5, [22, 110, 330, 800, 975, 1150])
            self.spaces[28] = Property("Water Works", 150, 5, [4, 10, 20, 40, 40, 40])
            self.spaces[29] = Property("Marvin Gardens", 280, 5, [24, 120, 360, 850, 1025, 1200])
            self.spaces[30] = Space("Go To Jail")
            self.spaces[31] = Property("Pacific Avenue", 300, 6, [26, 130, 390, 900, 1100, 1275])
            self.spaces[32] = Property("North Carolina Avenue", 300, 6, [26, 130, 390, 900, 1100, 1275])
            self.spaces[33] = Random("Community Chest")
            self.spaces[34] = Property("Pennsylvania Avenue", 320, 6, [28, 150, 450, 1000, 1200, 1400])
            self.spaces[35] = Property("Short Line", 200, 6, [25, 50, 100, 200, 200, 200])
            self.spaces[36] = Random("Chance")
            self.spaces[37] = Property("Park Place", 350, 7, [35, 175, 500, 1100, 1300, 1500])
            self.spaces[38] = Space("Luxury Tax")
            self.spaces[39] = Property("Boardwalk", 400, 7, [50, 200, 600, 1400, 1700, 2000])

            



        

            
        #custom setup
        else:
            raise NotImplementedError("not doing all that")