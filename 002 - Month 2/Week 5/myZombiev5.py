# Zombie Game v.3
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
    def turn(self, gameState):
        shotguns = 0
        diceRollResults = zombiedice.roll()
        while diceRollResults and shotguns < 2:
            shotguns += diceRollResults['shotgun']
            if shotguns >= 2:
                break
            diceRollResults = zombiedice.roll()

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

class gunsoverBrainsZombie:
    def __init__(self, name):
        self.name = name
    def turn(self, gameState):
        brains = 0
        shotguns = 0
        diceRollResults = zombiedice.roll()
        while diceRollResults and shotguns >= brains:
            brains += diceRollResults['brains']
            shotguns += diceRollResults['shotgun']
            diceRollResults = zombiedice.roll()




zombies = [
    randomZombie(name='Random Zombie'),
    twobrainsZombie(name='Two Brains Zombie'),
    twoshotgunsZombie(name='Two Shotguns Zombie'),
    indecisiveZombie(name='Indecisive Zombie'),
    gunsoverBrainsZombie(name='Guns Over Brains Zombie'),
]

# Uncomment one of the following lines to run in CLI or Web GUI mode:
#zombiedice.runTournament(zombies=zombies, numGames=1000)
zombiedice.runWebGui(zombies=zombies, numGames=10000)



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
    

# creative names, if i do say so myself!
# we also change the list on the bottom to our new zombies and zombe names
# afterwards, we create def __init__ for all of them, with the parameters of (self, name)
# we declare self.name = name, so it iterates on itself i'm guessing, just stealing code from the original
# we then start on randomzombie
# since we know classes can have multiple functions inside, that means we can create a new function
# we create def turn with the parameters of self and gameState
# we use this for all of them
# our first zombbie needs to use the random choice somehow, what if we use the same variable as before
# and use iterate that on the roll
# so we do that by making diceRollResults = zombiedice.roll()
# we create a while loop, and iterate it through the dicerollResults and our random.choice
# since we only need 2 values, stop or continue, we can iterate that as True or False statements
# creating a program with just 1 to test it, it works!
# next, to make the our nex zombie stop at 2 "brains"
# we create the variable brain, with an initial value of 0
# a little copy pasting from diceRollResults
# now, we can do a whlie loop,
# while we have less than 2 brains
# brains += (add 1) the variable to brains, and iterates on the roll
# very nice!
# run as an independent program again, and with works!
# next, i create another independent programe for my shotgun zombie
# use almost the same code, but added a check for shotgun >= 2, don't want too many of them
# Now, I create indecisive zombie in a new programe
# here it needs "# A bot that initially decides it’ll roll the dice one to four times, but will stop early if it rolls two shotguns
# so something the rolls have to be between 1 and 4 using randint
# max_roll with the method of randint(1,4) for the range of 1 -  4
# now we define the variables needed
# rolls
# shotguns
# so we have 3 variables, max_rolls which is our randint variable, rolls and shotguns
# we need the following: for it to roll but stop early if snotguns >=2
# so, we do a while loop, iterating on our diceRoll with rolls
# rolls has to be less than max rolls and shotguns, which has to be less than 2
# while these conditions are true, we can iterate through shotgun with our dice results
# and iterate to rolls with a value of 1
# we next need a check, to see if the shotgun exceeds the value of 2
# we bring the above idea with if shotguns >=2
# basically now the shotgun zombie is combined with randint!
# run it , and it works. very nice
# last one "A bot that stops rolling after it has rolled more shotguns than brains"
# using the same variables as before with rains and shotguns, we most likely have to do
# if shotguns <= brains
# iterate the rolls on both variables
# and using it's own program,a it works :)
# now i copy and paste each program to here, and combine the list
# YEAAA BOI
# it seems our guns over brains zombie is not winning at all
# lets change that
# making the shotguns >= brains events out the game more
