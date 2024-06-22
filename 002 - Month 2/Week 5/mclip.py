#! Python3

# mclip.py - A multi-clipboard program.

import sys, pyperclip
TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
        'busy': """Sorry, can we do this later this week or next week?""",
        'upsell': """Would you consider making this a monthly donation?"""}



if len(sys.argv) < 2:
    print('Usage: python mclip.py [keyphrase] - copy phrase text')
    sys.exit()


keyphrase = sys.argv[1]  # first comand line arg is the keyphrase


if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Text for ' + keyphrase + ' copied to the clipboard.')
else:
    print('There is no text for ' + keyphrase)



# Here, we create a python program that uses the sys and pyperclip modules
# We start by creating a dictionary named TEXT
# The keys for the dictionary are agree, busy, and upsell
# with the pairing/values being the responses
# we then create an if statement
# if the argument from the comandline is empty, using the length of the comandline input
# it prints out the string of text in line 13, 
# and exits the program using the sys.exit method
# we then define the variable keyphrase as the command line argument
# if the variable matches the key in our dictionary
# our pyperclip module uses the copy method, inside of our TEXT dictionary
# and prints out the string on line 22
# else, it states that there is no keyphrase, given our dictionary keys
