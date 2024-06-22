theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

turn = 'X'

for i in range(9):
    printBoard(theBoard)
    print('Turn for the ' + turn + '. Move on which space?')
    move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'








printBoard(theBoard)

# first mistake when reading over the code, wrote print(theBoard)
# it was supposed to be printBoard(theBoard)
# why is the function named printBoard
# it's like list, but stores more data and different usage.
# first, we declare the variable "theBoard" as a dictionary
# the dictionary includes 9 keys, with values of x and o
# yes, I played tic-tac-toe by myself
# the fucntion printBoard calls on the parameter (board)
# it iterates itself over the dictionary, meaning every instance board is called
# it maps to the dictionary for the value
# Then prints
# after that, the printBoard fucntion is called with the parameter of 
# the dictionary
# next, made the variable turn == 'X'
# we then use for interger in range of 9
# which means, for a number in the range of the 9, do the following:
# call the function printBoard with the parameter of theBoard
# again, theBoard acts as the dictionary 
# then it prins out turn, where turn is equal to x or o depending on if x == true
# then we ask for the input (ie- mid-M). 
# we iterate the input to the dictionary, where if the correct key was used
# then it inputs it into the spot as a value
# proceeding to the next turn.
