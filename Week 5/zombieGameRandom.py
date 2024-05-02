# Zombie game class random
import zombiedice, sys, random


class randomZombie:
    def __init__(self, name):
        self.name = name
    def turn(self, gameState):
        diceRollResults = zombiedice.roll()
        while diceRollResults and random.choice([True, False]):
            diceRollResults = zombiedice.roll()



zombies = [
    randomZombie(name='Random Zombie')]

zombiedice.runWebGui(zombies=zombies, numGames=1000)



def leave():
    sys.exit()
    KeyboardInterrupt









