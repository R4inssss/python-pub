#! python3
#       DSA Chapter 1.11 | Exercise 1
#       infinitemokeys.py | Randomly iterates strings until it resolves to the following Shakespearean line:
#       methinks it is like a weasel
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
    newstring = generateOne(28)
    best = 00
    newscore = score(goalstring, newstring)
    while newscore < 1:
        if newscore > best:
            print(newscore, newstring)
            best = newscore
        newstring = generateOne(28)
        newscore = score(goalstring, newstring)

main()

print(score('me thinks it is like a weasel', generateOne(28)))

# We are trying to get our function to resolve to the string of:
# methinks it is like a weasel
