# Table Printer

import sys


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def printTable():
    num_columns = len(tableData[0])
    colWidths = [0] * num_columns
    



    for row in tableData:
        for i in range(num_columns):
            colWidths[i] = max(colWidths[i], len(row[i]))
    for i in range(num_columns):
        for row in tableData:
            print(row[i].rjust(colWidths[i]), end=' ')
        print()
    
printTable()



# Objectives
# Function named printTable that takes a list of lists of strings 
# displays them in a well-organized table
# Assume all inner lists will contain the same number of strings

# First, used the table called tableData
# tableData = list
# now create a function named printTable
# in our function we need the table to print out right justified
# we also need it to be pretty
# so, let's start variable building
# we created the variable colWidths, that can store the width of the longest string in tabledata given
# it's values
# next we need a way to parse the data given it's respective rows
# So, we create a row integer
# first, we iterate each row in our list
# Then, we iterate over each index in the current row, using the value of the range of length of the rows
# to do this, we have to do the range(len(variable)) as with before
# we then need to update our values, we make coldWidths[i]
# to represent the max value given a column. 
# Our next goal is to define what is the max value of a collumn
# The max value must iterate through our variables somehow 
# knowing this, we could do something like max(colWidths[i], len(row[i]))
# where we can use the max value given i, given the variables.
# next we create another for loop
# it iterates through our list again using the row variable
# where it then uses i again while parsing through the range of the length of the given data
# it then prings that, using the right adjust method, iterating through with the corresponding widths
# 
# annnnnnd it doesnt work
# 
#        Traceback (most recent call last):
#          File "C:\Users\---\temp\atbs\Week 5\tablePrinter.py", line 23, in <module>
#            printTable()
#          File "C:\Users\---\temp\atbs\Week 5\tablePrinter.py", line 15, in printTable
#            colWidths[i] = max(colWidths[i], len(row[i]))
#                               ~~~~~~~~~^^^
#        IndexError: list index out of range
# since our index is out of range, we have to change the value of the index
# that did not work
# created a new variable to better organize the idea, number of columns.
# where num columns = the length of the table data
# we change colWidth = [0] * num_columns
# and make adjustments accordingly, where we replace the whole speel of len(row) for clarity
# it works, but does not work correctly haha
# that means that the formatting is wrong
# one day I will go back to this