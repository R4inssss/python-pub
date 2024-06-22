# Zombie Game v.4
# So first, I had to do some research into classes, which is documented outside of this

import zombiedice, sys, random

class randomZombie:
    def __init__(self, name):
        self.name = name
    def turn(self, gameState):
        diceRollResults = zombiedice.roll()
        while diceRollResults and random.choice([True, False]):
            diceRollResults = zombiedice.roll()


class twobrainsZombie:
    def __init__(self, name):
        self.name = name
    def turn(self, gameState):
        brains = 0
        diceRollResults = zombiedice.roll()
        while diceRollResults and brains < 2:
            brains += diceRollResults['brains']
            diceRollResults = zombiedice.roll()

class twoshotgunsZombie:
    def __init__(self, name):
        self.name = name
    def turn(self,gameState):


class indecisiveZombie:
    def __init__(self, name):
        self.name = name
    def turn(self,gameState):

class gunsoverBrainsZombie:
    def __init__(self, name):
        self.name = name
    def turn(self,gameState):









zombies = [
    randomZombie(name='Random Zombie'),
    twobrainsZombie(name='Two Brains Zombie'),
    twoshotgunsZombie(name='Two Shotguns Zombie'),
    indecisiveZombie(name='Indecisive Zombie'),
    gunsoverBrainsZombie(name='More Shotguns Than Brains Zombie'),
]

# Uncomment one of the following lines to run in CLI or Web GUI mode:
#zombiedice.runTournament(zombies=zombies, numGames=1000)
zombiedice.runWebGui(zombies=zombies, numGames=1000)



def leave():
    sys.exit()
    KeyboardInterrupt


































# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 