# Picnic Table


def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))

picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 5)



# Fun one, ok so first we create a function named printPicnic, which has the parameters of
# itemDict, leftWidth, and rightWidth
# we then print a string of text "PICNIC ITEMS", centered, with the -- string
# after that, we iterate through our dictionary using the variables k and v, using the .items method
# for each item in the dictionary with k, for key, it places it in the left with the left adjust values and 
# fills in the remaining space with a string of periods.
# it then converts our value to a string, and uses the rightadjust method while calling 
# on the rightWidth variable, making our integer now a string adjust to the right
# we then create a dictionary, with picnic items
# Then we call upong our function, picnicItems, first using
# the values of 12 and 5, the nwith the values of 20 and 5