# madlibs.py v1
# Usage: madlibs.py replaces a text file's <ADJECTIVE | NOUN | ADVERB | VERB> with user-supplied prompts.
# The program will find the occurrences and automatically replace them.

import sys
import re
import os


class Prompt:
    def __init__(self):
        options = {
            '1': MadLibs,
            '2': MadGibs
        }

        print('''Choose an option:
1: Load from file
2: Choose which content you want
Etc: Exit''')
        choice = input('>>> ')
        if choice in options:
            options[choice]()
        else:
            sys.exit('Choose a valid option')


class MadLibs:
    def __init__(self):
        try:
            print('Choose a file:')
            madfile = input('>>> ')
            with open(madfile, 'r') as file:
                content = file.read()

            madpattern = re.compile(r'\b(ADJECTIVE|NOUN|ADVERB|VERB)\b')
            madfind = madpattern.findall(content)

            for placeholder in madfind:
                words = input(f'Enter a {placeholder.lower()}: ')
                content = content.replace(placeholder, words, 1)

            i = 1
            while os.path.exists(f'madlib_{i}.txt'):
                i += 1

            with open(f'madlib_{i}.txt', 'w') as madoutput:
                madoutput.write(content)

            print(f'Your madlib has been saved as madlib_{i}.txt')

        except FileNotFoundError as z:
            print(f'The file was not found: {z}')
        except Exception as e:
            print(f'An error occurred: {e}')


class MadGibs:
    def __init__(self):
        print('No function yet.')


if __name__ == '__main__':
    Prompt()

# Prompt: Create a mad libs program that reads in text files and lets the user add their own text anywhere
# the word ADJECTIVE, NOUN, ADVERB, OR VERB appears in the text file.
