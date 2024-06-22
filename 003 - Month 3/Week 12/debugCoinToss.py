#! python3
#       ATBS Practice Project | Chapter 11

import random

guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input().lower()  # converted all cases to lower
toss = random.choice(['heads', 'tails'])  # converted random int to random choice
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = ''  # remade it so that guess variable is empty
    while guess not in ('heads', 'tails'):
        print('Guess the coin toss! Enter heads or tails:')
        # bug one, change guesss into guess
        guess = input().lower()  # converted all cases to lower
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')

# Prompt: Code is meant to be a coin toss game, but the results are always the same
