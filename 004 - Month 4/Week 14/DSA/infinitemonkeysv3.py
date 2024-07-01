#! python3
#       DSA Chapter 1.11 | Exercise 1
#       infinitemokeysv3.py | Randomly iterates strings until it resolves to the following Shakespearean line:
#       methinks it is like a weasel
import random

import random


def generateOne(strlen):
    alphabet = 'abcdefghijklmnopqrstuvwxyz '
    res = ""
    for i in range(strlen):  # ensure we're creating a string of the right length
        res = res + alphabet[random.randrange(27)]  # iterate through our 27 "variables"
    return res


def score(goal, teststring):
    a = 0
    for i in range(len(goal)):
        if i < len(teststring) and goal[i] == teststring[i]:
            a += 1
    return a / len(goal)


def main():
    goalstring = 'methinks it is like a weasel'
    print(f'Target/Goal: {goalstring}')
    best = generateOne(len(goalstring))
    bestScore = score(goalstring, best)
    iterations = 0

    while bestScore < 1:   # Our original condition, where 1 is the end goal
        a = generateOne(len(goalstring))  # 'a' is equivalent to the length of our goal (above)
        b = score(goalstring, a)          # 'b' passing our score function using the parameters given
        if b > bestScore:                 # logic check
            best = a
            bestScore = b
            print(f'Best string: {best}, score {bestScore}')

        iterations += 1
        if iterations % 1000 == 0:
            print(f'Iterations: {iterations} | Current score: {bestScore}')
            print(f'Current best score: {best}')  # Looping through and printing our iterations

    print(f'Ran {iterations} iterations and resolved to {best}.')  # Final results, if feasible


if __name__ == "__main__":
    main()

# We are trying to get our function to resolve to the string of:
# methinks it is like a weasel
# our goals, track each iteration (while loop)
# Print target/goal
