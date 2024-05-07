#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.
# Project: Phone Number and Email Address Extractor
import sys, pyperclip, re


phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                # area code
    (\s|-|\.)?                        # separator
    (\d{3})                           # first 3 digits
    (\s|-|\.)                         # separator
    (\d{4})                           # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
    )''', re.VERBOSE)
# here we use regular expression to iterate through phone numbers
# the \d{3} searches for 3 digest, the \(d{3}\))? is an optional parameter given the digits
# are inside of a parentheses
# the \s searches for the space/tab/newline, piped in is a \. ? which creates a search for wildcards that is optional
# \d{3} is another 3 digits
# seperator again, this time without the ?
# last for digits using \d{4}
# funny one, using \s* matches everything with the values above, the above being the extension


emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+      # username
    @                      # @ symbol
    [a-zA-Z0-9.-]+         # domain name
    (\.[a-zA-Z]{2,4})       # dot-something
    )''', re.VERBOSE)

# cool search stuff, it's matching all characters upper,lower,numericals, and some symbols
# with the @ using the + (one or more) symbol, proceeded by another object match
# then a dot something in the ranges of 2 - 4 char

text = str(pyperclip.paste())

matches = []
for groups in phoneRegex.findall(text):
       phoneNum = '-'.join([groups[1], groups[3], groups[5]])
       if groups[8] != '':
           phoneNum += ' x' + groups[8]
       matches.append(phoneNum)
for groups in emailRegex.findall(text):
       matches.append(groups[0])

# more join, appending, and fun list making


# Copy results to the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')


# then iterates it through the paperclip.copy method, using newline and .join for our list

# Get text off clipboard (pyperclip)
# Find all phone numbers  and email addresses in the text (regex)
# Paste them onto the clipboard easypz
