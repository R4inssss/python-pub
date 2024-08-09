#! python3
#  guiauto.py - ATBS chapter 20 | Increments i by 1, the values of a and b iterate on it by 100, then we pass it through our moveTo method.


import pyautogui



wh = pyautogui.size()
for i in range(10):
    i += 1
    a = i * 100
    b = i * 100
    pyautogui.moveTo(a, b, duration=0.25)

