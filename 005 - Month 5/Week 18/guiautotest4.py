#! python3
# formFiller.py - Automatically fills in the form.
import pyautogui
import time

# Coordinates of the "Submit another response" link (Replace with actual coordinates)
submitAnotherLink = (x, y) #Change as needed, we can use the print function to capture cursor position if you would like

formData = [{'name': 'Alice', 'fear': 'eavesdroppers', 'source': 'wand',
            'robocop': 4, 'comments': 'Tell Bob I said hi.'},
            {'name': 'Bob', 'fear': 'bees', 'source': 'amulet', 'robocop': 4,
            'comments': 'n/a'},
            {'name': 'Carol', 'fear': 'puppets', 'source': 'crystal ball',
            'robocop': 1, 'comments': 'Please take the puppets out of the break room.'},
            {'name': 'Alex Murphy', 'fear': 'ED-209', 'source': 'money','robocop': 5, 'comments':
              'Protect the innocent. Serve the public trust. Uphold the law.'},
           ]

pyautogui.PAUSE = 0.5
print('Ensure that the browser window is active and the form is loaded!')

for person in formData:
    print('>>> 5-SECOND PAUSE TO LET USER CTRL+C <<<')
    time.sleep(5)
    print('Entering %s info...' % (person['name']))

    # Move to the first field
    pyautogui.press('tab')
    pyautogui.press('tab')

    # Fills out the Name field
    pyautogui.write(person['name'])
    pyautogui.press('tab')

    # Fills out the Greatest Fears field
    pyautogui.write(person['fear'])
    pyautogui.press('tab')

    # Fill out the Source of Wizard Powers field
    if person['source'] == 'wand':
        pyautogui.press('down')
    elif person['source'] == 'amulet':
        pyautogui.press('down')
        pyautogui.press('down')
    elif person['source'] == 'crystal ball':
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('down')
    elif person['source'] == 'money':
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('down')
    pyautogui.press('tab')

    # Fill out the RoboCop field
    if person['robocop'] == 1:
        pyautogui.press('space')
    elif person['robocop'] == 2:
        pyautogui.press('right')
    elif person['robocop'] == 3:
        pyautogui.press('right')
        pyautogui.press('right')
    elif person['robocop'] == 4:
        pyautogui.press('right')
        pyautogui.press('right')
        pyautogui.press('right')
    elif person['robocop'] == 5:
        pyautogui.press('right')
        pyautogui.press('right')
        pyautogui.press('right')
        pyautogui.press('right')
    pyautogui.press('tab')

    # Fill out the Additional Comments field
    pyautogui.write(person['comments'])
    pyautogui.press('tab')

    # "Click" Submit button by pressing Enter
    time.sleep(0.5)  # Wait for the button to activate
    pyautogui.press('enter')

    # Wait until form page has loaded
    print('Submitted form.')
    time.sleep(5)

    # Click the Submit another response link
    pyautogui.click(submitAnotherLink[0], submitAnotherLink[1])
