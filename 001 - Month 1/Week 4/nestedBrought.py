allGuest = {'Alice': {'apples': 5, 'pretzels': 12},
            'Bob': {'ham sandwiches': 3, 'apples': 2},
            'Carol': {'cups': 3, 'apple pies': 1}}

def totalBrought(guests, item):
    numBrought = 0
    for k, v in guests.items():
        numBrought = numBrought + v.get(item, 0)
    return numBrought

print('Number of things being brought:')
print('- Apples         ' + str(totalBrought(allGuest, 'apples')))
print('- Cups           ' + str(totalBrought(allGuest, 'cups')))
print('- Cakes          ' + str(totalBrought(allGuest, 'cakes')))
print('- Ham Sandwiches ' + str(totalBrought(allGuest, 'ham sandwiches')))
print('- Apple Pies     ' + str(totalBrought(allGuest, 'apple pies')))



# So, first we make a dictionary named "allGuest"
# In that dictionary, we have the key Alice, and Alice's value is a dictionary.
# That dictionary has it's own keys of apple and pretzel, with 5 and 12 being the values respectively.
# This goes on with the key of Bob, with it's own value being a dictionary containing more key pairings and
# with Carol, which has it's own dictionary and key pairings as well. Both function the same way as the Alice nested
# dictionary.
# Next, we have the fucntion totalBrought, with the parameters of guest and item
# we also have a new local variable named "numBrought", which is assigned the interger of 0
# then, we call the dictionary.items method using our parameter guest, and use the variables k and v to iterate on it
# the item iterates tuples of the values using guest
# we then iterate over the numBrought variable, and make it
# equvilant to num brought + the variable v using the get method, which takes the "item" value from using the 
# parameter as a reference and returns it
# after, we print strings and create a string from our function
# iterating it with our dictionary followed by a string