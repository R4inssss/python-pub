# Comma Code

def cookedSpam(cooked):


    if len(cooked) == 0:
        return ''  # Return an empty string if the list is empty


    cooked_copy = cooked[:]  # create a copy of the list to avoid modifying the original
    cooked_copy.insert(-1, 'and')  # insert 'and' before the last item
    return ', '.join(cooked_copy)




spam = ['apples', 'bananas', 'tofu', 'cats']
print(cookedSpam(spam))

# you could also iterate over a variable if needed
# so for i in range(len(cooked)):
# if i == (len cooked) - 1: # here we grab the last item on our list
# result += 'and ' + cooked[1]
#  else result += cooked[i] ', '
# return result
# we could do it this way as well, but rehearsing the copy method used in the chapter and 
# using the methods made is good practice.