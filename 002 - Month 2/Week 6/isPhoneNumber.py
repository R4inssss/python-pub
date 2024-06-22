# isPhoneNumber.py


def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True


message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)

print ('Done.')




# First, we create a non regex version of our code
# We create a function named isPhoneNumber with the parameter of text
# we capture the length of the text with len, and if the length is not 12
# it returns false
# we then create a for condition, for the integers in range of 0 - 3
# we iterate it through the isdecimal method, which checks if the string consists only of number characters
# if it's not, it returns false
# then, we iterate through the text again for the 7's index in the list, for '-' (8th place)
# we also iterate through our ranges of 8 - 12 using the same method as before
# and call our function with the parameters given, iterating it with the value of the string
# inside of the parentheses

# the new addon creates a variable with 2 phone numbers within it
# we then create a for statement, for the integer in the range of the length of our message
# then it iterates through the for loop, a new chuck of 12 characters from message is assigned
# to the variable chunk. i.e, it does call me at 4 -> all me at 41 -> ll me at 415.. etc
# we then pass chunk to isphonenumber, and it goes throught the same checks as before using our 
# new variable


