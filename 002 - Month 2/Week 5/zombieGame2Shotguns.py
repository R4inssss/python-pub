# Zombie game class random
import zombiedice, sys, random


class twoshotgunZombies:
    def __init__(self, name):
        self.name = name
    def turn(self, gameState):
        shotguns = 0
        diceRollResults = zombiedice.roll()
        while diceRollResults and shotguns < 2:
            shotguns += diceRollResults['shotguns']
            diceRollResults = zombiedice.roll()



zombies = [
    twoshotgunZombies(name='Two Shotguns Zombie')]

zombiedice.runWebGui(zombies=zombies, numGames=1000)



def leave():
    sys.exit()
    KeyboardInterrupt









