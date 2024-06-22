# Zombie game class random
import zombiedice, sys, random


class gunsoverBrainsZombie:
    def __init__(self, name):
        self.name = name
    def turn(self, gameState):
        brains = 0
        shotguns = 0
        diceRollResults = zombiedice.roll()
        while diceRollResults and shotguns <= brains:
            brains += diceRollResults['brains']
            shotguns += diceRollResults['shotgun']
            diceRollResults = zombiedice.roll()


zombies = [
    gunsoverBrainsZombie(name='Guns Over Brains Zombie')]

zombiedice.runWebGui(zombies=zombies, numGames=1000)



def leave():
    sys.exit()
    KeyboardInterrupt









