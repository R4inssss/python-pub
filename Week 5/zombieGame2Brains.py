# Zombie game class random
import zombiedice, sys, random


class twobrainsZombie:
    def __init__(self, name):
        self.name = name
    def turn(self, gameState):
        brains = 0
        diceRollResults = zombiedice.roll()
        while diceRollResults and brains < 2:
            brains += diceRollResults['brains']
            diceRollResults = zombiedice.roll()



zombies = [
    twobrainsZombie(name='Two Brains Zomie')]

zombiedice.runWebGui(zombies=zombies, numGames=1000)



def leave():
    sys.exit()
    KeyboardInterrupt









