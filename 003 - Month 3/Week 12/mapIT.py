#! python3
#       ATBS Chapter 12 | Project 1
#       mapIt.py - launches a map in the browser using an address from the cli

import webbrowser
import sys

import pyperclip

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
