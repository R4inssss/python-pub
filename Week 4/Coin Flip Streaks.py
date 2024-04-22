# Coin Flip Streaks
import random
numberOfStreaks = 0



def streaks():
    for experimentNumber in range(10000):
        # Code that creates a list of 100 'heads' or 'tails' values.
        coins = []
        streak = 0

    for _ in range(100):
        if random.randint(0, 1) == 0:
            coins.append('H')
        else:
            coins.append('T')


    # Code that checks if there is a streak of 6 heads or tails in a row.

        if len(coins) >= 2 and coins[-1] == coins[-2]:
            streak += 1
        else:
            streak = 1
        
        if streak == 6:
            global numberOfStreaks
            numberOfStreaks += 1
            break

streaks()



print('Chance of streak: %s%%' % (numberOfStreaks / 100))