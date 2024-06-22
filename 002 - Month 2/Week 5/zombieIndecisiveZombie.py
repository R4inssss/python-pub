# Zombie game class random
import zombiedice, sys, random

class indecisiveZombie:
    def __init__(self, name):
        self.name = name
    def turn(self, gameState):
        max_rolls = random.randint(1, 4)
        rolls = 0
        shotguns = 0
        diceRollResults = zombiedice.roll()
        while diceRollResults and rolls < max_rolls and shotguns < 2:
            shotguns += diceRollResults['shotgun']
            rolls += 1
            if shotguns >= 2:
                break
            diceRollResults = zombiedice.roll()


zombies = [
    indecisiveZombie(name='Indecisive Zombie')]

zombiedice.runWebGui(zombies=zombies, numGames=1000)



def leave():
    sys.exit()
    KeyboardInterrupt









