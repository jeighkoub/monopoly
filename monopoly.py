from player import *
from board import *
import random

import inspect#why tf is onLand passing

class Monopoly:
    def __init__(self):
        self.players = [Bot("Bot1", 1000), Bot("Bot2", 1000), Bot("Bot3", 1000)]
        playerName = input("Enter your name: ")
        self.players.append(Player(playerName, 1000))
        self.board = Board()

    def play(self):
        print("Game start")
        remove = []
        #rounds
        roundCount = 0
        while len(self.players) > 1:
            roundCount += 1
            print(f"Round {roundCount}")

            #turns
            
            for r in remove:
                self.players.remove(r)
            remove = []
            for player in self.players:
                print(f"{player.name}'s turn")
                if player.isBankrupt():
                    #self.players.remove(player)
                    remove.append(player) # can py find payer without overloaded == ???
                    print(f"{player.name} is poor")
                    continue
                r1 = random.randint(1, 6)
                r2 = random.randint(1, 6)
                if r1 == r2:
                    player.doubleCount += 1
                else:
                    player.doubleCount = 0
                if player.doubleCount == 3:
                    player.jail = True
                    player.position = 10
                    continue
                player.position += r1 + r2
                if player.position >= 40:
                    player.position -= 40
                    player.money += 200
                player.position %= 40
                landed = self.board.spaces[player.position]
                print(f"{player.name} landed on {landed.name}")
   



