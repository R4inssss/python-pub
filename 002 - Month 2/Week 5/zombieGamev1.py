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


























# First thing I did was create a better exit with sys.exit()
# Much better :)
# Our objectives are as follows:
# A bot that, after the first roll, randomly decides if it will continue or stop
# A bot that stops rolling after it has rolled two brains
# A bot that stops rolling after it has rolled two shotguns
# A bot that initially decides it’ll roll the dice one to four times, but will stop early if it rolls two shotguns
# A bot that stops rolling after it has rolled more shotguns than brains
# ok for the first one, we import random
# let's replace the code with our own :)
# we first make classes that represent each of the classes needed
# for this, we need to declare our "classes"
# What the fuck is a class :)
# after some research, lots of research, more research i understand a little bit...
# but i do know how to use it now!
# so, classes are objects in our program that represent an object
# these objects can have attributes
# we need to always call __init__ and we need self
# self is a variable that represents the instance of the object itself, this one was easy to understand
# __init__ is a constructor. we went researching! WHAT IS A CONSTRUCTOR
# ok, constructors are used for instantiating an object. it initializes (assigns values) to
# the data members of the class when an object class is created
# WOOO RESEARCH
# there's 2 types of constructors, default and parameterized, which are constructeors with parameters
# It looks like we have to use parameterized constructors, since we have both self and name.
# ok, time to start building
    
# randomZombie, twobrainsZombie, twoshotgunZombies, indecisiveZombie, gunsoverbrainsZombie