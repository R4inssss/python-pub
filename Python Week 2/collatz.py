# Start of my program

import sys # i always import sys now out of habbit!

# One parameter named number
# Hint: An integer number is even if number % 2 == 0, and it’s odd if number % 2 == 1.
def collatz(number):
    if number % 2 == 0:  #Forgot semi colon
        result = number // 2
# if number == even | collatz() print number // 2 and return this value
    else:
        result = 3 * number + 1 # if number == odd  | print and return 3* number + 1
    print(result)
    return result # did not return result | added return
# Returning result allows the program to reused the variable
try: 
    numba = int(input("What's yo numba: ")) # Converts your input to an integer (as seen in input validation example). 
    while numba != 1: # (While number is not 1, do the function)
        numba = collatz(numba) # Running your number to the fbi
except ValueError:
    print('WHAT ARE THOSE!!!') # Example givven of value error here, if int is a non integer string then it prints this.