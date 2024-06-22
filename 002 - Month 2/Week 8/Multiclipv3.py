# mcb.pyw - v2 of multiclipboard
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.
import shelve
import pyperclip
import sys


# Well, we know how to use objects
# We also know how to iterate our selections as a menu, so let's do that!
class Main:
    def __init__(self):
        options = {
            '1': SaveClip,
            '2': LoadClip,
            '3': DeleteClip,
            '4': ShowClip,
            '5': HideEvidence,
        }
        print('''Choose an option:
1 = Save Clipboard
2 = Load Clipboard
3 = Delete Clipboard
4 = List Clipboard
5 = Delete Shelf Keywords''')
        choice = input(">>> ")
        if choice in options:
            if choice in ['1', '2', '3']:
                keyword = input("Keyword >>> ")
                options[choice](keyword)
            else:
                options[choice]()
        else:
            sys.exit('Choose a valid option.')


# Save Clipboard
# learned about with statements, now I don't have to shelve.close :)
class SaveClip:
    def __init__(self, keyword):
        with shelve.open('mcb') as shelf:
            clipped = pyperclip.paste()
            if clipped:
                shelf[keyword] = clipped
                print(f'{keyword} copied to clip.')
            else:
                print('Clipboard is empty')


# Load Clipboard Class
class LoadClip:
    def __init__(self, keyword):
        with shelve.open('mcb') as shelf:
            if keyword in shelf:
                pyperclip.copy(shelf[keyword])
                print(f'{keyword} locked and loaded.')
            else:
                print(f'{keyword} is the wrong ammunition.')


# Delete Clipboard Class
class DeleteClip:
    def __init__(self, keyword):
        with shelve.open('mcb') as shelf:
            if keyword in shelf:
                del shelf[keyword]
                print(f'{keyword} emptied.')
            else:
                print(f'{keyword} does not exist.')


# Copy Clipboard Class
class ShowClip:
    def __init__(self):
        with shelve.open('mcb') as shelf:
            keys = list(shelf.keys())
            if keys:
                pyperclip.copy('\n'.join(keys))
                print('Keywords copied to clipboard.')
            else:
                print('No keys are available.')


# Clear Keywords Class
class HideEvidence:
    def __init__(self):
        with shelve.open('mcb') as shelf:
            shelf.clear()
            print('All keywords deleted.')


if __name__ == '__main__':
    Main()
