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


print(generateOne(28))

# We are trying to get our function to resolve to the string of:
# methinks it is like a weasel
