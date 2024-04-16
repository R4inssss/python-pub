dogNames = []
while True: # While you keep inserting the variable of name =! blank
    print('Enter the name of doggo!' + str(len(dogNames) + 1 ) +   # I messed up here, I did )) + 1; instead it was supposed to be ) + 1 ) +
        ' (Or ender nothing to stop)') # In this line and the one above, it ask for the name of the dogs by printing out the text, followed by the string of the lengths of current dogs and addition to 1.
    name = input() # The name of the dog is the input
    if name == '': # if the name is blank
        break # loop breaks
    dogNames = dogNames + [name] # list concatenation
print('The doggos are: ') # print
for name in dogNames: #for name in the list
    print(' ' + name) # print the  doggos are (the blank space) + (name of the input)
