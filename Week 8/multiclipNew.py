# mcb.pyw - v2 of multiclipboard
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.
import shelve
import pyperclip
import sys

mcbShelf = shelve.open('mcb')
# The shelf name will be named with the prefix of mcb
# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    # Here, we use sys.argv to retrieve arguments from our commandline. The first CLI argument (which is the index of 1)
    # is saved, the second cl argument is the keyword for the current content of the clipboard. If there is only one cl
    # argument, we assume it is a list or a keyword to load content onto our clipboard
    # List keywords and load content.

    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
    # we use an if condition here and pass it as a list of string, then copied to our shelf key
    # else if the keyword exist in our shelf, we load the value onto the clipboard
mcbShelf.close()
