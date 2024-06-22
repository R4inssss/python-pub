theBoard = {'top-L': 'O', 'top-M': 'X', 'top-R': ' ',
            'mid-L': 'O', 'mid-M': 'O', 'mid-R': 'O',
            'low-L': 'X', 'low-M': ' ', 'low-R': 'X'}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


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