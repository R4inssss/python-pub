# chapter 8 project 1 - idiot.py

import pyinputplus as pyip
# Here, we make it easy to type pyinputplus by shortening it to pyip

while True:
    prompt = 'Want to know how to keep an idiot busy for hours?\n'
    response = pyip.inputYesNo(prompt)

# While this is true, aka until it encounts a break statement, it continues to loop the question

    if response == 'no':
        break
# If our response is no, it exits the loop. Otherwise, the loop iterates once again.


























