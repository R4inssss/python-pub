# Chess Dictionary Validator



def isValidChessBoard(board):
    white = {'wpawn':0, 'wknight': 0, 'wrook': 0, 'wbishop': 0, 'wking': 0, 'wqueen': 0 }
    black = {'bpawn':0, 'bknight': 0, 'brook': 0, 'bbishop': 0, 'bking': 0, 'bqueen': 0 }

    valid_position = [letter + str(i) for i in range(1, 9) for letter in 'abcdefgh']


    for k, pos in board.items(): # first, we declare 2 variables to iterate over the item method for board
        if k not in valid_position: # if our pos is not in our variable, aka not in the range of a1 - h8
            print(f"Invalid position: {k}")
            return False # it returns a false statement
        if not pos[0] in ('w', 'b'): # our next check, if it does not return the values of w and b
            print(f"Invalid position: {pos}")

            return False # another false statement
        pos_type = pos[1:] # in our prior chapter, we learned about iterating tables
        player = pos[0] # here, we make a new variable where player == pos[0]

        if player == 'w': # now, this is basically if pos == 'w'
            white['w' + pos_type] += 1 # white goes up one
        else:
            black['b' + pos_type] += 1 # black goes up one

    # king check, if string king != 1 for either then it returns false
    if white['wking'] != 1 or black['bking'] != 1:
        return False
    
    # here we check to see if white or blacks are over 16
    if sum(white.values()) > 16 or sum(black.values()) > 16:
        return False

    # pawn check, iterates on the dictionary, if the count > 8 then it returns a false statement
    if white['wpawn'] > 8 or black['bpawn'] > 8:
        return False


    return True


board = {'a8': 'brook', 'b8': 'bknight', 'c8': 'bbishop', 'd8': 'bqueen',
        'e8': 'bking', 'f8': 'bbishop', 'g8': 'bknight', 'h8': 'brook',
        'a7': 'bpawn', 'b7': 'bpawn', 'c7': 'bpawn', 'd7': 'bpawn',
        'e7': 'bpawn', 'f7': 'bpawn', 'g7': 'bpawn', 'h7': 'bpawn',
        'a1': 'wrook', 'b1': 'wknight', 'c1': 'wbishop', 'd1': 'wqueen',
        'e1': 'wking', 'f1': 'wbishop', 'g1': 'wknight', 'h1': 'wrook',
        'a2': 'wpawn', 'b2': 'wpawn', 'c2': 'wpawn', 'd2': 'wpawn',
        'e2': 'wpawn', 'f2': 'wpawn', 'g2': 'wpawn', 'h2': 'wpawn'}


print(isValidChessBoard(board))






# Pieces Needed: W/B
# pawn, knight, bishop, rook, queen, king
# 8 pawns | 2 rooks | 2 Knights | 2 bishops | 1 King | 1 Queen
# White Row 1/2 | Black Row 7/8
# Each player pieces <= 16 | <= 8 pawns and all pieces must be on a valid space
# This function should detect when a bug has resulted in an improper chess board.

# So, first I do the easy part, which is making the board. To do this, we just use the layout
# of key = position ; value = piece, where piece is named w/b followed by their characteristics
# we give it the creative name of board
# Afterwards, we need to make a function named isValidChessBoard() that takes our dictionary argument
# so, def isValidChessBoard(board)

# we need to do the following:
# ensure that each player has 16 pieces
# ensure that our function iterates for the pieces on the board, 
# and returns true or false statements
# Ensure the function detects when a bug has resulted in an improper chess board.

# First, we need to assign variables to our players, we can do that as create a dictionary to hold 
# both the keys and values. In this case, I created 2 simliar dictionaries with white and black.
# Next, we should define what is a valid position. In this case, we need to make the valid position a1-h8
# To do this, we need to combine the ranges of both a-h and 1-8

# I had no idea how to do this, or rather a vague idea but no idea how to manifest it
# SO GOOGLE, https://realpython.com/list-comprehension-python/ and I find list comprehension!
# Woawwhhhh so we build it!
# how we did this is by creating a list of valid positions
# in that list, we made a string equal to the interger of i
# it iterates over the numbers 1-8 and for each number, it iterates over a-h.
# for each combination of letter/number, it then concatenates them as a string


# So far we did the following: create a dictionary with position/pieces
# created a function and 2 list for the pieces
# create a list for valid poistions.

# We now need we need to iterate over the board
# so we use board.items()
# above for building of maincode part 1

# we first do checks and updates for each pos
# so after iterating over the board, we check if the positions are valid using k
# where k = the position of the board
# we do the second check, pos, where pos = name of the pieces

# we now have to declare 2variables, our pos types and player
# we increment the pos_type by 1, and make player = list[0]
# we then update the count for the respective player

# our code still returns a false, so apparently there's something wrong with it

# next thing to do, that i forgot is to implement checks for piece count
# so i put a return True statement and hope it works
# it doesnt work!
# I make checks for the kings and the pawns


# IT STILL RETURNS FALSE
# maybe else statement would help
# it did not.

# New check: check for pawns that are > 8 for both white and black.
# did not work

# removed else statement
# still false

# i forgot to make the function iterate using the method of .values()
# changed to white.values() and black.values()

# rewrote checks for sum of values
# moved sum of values up a a section for clarity

# wrote some basic debugging, which checks for invalid pieces
# MEEERRRRHHHHHHH
# everything broken

# so, i fixed things
# first changed the list comprehension. First, the debug showed a8 is considered invalid, thatbeans there is a mismatch for my keys
# but my keys are right, so it's the list comprehension that was wrong
# i spapped the letter + str(i).

# next, i went through and changed the dictionary list to include w/b inside the values
# then, i chhanged everything else that needed w/b for the checks
# it returns true!

